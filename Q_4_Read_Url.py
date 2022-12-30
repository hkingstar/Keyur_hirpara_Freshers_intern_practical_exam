'''
4. Provide a program to read the file from URL and display the content
in terminal.
• The file URL has to be input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.

'''




import urllib.request

# Prompt the user to enter the URL of the file
url = input("Enter the URL of the file: ")

# Open the URL and read the contents of the file
with urllib.request.urlopen(url) as f:
    content = f.read()

# Convert the content from bytes to a string and print it to the terminal
print(content.decode())
