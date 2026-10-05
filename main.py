#import other classes(.py files) into the main class(main.py)
import fileStructure
import cmdFileStructure

if __name__ == '__main__':
    # mainobj = fileStructure.file_structure()
    # mainobj.manipulate()
    mainobj = cmdFileStructure.cmd_file_structure()
    mainobj.read_dir_name()