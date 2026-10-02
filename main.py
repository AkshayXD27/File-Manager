import os
import keyboard
import time

class path:
    def __init__(self):
        self.__path = '/'
        os.chdir('/')
        self.__cwd = os.getcwd()
        self.__nwd = ''
        print("Currently in",self.__cwd)

    def enter(self):
        entered = True
        x=-1
        while(True):
            dir_files = os.listdir()
            dir_files = [dir_files_item.casefold() for dir_files_item in dir_files]

            if x<=len(dir_files):
                if keyboard.is_pressed('down'):
                    x+=1
                    print(f"\r{self.__cwd}{dir_files[x]}\x1b[K",flush=True,sep='',end='')
                    self.__nwd = self.__cwd+dir_files[x]
                    time.sleep(0.05)

                else:
                    if x<0:
                        print(f"\r{self.__cwd}\x1b[K",flush=True,sep='',end='')
                    else:
                        print(f"\r{self.__cwd}{dir_files[x]}\x1b[K",flush=True,sep='',end='')

                if keyboard.is_pressed('enter'):
                        self.__nwd,self.__cwd = self.__cwd,self.__nwd
                        self.__cwd+= '\\'
                        os.chdir(self.__cwd)
                        x=-1
                        time.sleep(0.05)

                if keyboard.is_pressed('esc'):
                        os.chdir(self.__cwd)
                        x=-1
                        time.sleep(0.05)

                time.sleep(0.05)




if __name__ == '__main__':
    mainobj = path()
    mainobj.enter()