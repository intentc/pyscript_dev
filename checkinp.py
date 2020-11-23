import string

def valid_password(pwd):
        length = len(pwd)
        if (length >= 2 and length <= 10):
                if (pwd[0].isalpha()):
                        if (pwd.isidentifier()):
                                if (pwd[-1].isalnum()):
                                    print("True")
                                else:
                                    print("False")
                        else:
                            print("False")
                else:
                    print("False")
        else:
            print("False")
 
pwd = input('Please enter your password:')
valid_password(pwd)