
import time
import json
import sys

animation = "|-"

print("C A R - R E G I S T E R")
time.sleep(2)
print("L O A D I N G")
for i in range(90):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
time.sleep(2)

print("\nEnter a number from the menu")
time.sleep(1)
print("1. Register")
print("2. Log-In")

time.sleep(1)

number = int(input("Enter the number: \n"))


if number == 1:
    with open("User_data.json", "r") as file_check:
        data = json.loads(file_check.read())
        Username = data["Username"]
        Password = data["Password"]
        if Username != "" and Password != "":
            print("You already have an account please Log-In to it!")
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



if number == 2:
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
        print("Enter a number from the menu\n")
        print("1. Register a new car\n2. See the details of a car\n3. Edit data of a car\n4. Edit username\n5. Edit password\n6. Delete Account")

        number = int(input("Enter the number: \n"))
        #Registerin a new car FINISHED
        if number == 1:
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
        #Displaying the data of a car from the database FINISHED
        if number == 2:
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
        #Editing a cars details in the database DEVELOPMENT
        if number == 3:
            print("Enter the number from the list below, what you would like to change in the database of you car!")
            print("1. Edit Brand\n2. Edit Modle\n3. Edit Class\n3. Edit Year\n4. Edit Type\n5. Edit Color\n6. Edit Weight\n7. Edit Gear Box\n8. Edit Engine\n9. Edit Horsepower\n10. Edit Kilometer\n11. Edit Condition")
            open_file = input("Enter the platenumber of the car, please make sure you enter it correctly!\n")
            #file = f"{open_file}_data.json"

        #Editing username FINISHED
        if number == 4:
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
        #Editing password FINISHED
        if number == 5:
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
        #Deleting the account info FINISHED
        if number == 6:
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


    #If the entered data is not matching with the data in the database...
    else:
        time.sleep(2)
        print("Log-In information is not correct...")
        

    















#------------------------------------------------------------------------------------------------------
'''p1 = Car("Daniel", 0, 0)
p1.get_info()
p1.update_points_if_win()
p1.save_to_json("Daniel_data.json")
p1.get_info()
p1.update_name("Daniel_data.json", "Chris")
p1.update_points_if_win()
p1.update_points_if_win()
p1.save_to_json("Daniel_data.json")
p1.get_info()
p1.update_points_if_lose()
p1.save_to_json("Daniel_data.json")
p1.get_info()'''


