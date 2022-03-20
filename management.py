from spartan import Spartan
import json
from flask import request, jsonify

all_spartans = {}


def spartan_api_insert():
    spartan_data = request.json

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
    new_spartan_obj = spartan_api_insert()


    idstr = str(new_spartan_obj.get_id())
    all_spartans[idstr] = new_spartan_obj

    for spartan_id in all_spartans:
        spartan_obj = all_spartans[spartan_id]
        spartan_dict = spartan_obj.__dict__
        tempdict_spartans[spartan_id] = spartan_dict
        
        
    with open("data.json", "w") as data_file:
        json.dump(tempdict_spartans, data_file)
    
    return 'New Spartan Successfully added.'


def spartan_getter(spartan_id):
    global all_spartans
    loaded_dictionary = {}
    try:
        with open("data.json", "r") as data_file:
            loaded_dictionary = json.load(data_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

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

    for id in all_spartans:
        spartan_object = all_spartans[id]
        spartans_dict = spartan_object.__dict__
        tempdict_spartans[id] = spartans_dict
        id_integer = int(spartan_id)
        if id_integer in tempdict_spartans:
            return tempdict_spartans[id_integer]


def spartan_deleter(id):
    global all_spartans
    id = int(request.args.get("id"))

    try:
        with open("data.json", "r") as data_file:
            loaded_dictionary = json.load(data_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

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











