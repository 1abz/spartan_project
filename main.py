import management
import management1
from spartan import Spartan
import json
from flask import Flask, request,  jsonify

flask_object = Flask(__name__)


# http://127.0.0.1:5000/
@flask_object.route('/', methods=['GET'])
def homepage():
    return 'Welcome to the Trainee management system. "\n" Website homepage: http://127.0.0.1:5000/ "\n" http://127.0.0.1:5000/spartan/add '

# http://127.0.0.1:5000/spartan/add
@flask_object.route('/spartan/add', methods = ['POST'])
def add_spartan():
    management.add_spartan_api()










# http://127.0.0.1:5000/spartan/1
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_record_getter(spartan_id):
    return management.read_spartan_id_api(spartan_id)


if __name__ == "__main__":

    flask_object.run()
