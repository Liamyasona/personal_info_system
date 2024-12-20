full_name_search = input("Please enter the full name to access the information: ").strip()

# Read file
with open("./personal_information.txt", "r") as info_system:
    found = False
    lines = info_system.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == f"Full name: {full_name_search}":
            found = True
        # Print the information
            print("Here are the information found on the inputted name:")
            print(lines[i].strip()) # full_name
            print(lines[i + 1].strip()) # address
            print(lines[i + 2].strip()) # age
            print(lines[i + 3].strip()) # email
            print(lines[i + 4].strip()) # phone number
            break 

    if not found:
        print("There is no information found for that name.")
