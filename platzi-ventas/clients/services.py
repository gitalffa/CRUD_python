#import csv
#import os

from common.services import PVService
from clients.models import Client
#1.- declaramos nuestra clase ClientService 
class ClientService(PVService):
    #2.- inicalizamos la clase, primer parametro self y los unico que
    # recibe esta clase es el nombre de la tabla donde guardaremos los datos
    def __init__(self,table_name):
        super().__init__(table_name)
        #3.- guardamos el nombre de la tabla en una variable de instancia
        #self.table_name=table_name
    #4.- definimos el metodo create_client, que claro recibe como primer parametro
    # self y el objeto cliente
    def create_client(self,client):
        #5.- aqui escribimos en el archivo con open y en modo append ya que vamos a 
        # estar añadiendo registros en él
        """ with open(self.table_name,mode='a') as f:
            writer=csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerow(client.to_dict())
 """
        self.create(client.to_dict(),Client.schema())
    #6.- para listar a los clientes tenemos que declarar un nuevo metodo que llamaremos
    #  list_cleints y solo recibe el argumento self
    def list_clients(self):
        return self.list(Client.schema())
        #7.- abrimos el archivo en modo lectura "r"
        #with open(self.table_name,mode="r") as f:
            #8.- creamos un readers y le pasamos la referencia del schema del cliente
            #reader=csv.DictReader(f,fieldnames=Client.schema())
            #9.- regresamos el reader utilizando la funcion gobal list()
            #return list(reader)
#10.- vamos a añadir un nuevo metodo para la actualizacion del cliente

    def update_client(self,updated_client):
        self.update(updated_client.to_dict(),Client.schema())
        #11.- lo primero que tenemos que hacer es obtener una lista de los clientes,
        #  y ya tenemos una funcion para eso list_clients(), para esto declaramos una 
        #  variable don de vamos a guardar la lista
        #clients = self.list_clients()
        #12.- ahora utilizamo una variable auxiliar para poder ciclar entre los clientes
        # y unicamente tomar al cliente que se modifico y reemplazarlo y los demas
        # clientes dejarlos comos estan
        #updated_clients=[]
        #for client in clients:
            #if client['uid']== updated_client.uid:
                #tener en cuenta que cuando escribimos tenemos que hacerlo con to_dict()
                #updated_clients.append(updated_client.to_dict())
            #else:
                #updated_clients.append(client)
        #13.- ahora lo que tenemos que hcer es mandarlo al disco y para eso utilizamos un
        #  metodo privado _save_to_disk()
        #self._save_to_disk(updated_clients)

    #14.- declaramos el metodo _save_to_disk(), iniciamos creando una tabla temporal de nuestros clientes
    # despues con with open() abrimos el archivo temporal y creamos nuestro writer, despues solo escribimos
    # todos los clientes con la funcion writerows
    """ def _save_to_disk(self,clients):
        tmp_table_name = self.table_name +'.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerows(clients) 
    
        #ahora solo queda borrar el archivo original, luego renombrar el tmp y dejarlo con el nombre del original
        os.remove(self.table_name)
        os.rename(tmp_table_name,self.table_name)
 """

    def delete_client(self,client_uid):
        self.delete(client_uid,Client.schema())
    
