# Ask user for their personal information

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

    # Print Invalid when age inputted is less than and equal to 0
    while True:
        age = int(input("Please input your age: "))
        if age <= 0:
            print("Invalid. Input the correct age")
        else:
             break
        
    email = input("Please input your email: ")
    while True:
        contact_number = int(input("Please input your Contact Number: "))
        if len(contact_number) == 11:
            break  
        else:
            print


with open("./Personal Information System.txt") as file_handle:
    file_handle.write()
    file_handle.write()
    file_handle.write()
    file_handle.write()
    file_handle.write()