full_name_search = input("Please enter the full name to access the information:")

with open("./Personal Information.txt", "r") as info_system:
    lines = info_system.readlines()
    for line in lines: 
        