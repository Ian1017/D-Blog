from flask import Flask
from config import config_options
from flask_fontawesome import FontAwesome

fa = FontAwesome

def create_app(config_name):
    '''
    Function that takes configuration setting as an arguement

    Args:
    config_name: name if the configuration to be used
    '''

    # Initializing application
    app = Flask(__name__)

    #creating the app configuration
    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    ##fa.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
   
    return app



class BlogPost(db.Model):

    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())

    @classmethod
    def get_blogposts(cls, id):
        blogposts = BlogPost.query.order_by(blogpost_id=id).desc().all()
        return blogposts

    def __repr__(self):
        return f'BlogPost {self.description}' 