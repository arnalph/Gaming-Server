import os
import subprocess
import webbrowser
import db

direc = os.getcwd()
def rungame(gamedir:str,exe:str,typ:str):
    '''Runs the game for the system
    Run Codes- 1:Working, Relative
               2:Working, SDL
               3:Error'''
    os.chdir(direc+"/bin")
    conf = gamedir+"/server."+(exe.replace(".exe",""))+".conf"
    if typ=="rel":
        return 1
    if typ=="sdl":
        webbrowser.open("steam://rungameid/291550")
        '''if os.path.exists(gamedir)==True:
            subprocess.Popen([gamedir+exe])
        else:
            return 3'''
        os.system('ga-server-periodic config/server.brawlhalla.conf')
        return 2
    else:
        return 3

def rungame(code):
    dat = db.chk_game(code)
    for dat in dat:
        print(dat[0])
        print(dat[1])
        print(dat[2])
    
