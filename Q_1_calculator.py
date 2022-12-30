'''1. Provide a program for the calculator from terminal.
• Make sure it do not ask questions but when you press enter. it displays the result. 
• Amount and formula has to be in one line. 
e.g 456 - 12 
 564/ 10 
 456*1234+09-12
 
 '''





while True:
  # Read input from the user
  formula = input('Enter a formula (or "q" to quit): ')
  
  # Check if the user wants to quit
  if formula.lower() == 'q':
    break
  
  # Evaluate the formula and print the result
  result = eval(formula)
  print(result)