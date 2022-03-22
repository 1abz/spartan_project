import management
from flask import Flask

flask_object = Flask(__name__)


# http://127.0.0.1:5000/
@flask_object.route('/', methods=['GET'])
def homepage():
    description = '''

    1 -  http://127.0.0.1:5000/ - HOMEPAGE  
    
    2 -  http://127.0.0.1:5000/spartan/add  - METHOD=POST route: /spartan/add 
        Use this API to save the detail of new spartan into a JSON database
        
    3 -  http://127.0.0.1:5000/spartan/1 - METHOD=GET route: /spartan/<spartan_id>
        Use this API to display details of spartan using the spartan ID. Replace "1" with any ID on the database.
        An error message should be returned if the spartan_id doesn't exist in the system. 
      
    4 -  http://127.0.0.1:5000/spartan/remove?id=353 - METHOD=POST route: /spartan/remove?id=sparta_id 
        Use this API to delete details of spartan using the spartan ID. Replace "353" with any ID on the database.
    
    5 - http://127.0.0.1:5000/spartan - METHOD: GET, route: /spartan 
        Use this API to display details of all spartans in database of json file. 
        '''

    return description


# http://127.0.0.1:5000/spartan/add
@flask_object.route('/spartan/add', methods=['POST'])
def add_spartan():
    return management.add_spartan_api()

# http://127.0.0.1:5000/spartan/1
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_record_getter(spartan_id):
    return management.spartan_getter(spartan_id)


# http://127.0.0.1:5000/spartan/remove?id=353
@flask_object.route('/spartan/remove', methods=['POST'])
def spartan_record_deleter():
    return management.spartan_deleter(id)


# http://127.0.0.1:5000/spartan
@flask_object.route('/spartan', methods=['GET'])
def whole_spartan_list():
    return management.spartan_list()


if __name__ == "__main__":

    flask_object.run()
