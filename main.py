import sys
clients=[
    {
        'name':'pablo',
        'company':'Google',
        'email':'pablo@google.com',
        'position':'Software Ingenier'
    },
    {
        'name':'Ricardo',
        'company':'Facebook',
        'email':'ricardo@facebook.com',
        'position':'Data engineer'
    }

]


def _exist_client(client):
    global clients
    
    total_clientes=range(len(clients)-1)
    for x in total_clientes:
        if client['name'] not in clients[x]['name']:
            return False


def create_client(client):
    if _exist_client(client)==False:
        clients.append(client)
    else:
        print('Client already in the client\'s list')


def client_not_list():
    print('Client in not in clients list')


def list_clients():
    for idx,client in enumerate(clients):
        print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'] 
        )
        )


def updated_client(client_name,updated_client_name):
    global clients

    if client_name in clients:
        index=clients.index(client_name)
        clients[index]=updated_client_name
    else:
        client_not_list()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        client_not_list()

    
def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True




def _print_welcome():
    print('Welcome To Platzi Ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('(C)reate client')
    print('(L)ist')
    print('(U)pdate client')
    print('(D)elete client')
    print('(S)earch client')

def _get_client_field(field_name):
    field =None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field


def _get_client_name():
    client_name=None

    while not client_name:
        client_name=input('What is the Client name?')
        if client_name=='exit':
            client_name=None
            break
    
    if not client_name:
            sys.exit()

    return client_name



if __name__=='__main__':
    _print_welcome()
    
    command =input()
    command = command.upper();
    if command=='C':
        client={
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position')
        }
        create_client(client)
        list_clients()
    elif command=='L':
        list_clients()
    elif command=='D':
        client_name=_get_client_name()
        delete_client(client_name)
        list_clients()
    elif command=='S':
        client_name=_get_client_name()
        found=search_client(client_name)
    
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command =='U':
        client_name=_get_client_name()
        updated_client_name=input('What is the updated client name ?')
        updated_client(client_name,updated_client_name)
        list_clients()
    else:
        print('Invalid command')