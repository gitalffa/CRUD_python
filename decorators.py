PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password=input('Cual es tu contraseña ? ')
        if password==PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta.')
    return wrapper


@password_required
def needs_password():
    print('La contraseña es correcta')


if __name__ == '__main__':
    needs_password()