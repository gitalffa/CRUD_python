#import uuid
from common.models import PVClient

#1.- creamos la clase Clients que sera el modelo de nuestro cleinte
class Client(PVClient):
    #2.- inicializamos nuestro cliente con el metodo __init__ y como primer 
    # parametro el damos self, que es el primer parametro de toda clase en 
    # python y ademas le pasamos todos las propiedades de los que va a constar
    # el modelo clients y como ultimos parametro le pasamos un uid que lo 
    # va a generar python con el modulo uuid
    def __init__(self,name,company,email,position, uid=None):
    #igualamos las propiedades a los parametros recibidos y la propiedad uid
    # la igualamos al uid recibido y si no recibimos nada utilizamos el modulo 
    # uuid y usamos su metodo uuid4 que es el standar en la industria

        #creo que la funcion super() la metieron para sustituir la funcion
        # privada to_dict(self) que nos regresa el diccionario del objeto pasado por parametro
        super().__init__(uid)
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        #self.uid=uid or uuid.uuid4()

# Python vars ()
# La función vars () devuelve el atributo __dict__ del objeto dado.
# La sintaxis de la vars()función es:

# vars(object)
# vars () Parámetros
# vars() toma un máximo de un parámetro.

# objeto : puede ser módulo, clase, instancia o cualquier objeto que tenga el __dict__atributo.
# Valor de retorno de vars ()
# vars()devuelve el __dict__atributo del objeto dado.
# Si el objeto pasado a vars()no tiene el __dict__atributo, genera una TypeErrorexcepción.
# Si no se pasa ningún argumento vars(), esta función actúa como la función locals () .
# Nota: __dict__ es un diccionario o un objeto de mapeo. Almacena los atributos del objeto (de escritura).
    #def to_dict(self):
    #   return vars(self)
#Este es un decorador llamado staticmethod que nos permite declarar metodos estaticos dentro de 
# nuestra clase, un metodo estatico es aquel que se puede ejecutar sin una instancia de clase,
#aqui los definimos el esquema o la estructura del arreglo de campos que tendra nuestra BD
    @staticmethod
    def schema():
        return ['name','company','email','position','uid']
        
