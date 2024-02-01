import os
from flask import Flask, request, render_template

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/breeder')
    def breeder():
        return 'Hello, breeder!'
    
    @app.route('/add', methods=['GET', 'POST'])
    def add_numbers():
        result = None
        
        if request.method == 'POST':
            # If the form is submitted, process the form data
            try:
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result = num1 + num2
            except ValueError:
                return 'Invalid input. Please provide numeric values for num1 and num2.'

        # Render the HTML template and pass the result to display
        return render_template('add_numbers.html', result=result)
        
    return app