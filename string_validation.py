if __name__ == '__main__':
    s = input()
    if s.isalnum()==True:
        print("True")
    else:
        print("False")

    if s.isalnum()==True:
        if s.isdigit()==True:
            print("False")
        else:
            print("True")


    if s.isalpha()==True:
        print("False")
    else:
        print("True")


    if s.islower()==True:
        print(True)
    elif s.isupper()==True:
        print("False")
    else:
        print("True") 

    if s.isupper()==True:
        print("True")
    elif s.islower()==True:
        print("False")
    else:
        print("True")



   
    

