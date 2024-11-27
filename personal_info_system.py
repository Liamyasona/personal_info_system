# Ask user for their personal information
with open("./Personal Information System.txt", "a") as info_system:
     
    # Loop to keep asking user for input
    while True:
        print("Welcome! Please input your personal information.")

        # Ask user for full name and print invalid when user inputs numbers
        while True:
            full_name = input("Please input your full name: ")
            if full_name.isalpha() or " " in full_name:  
                    break  # Valid name
            else:
                print("Invalid Name. Input your correct name.")

        address = input("Please input your address: ")

        # Ask user for age and print invalid when age inputted is less than and equal to 0
        while True:
            age = int(input("Please input your age: "))
            if age <= 0:
                print("Invalid. Input the correct age")
            else:
                break
            
        # Ask user for email
        email = input("Please input your email: ")

        # Ask user for contact number and print invalid when number inputted is not in 11 digits
        while True:
            contact_number = int(input("Please input your Contact Number: "))
            if contact_number == 11:
                break  
            else:
                print("Invalid Contact number. Please input a valid number")

    # Every user input will be appended to the file

        info_system.write(f"Full name: {full_name}\n")
        info_system.write()
        info_system.write()
        info_system.write()
        info_system.write()