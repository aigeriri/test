import os

def check_access(path):
    exists = os.path.exists(path)
    is_readable = os.access(path, os.R_OK) if exists else False
    is_writable = os.access(path, os.W_OK) if exists else False
    is_executable = os.access(path, os.X_OK) if exists else False
    return exists, is_readable, is_writable, is_executable

path = '/Users/zhaisanovaaigerim/Documents' 
exists, readable, writable, executable = check_access(path)
print(f"Exists: {exists}, Readable: {readable}, Writable: {writable}, Executable: {executable}")
