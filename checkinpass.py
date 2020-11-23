import re
import stringprep
def valid_password(pwd):
        length = len(pwd)
        if (length >= 2 and length <= 10):
                if (re.findall('^[A-Za-z]',pwd)):
                        if(re.findall('[A-Za-z0-9_]+[A-Za-z0-9]$',pwd)):
                                print("True")
                        else:
                            print("False")
                else:
                    print("False")
        else:
            print("False")
 
pwd = input('Please enter your password:')
valid_password(pwd)