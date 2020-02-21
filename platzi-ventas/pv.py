import click # 1-. lo primero que hacemos es importar click
#5.- regresamos a pv.py y vamos a importar los comandos que declaramos en el modulo clients, esto lo hacemos
#importando de clients los comandos y que se llamen cleints_commands
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

#3.- para decirle a click cual es el punto de entrada usamos @click.group
@click.group()
#4.- click tiene un segundo decorador llamdo @click_context y este nos va a dar un obj
#contexto el cual le pasa como  parametro a la funcion cli y pasamos a nuestro archivo clients/commands.py
@click.pass_context
#2.- despues definimos una funcion llamada cli que sera nuestro punto de entrada
def cli(ctx):
    """An application to manage clients, inventory, sales and produce reports."""
    #2.5- inicializamos este objeto contexto como un diccionario vacio
    ctx.obj = {}
    ctx.obj['clients_table']=CLIENTS_TABLE
    

#6.- ahora registramos los comandos que importamos de commands.py en la funcion de entrada cli con su metodo
#  add_command pasandole como parametro la importacion que hicimos en clients_commands y utilizamos el alias
#  all para hacer referencia a todos los comandos de clients
cli.add_command(clients_commands.all)
