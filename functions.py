import os
from bs4 import BeautifulSoup

def fileRead(actualFile):
    # HTML file is parsed into a BeautifulSoup object
    with open(actualFile) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup

def fileUpdate(actualFile, languageCode, languageName):

    # HTML file is parsed
    soup = fileRead(actualFile)
    # HTML tag is selected
    html_tag = soup.html
    # attribute LANG is updated to "LANGUAGE_CODE"
    html_tag['lang'] = languageCode #'it_IT'
    html_tag['xml:lang'] = languageCode #'it_IT'

    print("Language code updated to: ", languageCode)
    print("Language updated to: ", languageName)

    # open file
    file = open(
        actualFile,
        "w")

    # new content is pasted into file
    for line in soup:
        file.write(str(line))  # str() writes content matching source file format

    file.close()

    createFile(actualFile, languageCode, languageName)

def createFile(actualFile, languageCode, languageName):

    path = actualFile.split("/")
    fileName = path[2]
    print("File name: ",fileName)

    new_name = fileRename(fileName, languageCode, languageName)
    print("New file name: ",new_name)
    path[2] = new_name
    path[1] = "Finished_target_files"
    print("Path: ",path)

    newFile = "/".join(path)
    print("Joined Path: ",newFile)

    # New Directory is created
    newPath = "./Finished_target_files/"
    print("New Path: ", newPath)
    # Check whether the specified path exists or not
    if not os.path.exists(newPath):
        os.makedirs(newPath)

    # File is remaed into new directory
    os.rename(actualFile, newFile)

def fileRename(fileName, languageCode, languageName):

    new_name = fileName.replace('English', languageName).replace(languageCode,'').replace('_', '')
    return new_name