import json


filename = "contact.json"
while True:
    print("1.Add contact\n2.Modify contact\n3.Delete contact\n4.Print all contact\n5.Quit")
    user = input()
    if user == "1":
        try:
            with open(filename,"r") as file:
                my_dict = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            my_dict = {}

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        new_my_dict = {
            "Name":name,
            "Phone":phone,
            "Email":email
        }
        my_dict[name.lower()] = new_my_dict
        with open(filename, "w") as file:
            json.dump(my_dict,file)
        print("Successful!")
    if user == "2":
        with open(filename, "r") as file:
            user_data = json.load(file)
            name = input("Enter user name: ")
            if name.lower() in user_data:
                data = user_data[name]
                print(data)
                new_name = input("Name: ")
                new_phone = input("Phone: ")
                new_email = input("Email: ")
                data["Name"] = new_name
                data["Phone"] = new_phone
                data["Email"] = new_email
                user_data[name.lower()] = data
                with open(filename, "w") as f:
                    json.dump(user_data,f)
                print(user_data[name])
    if user == "3":
        with open(filename, "r") as file:
            user_data = json.load(file)
            name = input("Enter user name: ")
            if name.lower() in user_data:
                del user_data[name.lower()]
                with open(filename, "w") as f:
                    json.dump(user_data, f)
                print("Successful")
    if user == "4":
        with open(filename, "r") as file:
            print(file.read())
    if user == "5":
        break
