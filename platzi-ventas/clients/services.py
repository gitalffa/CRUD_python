import csv

from clients.models import Client
#1.- declaramos nuestra clase ClientService 
class ClientService:
    #2.- inicalizamos la clase, primer parametro self y los unico que
    # recibe esta clase es el nombre de la tabla donde guardaremos los datos
    def __init__(self,table_name):
        #3.- guardamos el nombre de la tabla en una variable de instancia
        self.table_name=table_name
    #4.- definimos el metodo create_client, que claro recibe como primer parametro
    # self y el objeto cliente
    def create_client(self,client):
        #5.- aqui escribimos en el archivo con open y en modo append ya que vamos a 
        # estar añadiendo registros en él
        with open(self.table_name,mode='a') as f:
            writer=csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    #6.- para listar a los clientes tenemos que declarar un nuevo metodo que llamaremos
    #  list_cleints y solo recibe el argumento self
    def list_clients(self):
        #7.- abrimos el archivo en modo lectura "r"
        with open(self.table_name,mode="r") as f:
            #8.- creamos un readers y le pasamos la referencia del schema del cliente
            reader=csv.DictReader(f,fieldnames=Client.schema())
            #9.- regresamos el reader utilizando la funcion gobal list()
            return list(reader)