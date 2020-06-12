def print_formatted(number):
    for i in range(1,number+1):
        print(i,end=" ")
        print(int(oct(i)[2:]),end=" ")
        print(hex(i)[2:],end=" ")
        print(int(bin(i)[2:]))

print_formatted(25)
