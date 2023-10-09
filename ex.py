import csv

Student_info = {}


def file_read():
    try:
        with open('Student_info.csv', 'r') as myfile:
            redar = csv.DictReader(myfile)
            for row in redar:
                name = row['name']
                age = row['age']
                roll = row['roll']
                Student_info[roll] = {'Name: ': name, 'Age: ': age, 'Roll: ': roll}
                print(name)
                return Student_info
    except:
        return {}


def save_to_csv():
    with open('data.csv', 'a') as csvfile:
        fieldnames = ['Name', 'Age', 'Roll']
        write = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write.writeheader()
        for roll, info in Student_info.items():
            write.writerow(
                {'Roll': roll, 'Name': info['name'], 'Age': info['age']}
            )


def show_student():
    if not Student_info:
        print('student are not listed')
    else:
        print('Name \t\tAge \t\t Roll')
        for roll, info in Student_info.items():
            print('{} \t\t{} \t\t{} \t\t'.format(info['name'], info['age'], roll))


def main():
    Student_info = file_read()
    while True:
        choise = int(input('1.Add\n'
                           '2.Remove\n'
                           '3.edit\n'
                           '4.Show'
                           '5.exit\n'
                           'input the number (1-4)'))
        if choise == 1:
            name = input('Student name here:')
            roll = input('Student Roll: ')
            age = input('Student age: ')
            Student_info[roll] = {'Name': name, 'Age': age}
            save_to_csv()
            print('add sucessfully!')
        elif choise == 2:
            remove_roll = input('Student Roll: ')
            if remove_roll in Student_info:
                ask = input('Do you want remove this student Y/N')
                if ask == 'Y' or ask == 'y':
                    Student_info.pop(remove_roll)
                    print('Remove sucessfully!')
                else:
                    print('Do not edit any data from csv')
            else:
                print(f'This Student are not exist you input {remove_roll}')
        elif choise == 3:
            ed_roll = input('Student Roll: ')
            if ed_roll in Student_info:
                ed_name = input('Student name: ')
                ed_age = input('Student Age: ')
                Student_info[ed_roll] = {'Name': ed_name, 'Age': ed_age}
                save_to_csv()
        elif choise == 4:
            print(Student_info)
            show_student()
        elif choise == 5:
            exit = input('Do you want to close this program Y/N')
            if exit == 'Y' or exit == 'y':
                main()
            else:
                print("Thank's for using My program Made by mahadi ")
                break
        else:
            print('Input a real number above (1-4)')


if __name__ == '__main__':
    main()
