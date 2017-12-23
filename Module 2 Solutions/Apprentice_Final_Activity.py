import operator
import sys
import os
saved_string = ''

#=====================================================================================

def remove_letter(): #Remove a selected letter from a string
  #os.system('clear')
  remove = str(raw_input("Enter letter to remove: "))
  remove = remove[0]
  global saved_string 
  edited_str = saved_string.replace(remove,"")
  print "Edited string is: %s" %edited_str
  return edited_str
#=====================================================================================
  
def num_compare(): #Compare 2 numbers to determine the larger
  #os.system('clear')
  a = int(raw_input("Enter first number: "))
  b = int(raw_input("Enter second number: "))
  if(a>b):
    print "Number %d is greater than %d" %(a,b)
  elif(a<b):
    print "Number %d is greater than %d" %(b,a)
  else:
    print "They're equal"
#=====================================================================================

def print_string(): #Print the previously stored string
  #os.system('clear')
  global saved_string
  if(saved_string == ""):
    print "\nNo value has been entered. Please enter a value first!"
  else:
    print "Saved String is: %s" %saved_string
#=====================================================================================

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
  #os.system('clear')
  a = int(raw_input("Enter first value: "))
  b = int(raw_input("Enter second value: "))
  a_b_Div = 0
  a_b_Rem = 0
  a_b_Sum = a+b
  a_b_Sub = a-b
  a_b_Prod = a*b
  try:
    a_b_Div = a/b
    a_b_Rem = a%b
  except ZeroDivisionError:
    print "You can't divide by zero numbnuts! 'Insert facepalm emoji here'"
  print "Sum: %d \nDifference: %d \nProduct: %d " %(a_b_Sum, a_b_Sub, a_b_Prod)
  if(b!=0):
	print "Quotient: %d \nRemainder: %d" %(a_b_Div, a_b_Rem)
  else:
	print "Quotient: Division by Zero \nRemainder: Division by Zero"
#=====================================================================================

def accept_and_store(): #Accept and store a string
  #os.system('clear')
  global saved_string 
  saved_string = str(raw_input("\nEnter the string to be saved: "))
  #saved_string = string_input
  print "Entered string: is %s" %saved_string
#=====================================================================================

def main(): #menu goes here
  global saved_string
  try:
    bool1 = True
    while bool1 == True:
      print "\n\ Welcome to Apprentice Program in Python / \n"
      print "1.\tLetter removal\n"
      print "2.\tCompares 2 numbers\n"
      print "3.\tPrint stored string\n"
      print "4.\tCalculator\n"
      print "5.\tEnter string to perform operations\n"
      print "6.\tClear screen\n"
      option = int(raw_input("\nEnter your option or Press Ctrl+C to exit: "))
      if(option == 1):
        saved_string = remove_letter()
      elif(option == 2):
        num_compare()
      elif(option == 3):
        print_string()
      elif(option == 4):
        calculator()
      elif(option == 5):
        accept_and_store()
      elif(option == 6):
		os.system('clear')
      else:
        os.system('clear')
        print "\nXXXXX  Bad input kid! Try Again  XXXXX\n"
  except KeyboardInterrupt:
    sys.exit(0)
main()
#=====================================================================================
