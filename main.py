import sys
import ast

class User:
    """
    Class to describe every item

    Attributes:
        raw (bool):
        item (type):
        verify_item(item) (type):
        name (type):
        verify_item(name) (type):
        kwards (type):
        verify_item(kwards) (type):

    Args:
        item (undefined):
        name (undefined):
        **kwards (undefined):

    """
    def __init__(self, item, name, **kwards):
        self.raw = 0
        self.item = self.verify_item(item)
        self.name = self.verify_item(name)
        self.kwards = self.verify_item(kwards)

    def verify_item(self, it):
        """
        Description of verify_item

        Args:
            self (undefined):
            it (undefined):

        """
        if isinstance(it, dict):
            if None in it.values():
                self.raw = 1
            if None in it.keys():
                self.raw = 1
        else:
            assert it != "None", "A key is noneType which is invalid %r" % it
        return it

    def person(self):
        """
        Description of person

        Args:
            self (undefined):

        """
        
        print("{} trabaja en la posición de {}. \n".format(self.name, 
                self.kwards["position"]))
    
    def dog(self):
        """
        Description of dog

        Args:
            self (undefined):

        """
        print("{} pertenece a la raza {} y tiene {} años de edad. \n".format(self.name, 
                self.kwards['breed'], self.kwards['age']))

    def song(self):
        """
        Description of song

        Args:
            self (undefined):

        """
        print("Song: {} - {}. \n".format(self.kwards['artist'], 
                self.name))
    
    def unknown(self):
        """
        Description of unknown

        Args:
            self (undefined):

        """
        print("{} es un item desconocido. \n".format(self.item))

    def print_user(self):
        """
        Description of print_user

        Args:
            self (undefined):

        """
        if not self.raw:
            if self.item == "Person":
                self.person()
            elif self.item == "Dog":
                self.dog()
            elif self.item == 'Song':
                self.song()
            else:
                self.unknown()
        return self.raw

if __name__ == '__main__':
    args = sys.argv[1]
    file = open(args, "r")

    contents = file.read()
    list_items = ast.literal_eval(contents)

    file.close()
    errors = []
    for item in list_items:
        if all(isinstance(s, str) for s in item.keys()):
            user = User(**item)
            if_raw = user.print_user()
        else: 
            if_raw = True
        if if_raw !=0:
            errors.append(item)
    print(errors)