import subprocess
import eel

repositorioGit = "https://github.com/Rog-Junior/gitTestes.git"

def Main():
    global outputCommand

   
   

Main()


eel.init('.')

@eel.expose
def GitClone():
    if(diretorio != ""):
        messageCmd = f'cd {diretorio} && git clone {repositorioGit}'
        execute = subprocess.run(messageCmd, shell=True, capture_output = True, text = True)
        # outputCommand['text'] = execute
        print(execute)
        return str(execute)
    else:
        return str("Não possui diretório")
    

@eel.expose
def GitStatus():
    gitStatusCommand = f'cd {diretorio} && git status'
    gitStatusExecute = subprocess.run(gitStatusCommand, shell = True, capture_output = True, text = True)
    print(str(gitStatusExecute))
    return str(gitStatusExecute)

@eel.expose
def ChangePathPy(Path):
    global diretorio
    diretorio = f'{Path}'
    changeDiretoryCommand = f'cd {diretorio}' # && git clone {repositorioGit} 
    changeDiretoryExecute = subprocess.run(changeDiretoryCommand, shell = True, capture_output = True, text = True)
    print(changeDiretoryExecute)
    return str(changeDiretoryExecute)

@eel.expose 
def GitPull():
    gitPullCommand = f'cd {diretorio} && git pull'
    gitPullExecute = subprocess.run(gitPullCommand, shell = True, capture_output = True, text = True)
    return str(gitPullExecute)

eel.start("./assets/main.html", mode="default", size=(800,600))
