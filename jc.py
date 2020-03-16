
# number of elements 
# n = int(input("Enter number of elements : ")) 

# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
  
# print("\nList is - ", a) 

#print("Enter the string : ")
s = input()
#print("Enter index : ")
n = int(input())
#count = 0


def findChar(s,e):
    c = 0
    p =0
    for i in range(len(s)):
        if(s.find('a',p,len(s)) != -1):
            c = c + 1
            i = p
    return c
        




if(len(s) >= n):
    print(s.find('a',0,len(s)))
else:
    while len(s) < n:
        s.join(s)
    


