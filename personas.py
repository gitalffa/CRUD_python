

class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, My name is {} and I am {} years old".format(self.name,self.age))


if __name__ =='__main__':
    person=Persona('David',34)

    print('Age:{}'.format(person.age))
    person.say_hello()