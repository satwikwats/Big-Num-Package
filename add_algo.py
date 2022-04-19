#addition case
#Takes in integer value and does operation in list and returns integer value
def listadd(n1, n2):
    l1 = [int(x) for x in str(n1)]
    l2 = [int(x) for x in str(n2)]
    if l2 == [] and l1==[]:
        print([])
    elif l2 == []:
        print(l1)
    elif l1==[]:
        print(l2)
    else:
        if (len(l2) > len(l1)):
            x = l2
            l2 = l1
            l1 = x
        a=len(l1)
        b=len(l2)
    
        l3=[]
        l1 = l1[::-1]
        l2 = l2[::-1]
        carry=0
        for i in range(b):
 
            addition = ((l1[i])+(l2[i])+carry)
 

            if (addition >= 10):
 
                addition = addition - 10
                carry = 1
 
            else:
                carry = 0
 
            l3.append((addition))
 
    
        for i in range(b, a):
 
            addition = ((l1[i])) + carry
 
        
            if (addition >= 10):
 
                addition = addition - 10
                carry = 1
 
            else:
                carry = 0
 
            l3.append((addition))
 
    
        l3 = l3[::-1]
        L3 = [str(x) for x in l3]
        n3 = ''
        for i in L3:
            n3=n3+i
        N3 = int(n3)
        return N3
