import spartan
import json

if __name__ == "__main__":

    spartan_dict = {}
    with open("recording_log.txt", 'a+') as log_file:
        log_file.write("Employee Management system log book created" + "\n")
        #log_file.close()

    while True:
        option = spartan.read_option()

        if option == "add":
            print("The user wants to add an Employee")
            spartan_object = spartan.create_spartan_object()

            spartan_id = spartan_object.get_emp_id()

            spartan_dict[spartan_id] = spartan_object
            print(spartan_dict.get(spartan_id))
            #with open("recording_log.txt", 'a+') as log_file:
                #log_file.write("New employee added" + "\n")


        elif option == "remove":
            print("The user wants to remove an Employee")
            spartan_id = spartan.read_spartan_id()
            del spartan_dict[spartan_id]
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("Employee removed" + "\n")

        elif option == "list":
            print("The user wants a list of the employees")
            spartan.print_all_spartans_data()
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("All spartans printed" + "\n")

        elif option == "update":
            print("The user wants to update the data of an employee")
            spartan_id = spartan.read_spartan_id()
            spartan.update_spartan(spartan_id)
            print(spartan_dict.get(spartan_id))
            with open("recording_log.txt", 'a+') as log_file:
                log_file.write("Spartan updated" + "\n")

        elif option == "total":
            print("The user wants the total number of employees")
            print(len(spartan_dict))

        elif option == "retrieve":
            print("The user wants to retrieve an Employee using ID")
            spartan_id = spartan.read_spartan_id()
            print(spartan_dict.get(spartan_id))

        elif option == "exit":
            print("Thanks, see you later")
            break

        elif option == "save":
            print("The data will be saved to json file")
            spartan.save_to_json()

        elif option == "load":
            print("the data will be loaded from a JSON file")
            spartan.load_from_json()

        else:
            print("Unknown option")






























