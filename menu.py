import os
import functions as f
import gettext

_ = gettext.gettext

path = "./Directory-Target-Files/"
def menu():
    print("Selecciones una opción:")
    print()
    print("1. Convertir archivos")
    print("2. Salir")

menu()
option = int(input())
print(type(option))

while option != 2:
    match option:
        case 1:
            for file in os.listdir(path):
                print("===============================")
                actualFile = path + file
                print(_("Actual file: "), actualFile)
                if file.__contains__("de_DE"):
                    f.fileUpdate(actualFile, "de-DE", "German")
                    continue
                if file.__contains__("el_GR"):
                    f.fileUpdate(actualFile, "el-GR", "Greek")
                    continue
                if file.__contains__("fr_FR"):
                    f.fileUpdate(actualFile, "fr-FR", "French(FR)")
                    continue
                if file.__contains__("es_ES"):
                    f.fileUpdate(actualFile, "es-ES", "Spanish(Spain)")
                    continue
                if file.__contains__("it_IT"):
                    f.fileUpdate(actualFile, "it-IT", "Italian(Italy)")
                    continue
            print("===============================")
    menu()
    option = input()

print(_("Gracias por usar la aplicación"))
