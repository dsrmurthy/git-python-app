import sys
#Working with command line arguments
#usage :   python cmdargs murthy 

if len(sys.argv) > 1:
    print("You have passed ")
    for index, argval in enumerate(sys.argv):
        print(f"arg{index}: {argval}")
        print(f"Your argument value is {argval}")
else:
    print("Sorry.. please pass args ;   Usage: python file.py  args.....")
