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

    @app.route('/add', methods=['GET', 'POST'])
    def add_numbers():
        result = ""
        
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
    
    
    @app.route('/breeder', methods=['GET', 'POST'])
    def breeder():
        result = ""
        
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
    
    @app.route('/calculator', methods=['GET', 'POST'])
    def calculator():
        my_list = [
        {"name": "Lamball", "image_url": "https://palworld.wiki.gg/images/e/ee/Lamball_icon.png"},
        {"name": "Cattiva", "image_url": "https://palworld.wiki.gg/images/6/6d/Cattiva_icon.png"},
        {"name": "Pengullet", "image_url": "https://palworld.wiki.gg/images/5/5f/Pengullet_icon.png"}
        ]
        return render_template('calculator.html', my_list=my_list)
        
    return app