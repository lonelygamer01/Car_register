from ast import Pass
import time
import json
import sys

animation = "|-"

print("C A R - R E G I S T E R")
time.sleep(2)
print("L O A D I N G")
for i in range(50):
    time.sleep(0.2)
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

    if username == Username and password == Password:
        time.sleep(2)
        print("Log-In was successful...\n")
        file_log.close()
        print("Enter a number from the menu\n")
        print("1. Register a new car\n2. See the details of a car\n3. Edit data of a car\n4. Edit username\n5. Edit password\n6. Delete Account")

        number = int(input("Enter the number: \n"))

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

            class Car:
                def __init__(self, brand, model, Class, year, type, color, weight, gearbox, engine, hp, plate_number, km, condition):
                    self.brand = brand
                    self.model = model
                    self.Class = Class
                    self.year = year
                    self.type = type
                    self.color = color
                    self.weight = weight
                    self.gearbox = gearbox
                    self.engine = engine
                    self.hp = hp
                    self.plate_number = plate_number
                    self.km = km
                    self.condition = condition

                def get_info(self):
                    print("Model: {}, Class: {}, Year: {}, Type: {}, Color: {}, Weight: {}, Gearbox: {}, Engine: {}, Hp: {}, Plate number: {}, Km: {}, Condition: {}".format(self.model, self.Class, self.year, self.type, self.color, self.weight, self.gearbox,self.engine,self.hp, self.plate_number, self.km, self.condition))

                def update_model(self, file, model):
                    a_file = open(file, "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    self.model = model
                    json_object["Model"] = self.model
                    a_file = open(file, "w")
                    json.dump(json_object, a_file, indent=2)
                    a_file.close()

                def update_color(self, file, color):
                    a_file = open(file, "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    self.color = color
                    json_object["Color"] = self.color
                    a_file = open(file, "w")
                    json.dump(json_object, a_file, indent=2)
                    a_file.close()

                def update_km(self, file, km):
                    a_file = open(file, "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    self.km = km
                    json_object["Km"] = self.km
                    a_file = open(file, "w")
                    json.dump(json_object, a_file, indent=2)
                    a_file.close()        

                def save_to_json(self,filename):
                    car_data = {"Brand":self.brand, "Model":self.model, "Class":self.Class, "Year":self.year, "Type": self.type, "Color":self.color, "Weight":self.weight, "Gearbox":self.gearbox, "Engine":self.engine, "Hp":self.hp, "Plate_number": self.plate_number, "Km":self.km, "Condition":self.condition}    
                    with open(filename, "w") as file:
                        file.write(json.dumps(car_data, indent=3))

                def load_from_json(self, filename):
                    with open(filename, "r") as file:
                        data = json.loads(file.read())

                    self.name = data["name"]
                    self.point = data["point"]
                    self.current_streak = data["streak"]

                

            c1 = Car(brand, model, Class, year, type, color, weight, gear_box, engine, hp, plate_number, km, condition)
            c1.save_to_json("{}_data.json".format(c1.plate_number))
            c1.get_info()

            update_model = input("Do you want to update the model's name? (y/n): ")
            if update_model == "y":
                file_name = input("Enter the filename you want to update: ")
                model_name = input("Enter the new model name: ")
                c1.update_model(file_name, model_name)
                c1.save_to_json("{}_data.json".format(c1.plate_number))
                print('Update was successful...')
                print('New model name is: {}'.format(c1.model))
            else:
                pass

            update_color = input("Do you want to update the model's color? (y/n): ")
            if update_color == "y":
                file_name = input("Enter the filename you want to update: ")
                model_color = input("Enter the new color: ")
                c1.update_color(file_name, model_color)
                c1.save_to_json("{}_data.json".format(c1.plate_number))
                print('Update was successful...')
                print('New color is: {}'.format(c1.color))
            else:
                pass

            update_km = input("Do you want to update the model's km? (y/n): ")
            if update_km == "y":
                file_name = input("Enter the filename you want to update: ")
                model_km = input("Enter the new km: ")
                c1.update_km(file_name, model_km)
                c1.save_to_json("{}_data.json".format(c1.plate_number))
                print('Update was successful...')
                print('New km is: {}'.format(c1.km))
            else:
                pass

        if number == 2:
            pass
        if number == 3:
            pass
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

        if number == 6:
            pass

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


