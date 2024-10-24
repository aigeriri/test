import shutil

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Copied {src} to {dst}")
    except FileNotFoundError:
        print("Source file not found.")

src_file = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/a.txt' 
dst_file = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/b.txt'  
copy_file(src_file, dst_file)
