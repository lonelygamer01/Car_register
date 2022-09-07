import json




plate_number = input("Enter the platenumber of the car please:\n")
def get_info(filename):
    with open(filename, "r") as file_info:
        data = json.loads(file_info.read())
    print(
        "Brand: {}".format(data["Brand"]),
        "Model: {}".format(data["Model"]),
        "Class: {}".format(data["Class"]),
        "Plate number: {}".format(data["Plate_number"]),
    )
plate_number_to_json = "{}_data.json".format(plate_number)

get_info(plate_number_to_json)    