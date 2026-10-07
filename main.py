#import other classes(.py files) into the main class(main.py)
import cmdParseAndProcess

if __name__ == '__main__':
    print("Started cmd...")
    mainobj = cmdParseAndProcess.parseAndProcess()
    mainobj.read_dir_file_name()