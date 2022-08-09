import os
from os import path
from compiler import compile_file
import sys


def under_pros_directory() -> bool:
    cwd = os.getcwd()
    pros_file = os.path.join(cwd, "project.pros")
    serene_bytecode_file = os.path.join(cwd, "src" + os.path.sep + "serene_bytecode.h")
    if not path.exists(pros_file) or not path.isfile(pros_file):
        print("Current Working Directory is not a PROS project. [ERROR]")
        return False
    elif not path.exists(serene_bytecode_file) or not path.isfile(serene_bytecode_file):
        print("Serene PROS Template not Found. [ERROR]")
        return False
    else:
        return True


if __name__ == '__main__':
    # if not under_pros_directory():
    #     exit()
    if not sys.argv[1] or sys.argv[1] != 'compile':
        print("Invalid Command [ERROR]")
        exit()
    if not sys.argv[2] or not path.exists(sys.argv[2]) or not path.isfile(sys.argv[2]) or not sys.argv[2][
                                                                                              -4:] == '.lua':
        print("Invalid File")
        exit()
    compile_file(sys.argv[2], os.path.join(os.getcwd(), "src" + os.path.sep + "serene_bytecode.h"))
