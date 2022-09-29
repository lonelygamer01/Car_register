
from msilib.schema import Condition
import time
import json
import sys


#making a class for the app so the user can navigate on the pages...
class Console_App:
    def anyad():
        print("ANYÁD")
    #define the loading page
    def loading_page():
        animation = "|-"

        print("C A R - R E G I S T E R")
        time.sleep(2)
        print("L O A D I N G")
        for i in range(90):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        time.sleep(2)
    #define the login and register options 
    def starting_page():
        print("\nEnter a number from the menu")
        time.sleep(1)
        print("0. Print ANYÁD")
        print("1. Register")
        print("2. Log-In")
    #define the register module
    def register():
        with open("User_data.json", "r") as file_check:
            data = json.loads(file_check.read())
            Username = data["Username"]
            Password = data["Password"]
            if Username != "" and Password != "":
                print("You already have an account please Log-In to it!")
                Console_App.starting_page()
            else:    


                username = input("Enter a username: \n")
                password = input("Enter a password: \n")

                user_data = {"Username" : username, "Password" : password}
                with open("User_data.json", "w") as file_reg:
                    file_reg.write(json.dumps(user_data, indent=3))
                    file_reg.close()
                
                time.sleep(2)
                print('Registration complete') 
            file_check.close()
    #define the login module
    def log_in():
        username = input("Enter the username: \n")
        password = input("Enter the password: \n")

        with open("User_data.json", "r") as file_log:
            data = json.loads(file_log.read())
            Username = data["Username"]
            Password = data["Password"]
        #If the username and the password which entered below is matching with the data in the database...
        if username == Username and password == Password:
            time.sleep(2)
            print("Log-In was successful...\n")
            file_log.close()
            
        #If the entered data is not matching with the data in the database...    
        else:
            time.sleep(2)
            print("Log-In information is not correct...")
            Console_App.log_in()        
    #define the car registration method
    def reg_new_car():
        brand = input("Brand: ")
        model = input("Model: ")
        Class = input("Class: ")
        year = input("Year: ")
        type = input("Type: ")
        color = input("Color: ")
        weight = input("Weight: ")
        gear_box = input("Gearbox type: ")
        engine = input("Engine type: ")
        hp = input("Horsepower: ")
        plate_number = input("Platenumber: ")
        km = input("Km: ")
        condition = input("Condition: ")
        time.sleep(2)
        print("\nProcessing...")

        file_name = f"{plate_number}_data.json"

        def save_to_json(filename):
            car_data = {"Brand":brand, "Model":model, "Class":Class, "Year":year, "Type": type, "Color":color, "Weight":weight, "Gearbox":gear_box, "Engine":engine, "Hp":hp, "Plate_number": plate_number, "Km":km, "Condition":condition}
            with open(filename, "w") as file_save:
                file_save.write(json.dumps(car_data, indent=3))
            file_save.close()
        save_to_json(file_name)
        time.sleep(2)
        print("New car has been added to the database")
    #define data apperance
    def display_data():
        plate_number = input("Enter the platenumber of the car please:\n")
        def get_info(filename):
            with open(filename, "r") as file_info:
                data = json.loads(file_info.read())
            print(
                "Brand: {}".format(data["Brand"]),
                "Model: {}".format(data["Model"]),
                "Class: {}".format(data["Class"]),
                "Year: {}".format(data["Year"]),
                "Type: {}".format(data["Type"]),
                "Color: {}".format(data["Color"]),
                "Weight: {}".format(data["Weight"]),
                "Gearbox: {}".format(data["Gearbox"]),
                "Engine: {}".format(data["Engine"]),
                "Hp: {}".format(data["Hp"]),
                "Plate number: {}".format(data["Plate_number"]),
                "Km: {}".format(data["Km"]),
                "Condition: {}".format(data["Condition"]),

            )
        plate_number_to_json = "{}_data.json".format(plate_number)

        get_info(plate_number_to_json)
    #define editing car data methods
    def edit_details():
        print("Enter the number from the list below, what you would like to change in the database of you car!")
        print("1. Edit Brand\n2. Edit Model\n3. Edit Class\n4. Edit Year\n5. Edit Type\n6. Edit Color\n7. Edit Weight\n8. Edit Gear Box\n9. Edit Engine\n10. Edit Horsepower\n11. Edit Kilometer\n12. Edit Condition")
        #Asking for an imput from the user
        select_number3 = int(input("Enter the number: \n"))
        
        if select_number3 == 1:
            print("You are about to change the brand of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                brand = input("Enter the new Brand: ")

                json_object["Brand"] = brand
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")

        elif select_number3 == 2:
            print("You are about to change the model of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                model = input("Enter the new Model: ")

                json_object["Model"] = model
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            

        elif select_number3 == 3:
            print("You are about to change the class of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                Class = input("Enter the new Class: ")

                json_object["Class"] = Class
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            
        elif select_number3 == 4:
            print("You are about to change the year of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                year = input("Enter the new Year: ")

                json_object["Year"] = year
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            
        elif select_number3 == 5:
            print("You are about to change the type of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                type = input("Enter the new type: ")

                json_object["Type"] = type
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
          
        elif select_number3 == 6:
            print("You are about to change the color of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                color = input("Enter the new Color: ")

                json_object["Color"] = color
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
           
        elif select_number3 == 7:
            print("You are about to change the Weight of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                weight = input("Enter the new Weight: ")

                json_object["Weight"] = weight
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            

        elif select_number3 == 8:
            print("You are about to change the gearbox type of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                gearbox = input("Enter the new Gearbox type: ")

                json_object["Gearbox"] = gearbox
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            

        elif select_number3 == 9:
            print("You are about to change the engine type of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                engine = input("Enter the new Engine tpye: ")

                json_object["Engine"] = engine
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            
        elif select_number3 == 10:
            print("You are about to change the horsepower of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                horsepower = input("Enter the new Horsepower: ")

                json_object["Hp"] = horsepower
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
            
        elif select_number3 == 11:
            print("You are about to change the kilometer of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                km = input("Enter the new Kilometers: ")

                json_object["Km"] = km
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
           
        elif select_number3 == 12:
            print("You are about to change the condition of the car")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")

            try: 
                file = open(f"{open_file}_data.json", "r")
                json_object = json.load(file)
                file.close()
                condition = input("Enter the new Condition: ")

                json_object["Condition"] = condition
                file = open(f"{open_file}_data.json", "w")
                json.dump(json_object, file, indent=2)
                file.close()
                print("Updating...")
                time.sleep(2)
                print("Data updated successfully...")

            except:
                print("Faield to reach the file, no such a file...")
           
        else:
            print("Please enter a valid number FROM THE LIST ABOVE")    
    #define editing username method
    def edit_username():
        old_username = input("Enter the current username:\n")
        with open ("User_data.json", "r") as file_edit1:
            data = json.loads(file_edit1.read())
            Username = data["Username"]

            if old_username == Username:
                new_username = input("Enter the new username here please:\n")
                with open("User_data.json", "r") as file_edit2:
                    data_for_edit = json.load(file_edit2)
                data_for_edit["Username"] = new_username
                with open("User_data.json", "w") as file_edit2:
                    json.dump(data_for_edit, file_edit2, indent=3)    
                time.sleep(2)
                print("Editing was successful...")    
                file_edit2.close()

            if old_username != Username:
                print('The username isnt correct...')
                
            file_edit1.close()
    #define editing password method
    def edit_password():
        old_password = input("Enter the current password:\n")
        with open ("User_data.json", "r") as file_edit1:
            data = json.loads(file_edit1.read())
            Password = data["Password"]

            if old_password == Password:
                new_password = input("Enter the new password here please:\n")
                with open("User_data.json", "r") as file_edit2:
                    data_for_edit = json.load(file_edit2)
                data_for_edit["Password"] = new_password
                with open("User_data.json", "w") as file_edit2:
                    json.dump(data_for_edit, file_edit2, indent=3)    
                time.sleep(2)
                print("Editing was successful...")    
                file_edit2.close()
                
            if old_password != Password:
                print('The password isnt correct...')
                
            file_edit1.close()
    #define deleting user method
    def delete_user():
        username_delete = input("Enter the username:\n")
        password_delete = input("Enter the password:\n")
        with open("User_data.json", "r") as file_delete1:
            data = json.loads(file_delete1.read())
            Username = data["Username"]
            Password = data["Password"]

            if username_delete == Username and password_delete == Password:
                time.sleep(2)
                print("Log-In was successful")
                file_delete1.close()
                time.sleep(1)
                ensure = input("Press y and hit Enter to continue deleting details...\n")
                if ensure == "y":
                    data_delete = {"Username": "", "Password": ""}
                    with open("User_data.json", "w") as file_delete2:
                        file_delete2.write(json.dumps(data_delete, indent=3))
                        file_delete2.close()
                    time.sleep(2)
                    print("Account successfully deleted...")


Console_App.loading_page()
Console_App.starting_page()

time.sleep(1)

select_number1 = int(input("Enter the number: \n"))

if select_number1 == 0:
    Console_App.anyad()


if select_number1 == 1:
    Console_App.register()

if select_number1 == 2:

    Console_App.log_in()
    while True :
        print("Enter a number from the menu\n")
        print("1. Register a new car\n2. See the details of a car\n3. Edit data of a car\n4. Edit username\n5. Edit password\n6. Delete Account")

        select_number2 = int(input("Enter the number: \n"))
        #Registerin a new car FINISHED
        if select_number2 == 1:
            Console_App.reg_new_car()
        #Displaying the data of a car from the database FINISHED
        if select_number2 == 2:
            Console_App.display_data()
            
        #Editing a cars details in the database DEVELOPMENT
        if select_number2 == 3:
            Console_App.edit_details()
            

            #file = f"{open_file}_data.json"

        #Editing username FINISHED
        if select_number2 == 4:
            Console_App.edit_username()
            
        #Editing password FINISHED
        if select_number2 == 5:
            Console_App.edit_password()
            
        #Deleting the account info FINISHED
        if select_number2 == 6:
            Console_App.delete_user()
