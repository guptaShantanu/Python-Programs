def count_substring(string, sub_string):
    n1=len(string)
    n2=len(sub_string)
    count=0
    for i in range(n1-n2+1):
        if string[i:i+3]==sub_string:
            count+=1
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
