# Plantilla Menu Imprimir
#
#
# Alejandro Ruiz


class Menu:
    def __init__(self, title, *args):
        self.__title = title
        if len(args) == 1 and (isinstance(args[0], tuple) or isinstance(args[0], list)):
            self.__options = list(args[0])
        else:
            self.__options = list(args)

#    @property
    def print_menu(self):
        if not self.__options:
            raise ValueError('No hay elementos en el menu')

        print(f'{self.__title:^40}')
        print(f'{"-"*len(self.__title):^40}')
        for i in range(len(self.__options)):
            print(f'{i+1}. {self.__options[i]}.')
        print(f'0. Salir.')
        print()

        q = int(input("Seleccione la opción que desee: "))
        print()
        print()

        if q <= len(self.__options) or (q == 0):
            return q
        raise ValueError('Debes introducir una opción válida.')