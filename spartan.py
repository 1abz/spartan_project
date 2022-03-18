

class Spartan:

    def __init__(self, id, first_name, last_name, birthDate, birthMonth, birthYear, course, stream):
        self.sid = id
        self.sfirst_name = first_name
        self.slast_name = last_name
        self.sbirth_day = birthDate
        self.sbirth_month = birthMonth
        self.sbirth_year = birthYear
        self.scourse = course
        self.sstream = stream


    def set_id(self, id):
        self.sid = id

    def set_first_name(self, first_name):
        self.sfirst_name = first_name

    def set_last_name(self, last_name):
        self.slast_name = last_name

    def set_birth_year(self, birth_year):
        self.sbirth_year = birth_year

    def set_birth_month(self, birth_month):
        self.sbirth_month = birth_month

    def set_birth_day(self, birth_day):
        self.sbirth_day = birth_day

    def set_course(self, course):
        self.scourse = course

    def set_stream(self, stream):
        self.sstream = stream



    def get_id(self):
        return self.sid

    def get_first_name(self):
        return self.sfirst_name

    def get_last_name(self):
        return self.slast_name

    def get_birth_year(self):
        return self.sbirth_year

    def get_birth_month(self):
        return self.sbirth_month

    def get_birth_day(self):
        return self.sbirth_day

    def get_course(self):
        return self.scourse

    def get_stream(self):
        return self.sstream

    def __str__(self):
        return f"'first_name': '{self.sfirst_name}', 'last_name': '{self.slast_name}', 'birth_year':'{self.sbirth_year}', 'birth_month':'{self.sbirth_month}', 'birth_day': '{self.sbirth_day}', 'course':'{self.scourse}', 'stream': '{self.sstream}', 'spartan_id': '{self.sid}'"

    def print_spartan_info(self):
        print(f'Spartan ID: {self.sid}')
        print(f"Spartan first name: {self.sfirst_name}")
        print(f"Spartan last name: {self.slast_name}")
        print(f"Spartan birth day: {self.sbirth_day}")
        print(f"Spartan birth month: {self.sbirth_month}")
        print(f"Spartan birth year: {self.sbirth_year}")
        print(f"Spartan course: {self.scourse}")
        print(f"Spartan stream: {self.sstream}")

'''
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

        s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
        sparta_api_dict[sparta_id] = s_obj

    sparta_id = sparta_data['sid']
    sparta_fn = sparta_data['sfirst_name']
    sparta_ln = sparta_data['slast_name']
    sparta_bd = sparta_data['sbirth_day']
    sparta_bm = sparta_data['sbirth_month']
    sparta_by = sparta_data['sbirth_year']
    sparta_c = sparta_data['scourse']
    sparta_s = sparta_data['sstream']

    s_obj = (sparta_id, sparta_fn, sparta_ln, sparta_bd, sparta_bm, sparta_by, sparta_c, sparta_s)
    sparta_api_dict[sparta_id] = s_obj

    with open("data.json", "w") as data:
        json.dump(sparta_api_dict, data)
    return "completed"
'''
