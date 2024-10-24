def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/aiko.txt' 
try:
    line_count = count_lines(file_path)
    print(f"Number of lines in {file_path}: {line_count}")
except FileNotFoundError:
    print("File not found.")
