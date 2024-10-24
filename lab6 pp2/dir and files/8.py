import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK): 
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print("File is not writable.")
    else:
        print("File does not exist.")


file_path = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/delete me.txt'  
delete_file(file_path)
