from spartan import Spartan
import json
from flask import request

all_spartans = {}


def spartan_validation(spartan_data):

    sparta_id = spartan_data['sid']
    id = int(sparta_id)
    if id < 1:
        return "Error, The Spartan ID should be positive number"

    sparta_fn = spartan_data['sfirst_name']
    sparta_fn = sparta_fn.strip()
    if len(sparta_fn) <= 2:
        return "Error, The Spartan first name should be at least 2 characters"

    sparta_ln = spartan_data['slast_name']
    sparta_ln = sparta_ln.strip()
    if len(sparta_ln) < 2:
        return "Error, The Spartan last name should be at least 2 characters"

    sparta_bd = spartan_data['sbirth_day']
    day = int(sparta_bd)
    if (day < 1) or (day > 31):
        return "Error, The Spartan birth date should be between 1 and 31."

    sparta_bm = spartan_data['sbirth_month']
    month = int(sparta_bm)
    if (month < 1) or (month > 12):
        return "Error, The Spartan birth month should be between 1 and 12."

    sparta_by = spartan_data['sbirth_year']
    year = int(sparta_by)
    if (year < 1900) or (year > 2004):
        return "Error, The Spartan birth year should be between 1900 and 2004."

    sparta_c = spartan_data['scourse']
    sparta_c = sparta_c.strip()
    if len(sparta_c) < 3:
        return "Error, The Spartan course name should be at least 3 characters"

    sparta_s = spartan_data['sstream']
    sparta_s = sparta_s.strip()
    if len(sparta_s) < 3:
        return "Error, The Spartan stream name should be at least 3 characters"

    return None


def create_new_spartan(spartan_data):

    sparta_id = spartan_data['sid']
    sparta_fn = spartan_data['sfirst_name']
    sparta_ln = spartan_data['slast_name']
    sparta_bd = spartan_data['sbirth_day']
    sparta_bm = spartan_data['sbirth_month']
    sparta_by = spartan_data['sbirth_year']
    sparta_c = spartan_data['scourse']
    sparta_s = spartan_data['sstream']

    s_obj = Spartan(sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)

    return s_obj


def add_spartan_api():

    global all_spartans
    tempdict_spartans = {}
    spartan_data = request.json
    data_validation = spartan_validation(spartan_data)
    if data_validation is None:
        new_spartan_obj = create_new_spartan(spartan_data)

        idstr = str(new_spartan_obj.get_id())
        all_spartans[idstr] = new_spartan_obj

        for spartan_id in all_spartans:
            spartan_obj = all_spartans[spartan_id]
            spartan_dict = spartan_obj.__dict__
            tempdict_spartans[spartan_id] = spartan_dict

        with open("data.json", "w") as data_file:
            json.dump(tempdict_spartans, data_file)

        return 'New Spartan Successfully added.'
    else:
        return data_validation


def spartan_getter(spartan_id):
    global all_spartans
    loaded_dictionary = {}
    try:
        with open("data.json", "r") as data_file:
            loaded_dictionary = json.load(data_file)
    except FileNotFoundError:
        print('File named data.json not found')

    for s_Id in loaded_dictionary:
        sparta_id = loaded_dictionary[s_Id]['sid']
        sparta_fn = loaded_dictionary[s_Id]['sfirst_name']
        sparta_ln = loaded_dictionary[s_Id]['slast_name']
        sparta_bd = loaded_dictionary[s_Id]['sbirth_day']
        sparta_bm = loaded_dictionary[s_Id]['sbirth_month']
        sparta_by = loaded_dictionary[s_Id]['sbirth_year']
        sparta_c = loaded_dictionary[s_Id]['scourse']
        sparta_s = loaded_dictionary[s_Id]['sstream']

        loaded_spartan = Spartan(sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)

        all_spartans[sparta_id] = loaded_spartan

    tempdict_spartans = {}
    for sparta_id in all_spartans:
        spartan_object = all_spartans[sparta_id]
        spartans_dict = spartan_object.__dict__
        tempdict_spartans[sparta_id] = spartans_dict
        int_id = int(spartan_id)
        if int_id in tempdict_spartans:
            return tempdict_spartans[int_id]



def spartan_deleter(spartan_id):
    global all_spartans
    tempdict_spartans = {}
    id_requested = int(request.args.get("id"))

    try:
        with open("data.json", "r") as data_file:
            loaded_dictionary = json.load(data_file)
    except FileNotFoundError:
        print('File named data.json not found')

    for s_Id in loaded_dictionary:
        sparta_id = loaded_dictionary[s_Id]['sid']
        sparta_fn = loaded_dictionary[s_Id]['sfirst_name']
        sparta_ln = loaded_dictionary[s_Id]['slast_name']
        sparta_bd = loaded_dictionary[s_Id]['sbirth_day']
        sparta_bm = loaded_dictionary[s_Id]['sbirth_month']
        sparta_by = loaded_dictionary[s_Id]['sbirth_year']
        sparta_c = loaded_dictionary[s_Id]['scourse']
        sparta_s = loaded_dictionary[s_Id]['sstream']

        loaded_spartan = Spartan(sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)

        all_spartans[sparta_id] = loaded_spartan


    if id_requested in all_spartans.keys():
        del all_spartans[id_requested]
        for spartan_id in all_spartans:
            spartan_obj = all_spartans[spartan_id]
            spartan_dict = spartan_obj.__dict__
            tempdict_spartans[spartan_id] = spartan_dict

        with open("data.json", "w") as data_file:
            json.dump(tempdict_spartans, data_file)

        return f'Spartan: {id_requested} successfully deleted'
    else:
        return f'Spartan: {id_requested} is not in database'


def spartan_list():
    global all_spartans
    all_spartans_temp_dict = {}
    try:
        with open("data.json", "r") as data_file:
            all_spartans_temp_dict = json.load(data_file)
    except FileNotFoundError:
        print('File named data.json not found')
    return all_spartans_temp_dict




