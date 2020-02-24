#1.- iniciamos importando click
import click
#7.- para jalar a nuestro cliente de nuestro servicio solo lo importamos, entonces le decimos que 
# de el modulo clients del archivo services importamos la clase ClientServices y del mismo modulo clients 
# tambien importamos la clase Client 
from clients.services import ClientService
from clients.models import Client

#4.-Para que todas las funciones se conviertan en comandos es necesario utilizar decoradores, para 
#esto utilizamos el decorador click.group() y lo aplicamos a la funcion clients() para poder usar
# a ésta como otro decorador y aplicarlo a todas las funciones comando y hacerlas parte del grupo clients
@click.group()
#3.-definimos una funcion llamada clients para definir a cual grupo van a
# pertenecer todas las funcion de comandos
def clients():
    """Manages the clients lifecycle"""#esto es un DocString (documentacion de la opcion)
    pass

#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command()
#  que es parte del decorador group @clients.commmands()
@clients.command()
#6.- la funcion create(ctx,name,company,email,position): recibe varios parametros y esos
#  paramtros se los vamos a pedir al usuario por medio de click
@click.option('-n','--name', # aqui le decimos que tenemos una opcion que su ShortName sera n y su LongName sera name
                type=str, # de tipo string
                prompt=True, #le decimos que si no nos lo dan via el patron abriviado se lo pedimos al usuario
                help='The client name')#pequeña ayuda acerca de la propiedad
@click.option('-c','--company',
                type=str,
                prompt=True,
                help='The client company')
@click.option('-e','--email',
                type=str,
                prompt=True,
                help='The client email')
@click.option('-p','--position',
                type=str,
                prompt=True,
                help='The client position')
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion iniciando con create
# la cual recibe el contexto "ctx"  y los diferenctes campos que utilizamos 
def create(ctx,name,company,email,position):
    """Create a new client""" #esto es un DocString (documentacion de la opcion)
    #8.- ahora inicializamos un cliente (creamos una instancia de Client) con todos
    #  sus parametros excepto uid y dejamos que uuid4 lo genere por nosotros
    client=Client(name,company,email,position)
    #9.- aqui creamos una instancia de los setvicios de cliente y en el contexto le pasamos el nombre de la tabla
    client_service = ClientService(ctx.obj['clients_table'])
    #10.-ahora de la instancia de ClientServices recien creado ejecutamos su unico metodo ( hasta ahora) 
    # create_client y le pasamos la referencia de nuestro cliente y no s vamos a pv.py para declarar el nombre de
    # la tabla o archivo que vamos a utilizar
    client_service.create_client(client)

#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() (que todavia no creamos) @clients.commmands()
@clients.command()
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion
def list(ctx):
    """List all clients"""
    #11.- en este caso list no necesita parametro por lo tanto no usamos el metodo click.option(), entonces iniciamos
    #  creando una instancia de la clase ClientService
    client_service=ClientService(ctx.obj['clients_table'])
    #14.- con esto nos traemos nuestra lista de clientes del service_list
    clients_list=client_service.list_clients()
    #12.- ahora vamos a imprimir un encabezado
    click.echo('  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*'*100)
    #13.- ahora iteramos a lo largo de nuestros clientes
    for client in clients_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))

#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() (que todavia no creamos) @clients.commmands()
@clients.command()
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion
def update(ctx):
    """Update a client"""
    client_uid='1e17bee6-7276-4cee-8e4b-72246017decb'
    client_service=ClientService(ctx.obj['clients_table'])
    client_list=client_service.list_clients()
    client=[client for client in client_list if client['uid']==client_uid]
    if client:
        client=_update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client Updated')
    else:
        click.echo('Client not found')

def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')
    client.name = click.prompt('New name',type=str,default=client.name)
    client.company = click.prompt('New company',type=str,default=client.company)
    client.email = click.prompt('New email',type=str,default=client.email)
    client.position = click.prompt('New Position',type=str,default=client.position)
    return client


#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() (que todavia no creamos) @clients.commmands()
@clients.command()
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion
def delete(ctx,client_uid):
    """Delete a client"""
    pass

#aqui creamos un alias de clients y lo llamamos all
all=clients
