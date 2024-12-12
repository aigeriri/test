import csv
users=[
    ('personName', 'phoneNumber'),
    ['Arsen', '123'],
    ['Aliya', '77777']
]
with open(r'C:\Users\D16 i7-13700k\Desktop\pp2 ахма\lab10\PhoneBook\abc.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    writer.writerows(users)