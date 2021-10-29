# This file contains an example Flask-User application.
# To keep the example simple, we are applying some unusual techniques:
# - Placing everything in one file
# - Using class-based configuration (instead of file-based configuration)
# - Using string-based templates (instead of file-based templates)

from flask import Flask, render_template_string,render_template, request, redirect
from flask import jsonify


def create_app():

    app = Flask(__name__)
    
    @app.route('/')
    def home3():
        """Renders the home page."""
        return render_template(
        'page3.html',
        title='Home Page',
        #year=datetime.now().year,
        )
    @app.route('/page4')
    def home4():
        """Renders the home page."""
        return render_template(
        'page4.html',
        title='Home Page',
        #year=datetime.now().year,
        )


    return app

    

# Start development web server
if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)