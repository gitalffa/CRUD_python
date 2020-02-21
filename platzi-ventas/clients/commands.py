#1.- iniciamos importando click
import click

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

#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() que es parte del decorador group @clients.commmands()
@clients.command()
@click.option('-n','--name',
                type=str,
                prompt=True,
                help='The client name')
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
    client=Client(name,company,email,position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)

#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() (que todavia no creamos) @clients.commmands()
@clients.command()
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion
def list(ctx):
    """List all clients"""
    pass


#5.-ahora usamos el decorador que acabamos de creas y lo llamamos con su metodo command() (que todavia no creamos) @clients.commmands()
@clients.command()
#6.- y le pasmos tambien el contexto
@click.pass_context
#2.- definimos nuestros comandos basico de la aplicacion
def update(ctx,client_uid):
    """Update a client"""
    pass


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
