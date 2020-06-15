from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root page  function that return index and its data
    '''
    title = "Ian's Blog"
    intro = "Welcome to my journey"

    return render_template('index.html, title = title, intro = intro')

@main.route('/about')
def about():
    '''
    View about page function that returns the about page
    '''
    return render_template('about.html')

@main.route('/blogposts/new', methods = ['GET', 'POST'])
@login_required
def new_blogpost():
    form = BlogPostForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        date = date.now
        new_blogpost = BlogPost(owner_id = current_user._get_current_object().id, title = title, description = description)
        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('blogposts.html', form = form)

@main.route('/contact')
def contact():
    '''
    View function that returns the contact page
    '''
    return render_template('contact.html') 