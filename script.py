import os
import functions as f

path = "./File-Directory-English-File/"

for file in os.listdir(path):
    print("===============================")
    actualFile = path + file
    print("Actual file: ", actualFile)
    if file.__contains__("de_DE"):
        f.fileUpdate(actualFile, "de_DE", "German")
        continue
    if file.__contains__("el_GR"):
        f.fileUpdate(actualFile, "el_GR", "Greek")
        continue
    if file.__contains__("fr_FR"):
        f.fileUpdate(actualFile, "fr_FR", "French(FR)")
        continue
    if file.__contains__("es_ES"):
        f.fileUpdate(actualFile, "es_ES", "Spanish(Spain)")
        continue
    if file.__contains__("it_IT"):
        f.fileUpdate(actualFile, "it_IT", "Italian(Italy)")
        continue
print("===============================")