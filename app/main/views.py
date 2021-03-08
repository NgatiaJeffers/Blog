import os
import secrets

import app
from PIL import Image
from . import main
from .. import db
from ..models import Blog, Comment
from ..requests import get_random_quote
from .forms import BlogForm, UpdateProfile
from flask_login import current_user, login_required
from flask import render_template, flash, request, url_for, abort, redirect


@main.route('/')
@main.route('/home')
def index():
    quotes = get_random_quote()
    blogs = Blog.query.all()
    return render_template('index.html', quotes = quotes, blog = blogs, user = current_user)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/photos', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@main.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user.image_file = picture_file
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()

        flash('Account Updated Succefully. Yeaah!!')

        return redirect(url_for('main.profile'))

    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
    image_file = url_for('static', filename = 'photos/' + user.image_file)

    title = 'Profile || Dev Blog'
    return render_template('profile/profile.html', title = title, image_file = image_file, form = form)

@main.route('/blog/<int:blog_id>')
@login_required
def blog(blog_id):
    comments = Comment.query.filter_by(blog_id = id).all()
    heading = 'comments'
    blog = Blog.query.get_or_404(blog_id)

    title = 'Blog || Dev Blog'
    return render_template('blog/blog.html', title = blog.title, blog = blog, comments = comments, heading = heading)

@main.route('/new_blog', methods = ['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title = form.title.data, body = form.body.data, user = current_user)
        blog.save_blog()

        flash('Blog posted 😄.')

        return redirect(url_for('main.index'))
    title = 'Blog || Dev Blog'
    return render_template('blog/new_blog.html', title = title, form = form)

@main.route('/blog/<int:blog_id>/update', methods = ['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.user  != current_user:

        abort(403)
    form = BlogForm()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.body = form.body.data

        db.session.commit()

        flash('Blog Updated 😄.')

        return redirect(url_for('main.blog', blog_id = id))

    elif request.method == 'GET':
        form.title.data = blog.title
        form.boby.data = blog.body

    title = 'Update || Dev Blog'
    return render_template('blog/new_blog.html', title = title, form = form)