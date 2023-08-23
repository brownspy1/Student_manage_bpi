credentials = {'bpi': '123'}


def login():
    user = input('Username: ')
    password = input('Password: ')  # Use getpass to input password securely
    if credentials.get(user) == password:
        return True
    else:
        print('Wrong username or password')
        return False
