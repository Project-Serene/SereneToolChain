import ctypes
import os.path

SERENE_COMPILER_DLL_NAME = "libSerene.Compiler.dll"
file_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + SERENE_COMPILER_DLL_NAME
SERENE_COMPILER_DLL = ctypes.CDLL(file_path)

def compile_file(source_file: str, output_file: str):
    source_file = ctypes.create_string_buffer(source_file.encode())
    output_file = ctypes.create_string_buffer(output_file.encode())
    SERENE_COMPILER_DLL.CompileFile(source_file, output_file)
