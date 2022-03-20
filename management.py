from spartan import Spartan
import json
from flask import request

all_spartans = {}


def add_spartan_api():
    global all_spartans
    t_spartans = {}
    new_spartan_obj = spartan_api_insert()
    all_spartans[new_spartan_obj.get_id()] = new_spartan_obj

    # Convert spartan object to dictionary
    for spartan_id in all_spartans:
        spartan_obj = all_spartans[spartan_id]
        spartan_dict = spartan_obj.__dict__
        t_spartans[spartan_id] = spartan_dict
    with open("data.json", "w") as data_file:
        json.dump(t_spartans, data_file)


    #sparta_id = new_spartan_obj[spartan.Spartan.get_id()]
    #all_spartans[Spartan.get_id()] = new_spartan_obj
    #sparta_id = new_spartan_obj.
    #all_spartans[spartan_id] = new_spartan_obj


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






