#!/usr/bin/env python
import os
import functions as f

path = "./Directory-Target-Files/"

for file in os.listdir(path):
    print("===============================")
    actualFile = path + file
    print("Actual file: ", actualFile)
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