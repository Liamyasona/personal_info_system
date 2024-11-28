full_name_search = input("Please enter the full name to access the information:")

# Try and except for error handling
try:
    # Read file
    with open("./Personal Information.txt", "r") as info_system:
        lines = info_system.readlines()
        for i in lines:
            if lines[i].strip() == f"Full Name: {full_name_search}":
            # Print the information
                print("Here are the information found on the inputted name:")
                print(lines[i].strip())
                print(lines[i + 1].strip())
                print(lines[i + 2].strip())
                print(lines[i + 3].strip())
                print(lines[i + 4].strip())


            
except FileNotFoundError:
    print("The name is not found in the list.")