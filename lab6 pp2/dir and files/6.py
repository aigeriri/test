def generate_text_files():
    for letter in range(65, 91): 
        file_name = f"{chr(letter)}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}")

generate_text_files()
print("26 text files created.")
