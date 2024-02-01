import os
from flask import Flask, request, render_template
from calculator.source.paldeck import dict_paldeck

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

    @app.route('/breeder', methods=['GET', 'POST'])
    def breeder():        

        if request.method == 'POST':
            parent1 = float(request.form.get('dropdown1'))
            parent2 = float(request.form.get('dropdown2'))            
            selected_option1 = dict_paldeck[parent1]['Name']
            selected_option2 = dict_paldeck[parent2]['Name']
            print(f'Selected Option 1: {selected_option1}')
            print(f'Selected Option 1: {parent1}')
            print(f'Selected Option 1: {selected_option2}')
            print(f'Selected Option 2: {parent2}')
            
        return render_template('breeder.html', dict_paldex=dict_paldeck)
    
    @app.route('/calculator', methods=['GET', 'POST'])
    def calculator():
        my_list = [
        {"name": "Lamball", "image_url": "https://palworld.wiki.gg/images/e/ee/Lamball_icon.png"},
        {"name": "Cattiva", "image_url": "https://palworld.wiki.gg/images/6/6d/Cattiva_icon.png"},
        {"name": "Pengullet", "image_url": "https://palworld.wiki.gg/images/5/5f/Pengullet_icon.png"}
        ]
        return render_template('calculator.html', my_list=my_list)
        
    return app