
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



def read_option():
    while True:
        user_option = input("Spartan Management options: add: Add Spartan, remove: Remove Spartan, list: List Spartan ,update: Update Spartan Data, exit: Exit the app, total: Total number of Spartans, retrieve: Retrieve Spartan using ID: load: Load from json, save: Save to json")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "update", "list", "exit", "total", "retrieve", ]:
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

    spartan = Spartan(spartan_id, spartan_firstname, spartan_lastname, spartan_birthd,
                  spartan_birthm, spartan_birthy, spartan_course, spartan_stream)

    return spartan


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
        spartan_id_dict[spartan_id].set_course(new_course)
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
        spartan_dict[spartan_id_id].set_is_graduated(new_stream)


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


def save_to_jason():
    temp_dict_of_dict = {}
    for spartan_id in spartan_dict:
        spartan_object = spartan_dict[spartan_id]
        spartan_dict_json = spartan_object.__dict__
        temp_dict_of_dict[spartan_id] = spartan_dict_json

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)


def load_to_jason():
    global spartan_dict
    temp_dict_of_dict = {}
    try:
        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)
    except:
        print("The file data1.json doesn't exist")
    print(temp_dict_of_dict)
    for employee_id_key in temp_dict_of_dict:
        employee_id = temp_dict_of_dict[employee_id_key]['emp_id']
    employee_object = Employee[create_employee_ob()]

#id, firstname, lastname, position, birth_day, birth_month, birth_year, graduated



