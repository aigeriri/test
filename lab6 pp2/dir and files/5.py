def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

file_path = '/Users/zhaisanovaaigerim/Desktop/lab6 pp2/dir and files/aiko.txt'  
data = ['apple', 'banana', 'cherry']
write_list_to_file(file_path, data)
print(f"Data written to {file_path}.")
