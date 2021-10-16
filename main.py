import sys
import ast

class User:
    def __init__(self, item, name, **kwards):
        self.item = item
        self.name = name
        self.kwards = kwards
    def print_user(self):
        
        if self.item == "Person":
            print("{} trabaja en la posición de {}.".format(self.name, 
                self.kwards["position"]))
        elif self.item == "Dog":
            print("{} pertenece a la raza {} y tiene {} años de edad.".format(self.name, 
                self.kwards['breed'], self.kwards['age']))
        elif self.item == 'Song':
            print("Song: {} - {}".format(self.kwards['artist'], self.name))
        else:
            print("{} es un item desconocido.".format(self.item))


if __name__ == '__main__':
    args = sys.argv[1]
    file = open(args, "r")

    contents = file.read()
    list_items = ast.literal_eval(contents)

    file.close()
    for item in list_items:
        user = User(**item)
        user.print_user()
