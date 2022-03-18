from spartan import Spartan
import json

def read_option():
    while True:
        user_option = input("Spartan Management options: add: Add Spartan, remove: Remove Spartan, list: List Spartan ,update: Update Spartan Data, exit: Exit the app, total: Total number of Spartans, retrieve: Retrieve Spartan using ID: load: Load from json, save: Save to json")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "update", "list", "exit", "total", "retrieve", "save", "load"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_first_name():
    while True:
        first_name = input("Please Enter The Spartan First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print('"Error, The Spartan First Name should be at least 2 Characters"')


def read_last_name():
    while True:
        last_name = input("Please Enter The Spartan Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Spartan Last Name should be at least 2 Characters")


def read_course():
    while True:
        course = input("Please Enter The Spartan Course:")
        course = course.strip()

        if len(course) >= 1:
            return course
        else:
            print("Error, The Spartan Position should be at least 1 Characters")


def read_year():
    while True:
        year_str = input("Please Enter the Spartan Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Spartan Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Spartan Birth Year should be a number")


def read_month():
    while True:
        month_str = input("Please Enter the Spartan Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Spartan Birth Month should be between 1 and 12")
        else:
            print("Error, The Spartan Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Spartan Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Spartan Birth Day should be between 1 and 31")
        else:
            print("Error, The Spartan Birth Day should be a number")


def read_stream():
    while True:
        stream = input("Enter Spartan stream: ")
        stream = stream.strip()
        if len(stream) >= 1:
            return stream
        else:
            print("Error, The Spartan Stream should be at least 1 Characters")



def create_spartan_object():
    spartan_id = read_spartan_id()
    spartan_firstname = read_first_name()
    spartan_lastname = read_last_name()
    spartan_course = read_course()

    spartan_birthy = read_year()
    spartan_birthm = read_month()

    spartan_birthd = read_day()

    spartan_stream = read_stream()

    s = Spartan(spartan_id, spartan_firstname, spartan_lastname, spartan_birthd,
                  spartan_birthm, spartan_birthy, spartan_course, spartan_stream)

    return s


def update_spartan(spartan_id):
    field_option = read_field_option()
    if field_option == "first_name":
        new_first_name = read_first_name()
        spartan_dict[spartan_id].set_first_name(new_first_name)
    elif field_option == "last_name":
        new_last_name = read_last_name()
        spartan_dict[spartan_id].set_last_name( new_last_name)
    elif field_option == "course":
        new_course = read_course()
        spartan_dict[spartan_id].set_course(new_course)
    elif field_option == "birth_year":
        new_birth_year = read_year()
        spartan_dict[spartan_id].set_birth_year(new_birth_year)
    elif field_option == "birth_month":
        new_birth_month = read_month()
        spartan_dict[spartan_id].set_birth_month(new_birth_month)
    elif field_option == "birth_day":
        new_birth_day = read_day()
        spartan_dict[spartan_id].set_birth_day(new_birth_day)
    elif field_option == "stream":
        new_stream = read_stream()
        spartan_dict[spartan_id].set_stream(new_stream)


def read_spartan_id():
    while True:
        id_str = input("Please Enter the Spartan ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0:
                return id
            else:
                print("Error, The Spartan ID should be positive number")
        else:
            print("Error, The Spartan ID should be a number")


def read_spartan_id_api(spartaId):
    sparta_api_dict = {}
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    for sparta_id_key in data:
        sparta_id = data[sparta_id_key]['sid']
        sparta_fn = data[sparta_id_key]['sfirst_name']
        sparta_ln = data[sparta_id_key]['slast_name']
        sparta_bd = data[sparta_id_key]['sbirth_day']
        sparta_bm = data[sparta_id_key]['sbirth_month']
        sparta_by = data[sparta_id_key]['sbirth_year']
        sparta_c = data[sparta_id_key]['scourse']
        sparta_s = data[sparta_id_key]['sstream']

        s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
        sparta_api_dict[sparta_id] = s_obj


    if int(spartaId) in sparta_api_dict:
        return str(sparta_api_dict.get(int(spartaId)))
    else:
        return "ID key not found"


def add_spartan_api(sparta_data):
    sparta_api_dict = {}
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    for sparta_id_key in data:
        sparta_id = data[sparta_id_key]['sid']
        sparta_fn = data[sparta_id_key]['sfirst_name']
        sparta_ln = data[sparta_id_key]['slast_name']
        sparta_bd = data[sparta_id_key]['sbirth_day']
        sparta_bm = data[sparta_id_key]['sbirth_month']
        sparta_by = data[sparta_id_key]['sbirth_year']
        sparta_c = data[sparta_id_key]['scourse']
        sparta_s = data[sparta_id_key]['sstream']

        s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
        sparta_api_dict[sparta_id] = s_obj

    sparta_id = sparta_data['sid']
    sparta_fn = sparta_data['sfirst_name']
    sparta_ln = sparta_data['slast_name']
    sparta_bd = sparta_data['sbirth_day']
    sparta_bm = sparta_data['sbirth_month']
    sparta_by = sparta_data['sbirth_year']
    sparta_c = sparta_data['scourse']
    sparta_s = sparta_data['sstream']

    s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
    sparta_api_dict[sparta_id] = s_obj

    with open("data.json", "w") as data:
        json.dump(sparta_api_dict, data)
    return "completed"






def print_all_spartans_data():
    for spartan_id_key in spartan_dict:
        print(f"(The data of the spartan with Spartan_ID = {spartan_id_key}")
        print(spartan_dict[spartan_id_key])


def read_field_option():
    while True:
        field_option = input("Please Enter the field you want to update: first_name, last_name, course, birth_year, birth_month, birth_day, stream:")
        field_option = field_option.strip()

        if field_option in ["first_name", "last_name", "course", "birth_year", "birth_month", "birth_day", "stream"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")


def save_to_json():
    temp_dict_of_dict = {}
    for spartans_id in spartan_dict:
        spartan_objects = spartan_dict[spartans_id]
        spartan_dicti = spartan_objects.__dict__
        temp_dict_of_dict[spartans_id] = spartan_dicti

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)


def load_from_json():
    global spartan_dict
    try:
        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)
    except FileNotFoundError:
        print("The file data.json doesn't exist")

    for sparta_id_key in temp_dict_of_dict:
        sparta_id = temp_dict_of_dict[sparta_id_key]['sid']
        sparta_fn = temp_dict_of_dict[sparta_id_key]['sfirst_name']
        sparta_ln = temp_dict_of_dict[sparta_id_key]['slast_name']
        sparta_bd = temp_dict_of_dict[sparta_id_key]['sbirth_day']
        sparta_bm = temp_dict_of_dict[sparta_id_key]['sbirth_month']
        sparta_by = temp_dict_of_dict[sparta_id_key]['sbirth_year']
        sparta_c = temp_dict_of_dict[sparta_id_key]['scourse']
        sparta_s = temp_dict_of_dict[sparta_id_key]['sstream']

        s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
        spartan_dict[sparta_id_key] = s_obj
    print('testing')
    print(temp_dict_of_dict)



if __name__ == "__main__":

    spartan_dict = {}

    with open("recording_log.txt", 'a+') as log_file:
        log_file.write("Employee Management system log book created" + "\n")
        #log_file.close()

    while True:
        option = read_option()

        if option == "add":
            print("The user wants to add an Employee")
            spartan_object = create_spartan_object()

            spartan_id = spartan_object.get_id()
            spartan_dict[spartan_id] = spartan_object
            print(spartan_dict.get(spartan_id))
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("New employee added" + "\n")


        elif option == "remove":
            print("The user wants to remove an Employee")
            spartan_id = read_spartan_id()
            del spartan_dict[spartan_id]
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("Employee removed" + "\n")

        elif option == "list":
            print("The user wants a list of the employees")
            print_all_spartans_data()
            #for spartan_id_key in spartan_dict:
                #print(f"The data of the spartan with Spartan_ID = {spartan_id_key}")
                #print(spartan_dict[spartan_id_key])
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("All spartans printed" + "\n")

        elif option == "update":
            print("The user wants to update the data of an employee")
            spartan_id = read_spartan_id()
            update_spartan(spartan_id)
            print(spartan_dict.get(spartan_id))
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("Spartan updated" + "\n")

        elif option == "total":
            print("The user wants the total number of spartans")
            print(len(spartan_dict))

        elif option == "retrieve":
            print("The user wants to retrieve an spartans using ID")
            spartan_id = read_spartan_id()
            print(spartan_dict.get(spartan_id))

        elif option == "exit":
            print("Thanks, see you later")
            break

        elif option == "save":
            print("The data will be saved to json file")
            save_to_json()

        elif option == "load":
            print("the data will be loaded from a JSON file")
            load_from_json()

        else:
            print("Unknown option")
