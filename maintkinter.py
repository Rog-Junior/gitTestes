import subprocess
from tkinter import *

repositorioGit = "https://github.com/Rog-Junior/gitTestes.git"
diretorio = r"C:\Users\Rog\Documents\Estudo\Desenvolvimento\GitKyou\gitTestes"


def GitClone():
   
    messageCmd = "git clone " + repositorioGit
    execute = subprocess.run(messageCmd, shell=True, capture_output = True, text = True)
    outputCommand['text'] = execute
    print(messageCmd)
    print(execute)

def ChangeDiretory():
    global diretorio
    diretorio = r"C:\Users\Rog\Documents\Estudo\Desenvolvimento\GitKyou\gitTestes"
    changeDiretoryCommand = f'cd {diretorio} && git clone {repositorioGit}'
    changeDiretoryExecute = subprocess.run(changeDiretoryCommand, shell = True, capture_output = True, text = True)
    print(changeDiretoryExecute)

def GitStatus():
    gitStatusCommand = f'cd {diretorio} && git status'
    gitStatusExecute = subprocess.run(gitStatusCommand, shell = True, capture_output = True, text = True)
    outputCommand['text'] = ""
    outputCommand['text'] = str(gitStatusExecute)
    print(str(gitStatusExecute))

def Main():
    global outputCommand


    windowMain = Tk()
    windowMain.title("Git Kyou")
    windowMain.geometry("400x400")

    text_orientation = Label(windowMain ,text="Seja bem vindo ao GitKyou")
    text_orientation.grid(column = 0, row = 0)

    executeGitClone = Button(windowMain, text="Efetuar clonagem do repositório", command= GitClone)
    executeGitClone.grid(column = 0, row = 1)
    executeChangeDiretory = Button(windowMain, text="Trocar diretorio", command= ChangeDiretory)
    executeChangeDiretory.grid(column = 0, row = 2)
    executeGitClone = Button(windowMain, text="Git Status", command= GitStatus)
    executeGitClone.grid(column = 0, row = 3)

    windowMain.grid_rowconfigure(4,weight = 4)
    outputCommand = Label(windowMain ,text="")
    outputCommand.grid(column = 0, row = 4)

    windowMain.mainloop()

Main()


