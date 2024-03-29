import os
from flask import Flask, request, render_template
from calculator.source.paldeck import dict_paldeck
from calculator.source.parent_oriented import get_child
from calculator.source.child_oriented import get_parent

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

    @app.route('/breeder/get_child', methods=['GET', 'POST'])
    def breeder_get_child():
        child_result = None
        if request.method == 'POST':
            p1 = float(request.form.get('parent1'))
            p2 = float(request.form.get('parent2'))

            child_result = get_child(p1, p2)

        return render_template('breeder_get_child.html', dict_paldeck=dict_paldeck, child_result=child_result)

    
    @app.route('/breeder/get_parents', methods=['GET', 'POST'])
    def breeder_get_parents():        
        name_list = []
        if request.method == 'POST':
            child = float(request.form.get('dropdown1'))
            list_parent_pairs = get_parent(child)
            name_list = [(d1['Name'], d2['Name']) for d1, d2 in list_parent_pairs]
        return render_template('breeder_get_parents.html', dict_paldeck=dict_paldeck, name_list=name_list)
    
    @app.route('/calculator', methods=['GET', 'POST'])
    def calculator():
        my_list = [
        {"name": "Lamball", "image_url": "https://palworld.wiki.gg/images/e/ee/Lamball_icon.png"},
        {"name": "Cattiva", "image_url": "https://palworld.wiki.gg/images/6/6d/Cattiva_icon.png"},
        {"name": "Pengullet", "image_url": "https://palworld.wiki.gg/images/5/5f/Pengullet_icon.png"}
        ]
        return render_template('calculator.html', my_list=my_list, dict_paldeck=dict_paldeck)
        
    return app