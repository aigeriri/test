import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    return False, None, None

path = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/aiko.txt'  
exists, filename, directory = path_info(path)
if exists:
    print(f"Path exists. Filename: {filename}, Directory: {directory}")
else:
    print("Path does not exist.")
