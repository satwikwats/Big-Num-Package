def subtractfun(list_a, list_b):
    if list_a == [] and list_b==[]:
        print([])
    elif list_b == [] and list_a!=[]:
        print(list_a)
    elif list_a==[]:
        print("Error")
    else: 
        x = len(list_a)
        y = len(list_b)
        a_string = ""
        b_string = ""

        for i in range(x):
            a_string += str(list_a[i])
    
        for i in range(y):
            b_string += str(list_b[i])
    
        a_string = int(a_string)
        b_string = int(b_string)

        if a_string > b_string:
            print("List b is subtracted from list a")
        elif(a_string == b_string):
            print("List a and list b are equal")
        else: 
            x = list_b
            list_b = list_a
            list_a = x
            print("List a is subtracted from list b")
        n1=len(list_a)
        n2=len(list_b)
    
    
        list_c=[]
        list_a = list_a[::-1]
        list_b = list_b[::-1]
        carry=0
        for i in range(n2):
 
            subtract = ((list_a[i])-(list_b[i])-carry)
 

            if (subtract < 0):
 
                subtract = subtract + 10
                carry = 1
 
            else:
                carry = 0
 
            list_c.append(subtract)
 
    
        for i in range(n2, n1):
     
            subtract = (((list_a[i])) - carry)
 
        
            if (subtract < 0):
 
                subtract = subtract + 10
                carry = 1
 
            else:
                carry = 0
 
            list_c.append(subtract)
 
    
        list_c = list_c[::-1]
 
        return list_c


    
