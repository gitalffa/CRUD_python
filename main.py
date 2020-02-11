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
    
        clients.append(client)
    


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

  

def search_client(client):
    global clients
    
    total_clientes=range(len(clients)-1)
    for x in total_clientes:
        regreso=clients[x].get(client['name'],-1)
        if regreso!=-1:
        	continue
    

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
            'name':_get_client_name()
        }
        if _exist_client(client)==False:    
                client['company']=_get_client_field('company')
                client['email']=_get_client_field('email')
                client['position']=_get_client_field('position')
                create_client(client)
        else:
                print('Client already in the client\'s list')

        list_clients()
    elif command=='L':
        list_clients()
    elif command=='D':
        client_name=_get_client_name()
        delete_client(client_name)
        list_clients()
    elif command=='S':

        client_name={
        	'name':_get_client_name()
        	}

        id=search_client(client_name)
    
        if id<0:
        	print('The client: {} is not in our client\'s list'.format(client_name['name']))
        else:
            print('The client is in the client\'s list')
            print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid=id,
            name=clients[id]['name'],
            company=clients[id]['company'],
            email=clients[id]['email'],
            position=clients[id]['position'] 
        	)
        	)
            
    elif command =='U':
        client={
            'name': _get_client_name()
        }
        if _exist_client(client)==False:
            client_not_list()
        else:
            updated_client_name=input('What is the updated client name ?')
            updated_client(client_name,updated_client_name)
            list_clients()
    else:
        print('Invalid command')