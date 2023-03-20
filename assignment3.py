#sum all the numbers in list
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
        return total
    print(sum((8,2,3,0,7)))

    
#reverse the string
def string_reverse(str1):
    rstr1=''
    index=len(str1)
    while index > 0:
        rstr1+= str1[index - 1]
        index=index - 1
        return rstr1
    print(string_reverse('1234abcd'))

#calculate the numberv of upper/lower case letters
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE",0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("original string:",s)
        print("No. of Upper case characters:",d["UPPER_CASE"])
        print("No. of Lower case character:",d["LOWER_CASE"])
        string_test('The quick Brown Fox')
