import os
from bs4 import BeautifulSoup
import gettext

_ = gettext.gettext

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

    print(_("Language code updated to: "), languageCode)
    print(_("Language in file name updated to: "), languageName)

    # open file
    file = open(
        actualFile,
        "w")

    # new content is writen into the file
    file.write(str(soup))  # str() writes content matching source file format

    file.close()

    createNewFile(actualFile, languageCode, languageName)

def createNewFile(actualFile, languageCode, languageName):

    path = actualFile.split("/")
    fileName = path[2]
    print(_("File name: "),fileName)

    new_name = fileRename(fileName, languageCode, languageName)
    print(_("New file name: "),new_name)
    path[2] = new_name
    path[1] = "Final_target_files"
    # print("Path: ",path)

    newFile = "/".join(path)
    print(_("New file path: "),newFile)

    # New Directory is created
    newPath = "./Final_target_files/"
    print(_("New Path: "), newPath)
    # Check whether the specified path exists or not
    if not os.path.exists(newPath):
        os.makedirs(newPath)

    # File is remaed into new directory
    os.rename(actualFile, newFile)

def fileRename(fileName, languageCode, languageName):

    languageCode = languageCode.replace("-","_")
    new_name = fileName.replace('English', languageName).replace(languageCode,'').replace('_', '')
    return new_name