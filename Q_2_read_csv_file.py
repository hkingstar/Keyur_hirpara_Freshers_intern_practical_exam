'''
2. Provide a program to read the CSV file.
• CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-DD) the third column is salary.
• Read the file and display the data and age in the terminal.
• The file path, delimiter, and quote char are the input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.

'''




import csv
import datetime

def read_csv(file_path, delimiter, quote_char):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter, quotechar=quote_char)
        for row in reader:
            name = row[0]
            birthdate = row[1]
            salary = row[2]
            birth_year = 2022
            try  :
                birth_year = int(birthdate[0:4])
            except:
                birth_year2= birthdate[0:4]  
                
            current_year = datetime.datetime.now().year
            age = current_year - birth_year
            print(f'Name: {name}, Birthdate: {birthdate}, Age: {age}, Salary: {salary}')

file_path = input("Enter the file path: ")
delimiter = input("Enter the delimiter: ")
quote_char = input("Enter the quote character: ")
            
            
read_csv(file_path, delimiter, quote_char)