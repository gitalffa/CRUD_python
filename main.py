import os
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA =['name','company','email','position']
clients=[]

def _inicitialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader =csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        f.close()
        os.rename(tmp_table_name,CLIENT_TABLE)


def _exist_client(client):
    global clients
    
    total_clientes=range(len(clients))
    x=0
    for x in total_clientes:
        id=x
        if client['name'] in clients[x]['name']:
            return True,id
        else:
            continue

    id=x        
    return False,id


def create_client(client):
        clients.append(client)
    


def client_not_list():
    print('Client in not in clients list')


def list_clients():
    print('|id| |Name| |Company| |Email| |Position|')
    print('*'*50)
    for idx,client in enumerate(clients):
        
        print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'] 
        )
        )


def updated_client(client_name,updated_client_name,id):
    global clients
    clients[id]['name']=updated_client_name
    clients[id]['company']=_get_client_field('company')
    clients[id]['email']=_get_client_field('email')
    clients[id]['position']=_get_client_field('position')
    


def delete_client(id):
    global clients

    clients.pop(id)

  

def search_client(client):
    global clients
    
    total_clientes=range(len(clients))
    for x in total_clientes:
        if client['name'] in clients[x]['name']:
            id=x
            return True,x
        id=x
    return False,id

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
    _inicitialize_clients_from_storage()

    _print_welcome()
    command =input()
    command = command.upper();
    if command=='C':
    
        client={
            'name':_get_client_name()
        }
        TrueFalse,id=_exist_client(client)
        if TrueFalse==False:    
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
        client_name={
            'name':_get_client_name()
        }
        TrueFalse,id=_exist_client(client_name)
        if TrueFalse==True:
            delete_client(id)
        else:
            print('The client: {} is not in our client\'s list'.format(client_name['name']))

        list_clients()
    elif command=='S':

        client_name={
        	'name':_get_client_name()
        	}

        TrueFalse,id=search_client(client_name)
        
        if TrueFalse==True:
            print('The client is in the client\'s list')
            print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid=id,
            name=clients[id]['name'],
            company=clients[id]['company'],
            email=clients[id]['email'],
            position=clients[id]['position'] 
        	)
        	)
        else:
            print('The client: {} is not in our client\'s list'.format(client_name['name']))
            
    elif command =='U':
        client={
            'name': _get_client_name()
        }
        TrueFalse,id=_exist_client(client)
        if TrueFalse==False:
            client_not_list()
        else:
            updated_client_name=input('What is the updated client name ?')
            updated_client(client,updated_client_name,id)
            list_clients()
    else:
        print('Invalid command')


    _save_clients_to_storage()