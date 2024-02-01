import os
from flask import Flask, request

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
    
    @app.route('/add')
    def add_numbers():
        try:
            # Get the values from the query parameters in the URL
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))

            # Perform the addition
            result = num1 + num2

            # Return the result as a string
            return f'The sum of {num1} and {num2} is: {result}'

        except ValueError:
            # Handle the case where the user provides non-numeric input
            return 'Invalid input. Please provide numeric values for num1 and num2.'
        
    return app