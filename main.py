import csv
from pyfiglet import *
import os


# Function to read data from CSV
def read_from_csv():
    student_list = {}
    try:
        with open('student_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                roll = row['Roll']
                department = row['Department']
                name = row['Name']
                session = row['Session']
                student_list[roll] = {'Name': name, 'Department': department, 'Session': session}
        return student_list
    except FileNotFoundError:
        return {}  # Return empty dictionary if the file doesn't exist


# funcation for auth
credentials = {'bpi': '123'}


def login():
    user = input('Username: ')
    password = input('Password: ')  # Use getpass to input password securely
    if credentials.get(user) == password:
        return True
    else:
        print('Wrong username or password')
        return False


# Function to save data to CSV
def save_to_csv(student_list):
    with open('student_data.csv', 'w', newline='') as file:  # Use 'w' mode to overwrite the file
        fieldnames = ['Roll', 'Department', 'Name', 'Session']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for roll, info in student_list.items():
            writer.writerow(
                {'Roll': roll, 'Name': info['Name'], 'Department': info['Department'], 'Session': info['Session']})


def show_student(student_list):
    if not student_list:
        print('No students are listed')
    else:
        print('Name\t\tRoll\t\tDepartment\t\tSession')
        for roll, info in student_list.items():
            print("{}\t\t{}\t\t{}\t\t\t{}".format(info['Name'], roll, info['Department'], info['Session']))


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main program
def main():
    student_list = read_from_csv()

    if login():
        while True:
            print(''' \t\to--o  o--o  o-O-o
 \t\t|   | |   |   |  
 \t\tO--o  O--o    |  
 \t\t|   | |       |  
 \t\to--o  o     o-O-o
Barisal Polytechnic Institute                

            ''')
            choice = int(input('1. Add Student\n'
                               '2. Show Student\n'
                               '3. Edit Student\n'
                               '4. Remove Student\n'
                               '5. Search Student\n'
                               '6. Exit\n'
                               'Enter your choice (1-6): '))

            if choice == 1:
                name = input('Input Student Name:')
                dep = input('Input Student Department:')
                roll = input('Input Student Roll:')
                session = input('Input Student Session:')
                student_list[roll] = {'Name': name, 'Department': dep, 'Session': session}
                save_to_csv(student_list)

            elif choice == 2:
                show_student(student_list)

            elif choice == 3:
                edit_roll = input("Which student's Roll to edit:")
                if edit_roll in student_list:
                    name = input('Input Student Name:')
                    dep = input('Input Student Department:')
                    session = input('Input Student Session:')
                    student_list[edit_roll] = {'Name': name, 'Department': dep, 'Session': session}
                    save_to_csv(student_list)
                else:
                    print('Student Roll not found!')

            elif choice == 4:
                remove_roll = input("Which student's Roll to remove:")
                if remove_roll in student_list:
                    ask = input("Do you want to remove this student? (Y/N): ")
                    if ask.lower() == 'y':
                        student_list.pop(remove_roll)
                        print('Successfully removed the student!')
                        save_to_csv(student_list)
                    else:
                        print('No changes were made.')
                else:
                    print('Student Roll not found!')

            elif choice == 5:
                search_roll = input('Enter Student Roll to search:')
                if search_roll in student_list:
                    print(student_list[search_roll])
                else:
                    print('Student not found.')

            elif choice == 6:
                ask = input("Do you Really  Wan't to exit from this program Y/N: ")
                if ask == 'Y' or ask == 'y':
                    main()
                else:
                    print('Thank for using this program!')
                    banner = pyfiglet.figlet_format("\tExit")
                    print(banner)
                    break
            else:
                clear_terminal()
                print('Invalid choice. Please choose a number between 1 and 6.')
    else:
        print('Sorry, you do not have access to this program!')


if __name__ == "__main__":
    main()
