
#THIS FILE IS ONLY FOR TESTING DIFFERENT PARTS OF THE PROGRAM WITHOUT RUNNING THE WHOLE CODE... I KKNOW SMART :))


import json

class Console_App:
    
    def login_page(self):
        print("Nem")
    def register_page(self):
        print("Igen")
        

        

            









'''         brand = input("Brand: ")
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
                pass'''