import management
from flask import Flask, request,  jsonify

flask_object = Flask(__name__)

# http://127.0.0.1:5000/
@flask_object.route('/', methods=['GET'])
def homepage():
    return "Welcome to the Trainee management system. "

# http://127.0.0.1:5000/spartan/add
@flask_object.route('/spartan/add', methods = ['POST'])
def add_employee():
    spartan_data = request.json
    return management.add_spartan_api(spartan_data)



# http://127.0.0.1:5000/spartan/1
#@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
#def spartan_getter(spartan_id):
    #return f"Your asking for information about spartan ID: {spartan_id}"


# http://127.0.0.1:5000/spartan/1
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_record_getter(spartan_id):
    return management.read_spartan_id_api(spartan_id)








if __name__ == "__main__":

    flask_object.run()
