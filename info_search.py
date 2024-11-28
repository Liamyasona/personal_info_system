full_name_search = input("Please enter the full name to access the information:")

try:
    with open("./Personal Information.txt", "r") as info_system:
        lines = info_system.readlines()
        for line in lines: 
            
except FileNotFoundError:
    print("The name is not found in the list.")