from flask import Flask, request,  jsonify

flask_object = Flask(__name__)

# http://127.0.0.1:5000/
@flask_object.route('/', methods=['GET'])
def homepage():
    return "Welcome to the Trainee management system"

# http://127.0.0.1:5000/spartan/add
@flask_object.route('/spartan/add', methods = ['POST'])
def add_employee():
    spartan_data = request.json
    spartan_id = spartan_data['e_id']
    first_name = spartan_data['f_name']
    last_name = spartan_data['l_name']
    #   Cal the method that will create the employee record
    return f"The employee ({spartan_id}: {first_name} - {last_name}) will be added to the database"

# http://127.0.0.1:5000/spartan/1
#@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
#def spartan_getter(spartan_id):
    #return f"Your asking for information about spartan ID: {spartan_id}"


# http://127.0.0.1:5000/spartan/1
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_record_getter(spartan_id):
    data = jsonify(id=spartan_id, fname = "Abz", sname="Mohammed", byear="1990", bmonth="2", bday="1", course="", stream="devops")
    return data







if __name__ == "__main__":

    flask_object.run()
