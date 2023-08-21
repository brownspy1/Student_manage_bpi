import csv
from bpi import login


# Function to read data from CSV
def read_from_csv():
    student_list = {}
    try:
        with open('student_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                department = row['Department']
                roll = row['Roll']
                session = row['Session']
                student_list[name] = {'Department': department, 'Roll': roll, 'Session': session}
        return student_list
    except FileNotFoundError:
        return {}  # Return empty dictionary if the file doesn't exist


# Function to save data to CSV
def save_to_csv(student_list):
    with open('student_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Department', 'Roll', 'Session']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for name, info in student_list.items():
            writer.writerow(
                {'Name': name, 'Department': info['Department'], 'Roll': info['Roll'], 'Session': info['Session']})


def show_student(student_list):
    if not student_list:
        print('No students are listed')
    else:
        print('Name\t\tDepartment\t\tRoll\t\tSession')
        for studentn, info in student_list.items():
            print("{}\t\t{}\t\t{}\t\t{}".format(studentn, info['Department'], info['Roll'], info['Session']))


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
                               'Enter your choice It Should Be Number 1-6: '))

            if choice == 1:
                name = input('Input Student Name:')
                dep = input('Input Student Department:')
                roll = input('Input Student Roll:')
                session = input('Input Student Session:')
                student_list[name] = {'Department': dep, 'Roll': roll, 'Session': session}
                save_to_csv(student_list)

            elif choice == 2:
                if not student_list:
                    print('Student info is empty.')
                else:
                    show_student(student_list)

            elif choice == 3:
                edit_name = input("Which student's data:")
                if edit_name in student_list:
                    dep = input('Input Student Department:')
                    roll = input('Input Student Roll:')
                    session = input('Input Student Session:')
                    student_list[edit_name] = {'Department': dep, 'Roll': roll, 'Session': session}
                    save_to_csv(student_list)
                else:
                    print('Incorrect Student Name!')

            elif choice == 4:
                rmst = input("Which student's data:")
                if rmst in student_list:
                    ask = input("Do you want to Remove This Student Y/N?")
                    if ask == 'Y' or ask == 'y':
                        student_list.pop(rmst)
                        print('Successfully removed the student!')
                        save_to_csv(student_list)
                    else:
                        print('Incorrect Input!')
                else:
                    print('Incorrect Student Name!')

            elif choice == 5:
                src = input('Search Student:')
                if src in student_list:
                    print(student_list[src])
                else:
                    print('Student Not Found')

            elif choice == 6:
                con = input('')
                break
            else:
                print('Invalid choice. Please choose a number between 1 and 6.')
    else:
        print('Sorry, you do not have access to this program!')


if __name__ == "__main__":
    main()
