#import required built-in modules
import os, keyboard, time

class cmd_file_structure:
    def __init__(self):
        # self.__path = ""
        os.chdir('/')
        self.__cwd = os.getcwd()
        self.__nwd = ""
        print("CMD started...")

    def path_displayer(self):
            if not(self.__cwd.endswith(">")):
                self.__cwd += ">"
                return self.__cwd
            return self.__cwd

    def enter_dir_file(self):
        os.chdir(self.__cwd)
        print("Inside:",self.__cwd)
        self.__nwd = ""
        print(f"\r{self.path_displayer()}\x1b[K",sep="",end="",flush=True)


    def read_dir_name(self):
        print(f"\r{self.path_displayer()}\x1b[K",sep="",end="",flush=True)
        while True:
            while(keyboard.read_key() != "enter"):
                self.__nwd += keyboard.read_key()
                time.sleep(0.03)
                print(f"\r{self.path_displayer()}{self.__nwd}\x1b[K",sep="",end="",flush=True)
            else:
                if(self.__cwd == "C:\\>"):
                    self.__cwd = (self.__cwd + self.__nwd).replace(">","")
                else:
                    self.__cwd = (self.__cwd + self.__nwd).replace(">","\\")

                if self.__nwd =="":
                    self.enter_dir_file()
                else:
                    print("h")
                    self.enter_dir_file()
            
            time.sleep(0.05)