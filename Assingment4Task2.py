def write_to_file(myfile):
    user_input = input("Enter text to write to the file: ")
    with open('myfile.txt', 'w') as file:
        file.write(user_input + '\n')

def append_to_file(myfile):
    additional_input = input("Enter additional text to append to the file: ")
    with open(myfile, 'a') as file:
        file.write(additional_input + '\n')

def read_file(myfile):
    print("\nFinal content of the file:")
    with open('myfile.txt', 'r') as file:
        for line in file:
            print(line.strip())

# File name
file_name = "myfile.txt"

# Execute steps
write_to_file(file_name)
append_to_file(file_name)
read_file(file_name)
