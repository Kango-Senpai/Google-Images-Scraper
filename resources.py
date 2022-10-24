import os
class DefaultImage:
    path = ""
class LogFile:
    path = ""

os.chdir("Resources")
DefaultImage.path = os.getcwd() + "\\default.png"
LogFile.path = os.getcwd() + "\\log.txt"
os.chdir("..")
