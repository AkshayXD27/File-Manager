#import required built-in modules
import os, keyboard, time

class changeDir:
    def __init__(self):
        os.chdir("/")
        self.__cwd = os.getcwd()
        self.__nwd = ""

    def path_modifier(self):
            if not(self.__cwd.endswith(">")):
                if self.__cwd == "C:":
                    self.__cwd = self.__cwd + "\\>"
                    return self.__cwd
                self.__cwd = self.__cwd + ">"
                return self.__cwd
            return self.__cwd

    def enter_dir_file(self):
            os.chdir(self.__cwd)
            self.__nwd = ""
            print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

    def read_dir_file_name(self):
        print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)
        while True:
            pressedEnter = True
            while pressedEnter:

                event = keyboard.read_event()
                time.sleep(0.03)

                if event.event_type == keyboard.KEY_DOWN:

                    if event.name == "enter":
                      pressedEnter = False

                    elif event.name == "backspace":
                        self.__nwd = self.__nwd[:-1]

                    elif event.name == "esc":
                        if self.__nwd == "":
                            if self.__cwd == "C:\\>":
                                self.__cwd = self.__cwd[:self.__cwd.rindex(">")]
                            else:
                                self.__cwd = self.__cwd[:self.__cwd.rindex("\\")]
                            self.enter_dir_file()
                            pressedEnter = False
                        else:
                            self.__nwd = ""
                            pressedEnter = False

                    else:
                      if len(event.name)==1:
                          self.__nwd += event.name
                print(f"\r{self.__cwd}{self.__nwd}\x1b[K",end="",sep="",flush=True)
    
            else:
                if self.__nwd == "":
                    self.__cwd = self.__cwd.rstrip(">")
                    self.enter_dir_file()
                else:
                    print()
                    if self.__cwd == "C:\\>":
                        self.__cwd = self.__cwd.replace(">","")
                        self.__cwd = self.__cwd + self.__nwd
                    else:
                        self.__cwd = self.__cwd.replace(">","\\")
                        self.__cwd = self.__cwd + self.__nwd
                    self.enter_dir_file()
    
            time.sleep(0.05) 