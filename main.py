import os
import sys

commands = {'echo':True, 'pwd':True, 'exit':True, 'type':True}
PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

def exity(number = 0):
    print("# Shell exits with code", number)
    sys.exit(number)

def type_cas_2(commande):
    PathSplit = PATH.split(":")
    for i in range(len(PathSplit)):
        contents = os.listdir(PathSplit[i])
        if commande in contents : 
            executable = str(PathSplit[i]+"/"+commande)
            return executable
    return False

def ch_dir(path):
    if path[0] == "/" :
        try:
            os.chdir(path)
        except FileNotFoundError : 
            print(f"{path}: No such file or directory")
        except Exception as e:
            print(f"An error Occured:{e}")
    elif path[0:2] == ".." : 
        try : 
            absolute_path = os.getcwd()
            separate_path = absolute_path.split("/")
            separator = "/"
            new_path = separator.join(separate_path[:-1])
            if len(path) > 2 :
                new_path = new_path + "/" + path[2:]
            elif new_path == '' :
                    new_path = "/"
            os.chdir(new_path)
        except Exception as e :
            print(f"An error occured:{e}")
    elif path[0] == "~" :
        try : 
            home_path = os.getenv('HOME')
            if len(path) > 1 :
                home_path = home_path + path[1:]
            os.chdir(home_path)
        except Exception as e :
            print(f"An error Occured: {e}")
    else :
        try :
            absolute_path = os.getcwd()
            final_path = absolute_path + "/" + path
            os.chdir(final_path)
        except Exception as e :
            print(f"en Error Occured:{e}")

while True:
    shell_input = input("$ ").split(" ")
    output = ""
    if len(shell_input) > 1 :
        while shell_input[1] == '':
            shell_input.pop(1)
            if len(shell_input) == 1 :
                break
    if shell_input[0] == "echo" : 
        for i in range(1,len(shell_input)):
            output += shell_input[i] + " "
        print(output)
    elif shell_input[0] == "pwd":
        print(os.getcwd())
    elif shell_input == [''] : 
        shell_input = input("$ ").split(" ")
    elif shell_input[0] == "exit":
        if len(shell_input) > 1:
            exity(int(shell_input[1]))
        else:
            exity()
    elif shell_input[0] == "type":
        if shell_input[1] in commands:
            print(shell_input[1],"is a shell builtin")
        elif type_cas_2(shell_input[1]) :
            executable = type_cas_2(shell_input[1])
            print(shell_input[1], "is", executable)
        else:
            print(shell_input[1]+": not found")
    elif shell_input[0] == "cd":
        if len(shell_input) > 1 : 
            path = shell_input[1]
            ch_dir(path)
        else:
            ch_dir(os.getenv('HOME'))
    else:
        print(shell_input[0] + ": command not found")