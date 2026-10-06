#import other classes(.py files) into the main class(main.py)
import cmdChangeDir

if __name__ == '__main__':
    print("Started cmd...")
    mainobj = cmdChangeDir.changeDir()
    mainobj.read_dir_file_name()