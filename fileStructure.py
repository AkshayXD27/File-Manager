#import required built-in modules
import os, keyboard, time

class file_structure:
    def __init__(self):
        self.__path = '/'
        os.chdir('/')
        self.__cwd = os.getcwd()
        self.__nwd = ''
        print("Currently in",self.__cwd)

    def return_dir_files(self):
        return os.listdir(self.__cwd)

    def path_constructor(self,path):
        if not(path.endswith("\\")):
            path = path + "\\"
            return path
        return path

    def path_destructor(self,path):
        if len(path)>3:
            if (path.endswith("\\")):
                path = path.rstrip("\\")
            path = path[(path.rfind("\\")+1):]
            self.__cwd = self.__cwd.replace(path+"\\","")
            return self.__cwd
        
        return self.__cwd
    
    def browse_cwd(self,x=-1):
        dir_files = self.return_dir_files()
        if x>=0:
            x = x%len(dir_files)
            print(f"\r{self.__cwd}{dir_files[x]}\x1b[K",end="",sep="",flush=True)
            return dir_files[x]
        elif x<0:
            print(f"\r{self.__cwd}\x1b[K",end="",sep="",flush=True)
            return


    def enter_dir_file(self,path):
        self.__cwd = path
        os.chdir(self.__cwd)

    def prev_dir(self,path):
        self.__cwd = path
        os.chdir(self.__cwd)

    def manipulate(self):
        x=-1
        while(True):
            if x<0:
                self.browse_cwd()

            if keyboard.is_pressed('down'):
                x+=1
                self.__nwd = self.browse_cwd(x)
                time.sleep(0.05)

            if keyboard.is_pressed('up'):
                self.browse_cwd()
                if x <0:
                    x = len(self.return_dir_files())
                else:
                    x-=1
                    self.__nwd = self.browse_cwd(x)
                    time.sleep(0.05)


            if keyboard.is_pressed('enter'):
                print()
                self.enter_dir_file(self.path_constructor(self.__cwd+self.__nwd))
                x=-1
                time.sleep(0.05)

            if keyboard.is_pressed('esc'):
                print()
                self.prev_dir(self.path_destructor(self.__cwd))
                x=-1
                time.sleep(0.05)
        
            time.sleep(0.05)