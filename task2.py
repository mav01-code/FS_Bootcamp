# 1
# n=int(input())
# list= [int(input()) for i in range(n)]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# 2
# String=input()
# count=0
# for i in String:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         count+=1
# print(count)

# 3
# n=int(input())
# def fact(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(n))

# 4 - Celsius to Fahrenheit
# c=float(input())
# f= (9/5)*c+32
# print(f)

# 5 - Calculator
# a=int(input())
# b=int(input())
# while(True):
#     op=input()
#     if(op=="+"):
#         print(a+b)
#     elif(op=="-"):
#         print(a-b)
#     elif(op=="*"):
#         print(a*b)
#     elif(op=="/"):
#         print(a/b)
#     else:
#         break

# 6- Word Frequency Counter
# words=input().split(" ")
# word_count={}
# for word in words:
#     word=word.lower()
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# print(word_count)   

# 7- Palindrome checker
# S=input()
# def palindrome(S):
#     return S==S[::-1]
# res=palindrome(S)
# if res:
#     print("Yes")
# else:
    # print("No")

# 8- Largest and smallest elements in a list
# n=int(input())
# list=[int(input()) for i in range(n)]
# list.sort()
# s=list[0]
# l=list[len(list)-1]
# print(s,l)

# 9- Reverse a list
# list=["Akshaya","Javiya","Vyshnavi","Manaswini","Gayatri","Anupama"]
# list.reverse()
# print(list)

# 10- 100 to 200, add +7 to each
# for i in range(100, 200, 7):
#     print(i)

# 11 - Grade calculation
"""
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())

if(s1<35):
    print("F")
elif(s1>=35 and s1<60):
    print("C")
elif(s1>=60 and s1<80):
    print("B")
elif(s1>=80):
    print("A")

if(s2<35):
    print("F")
elif(s2>=35 and s2<60):
    print("C")
elif(s2>=60 and s2<80):
    print("B")
elif(s2>=80):
    print("A")

if(s3<35):
    print("F")
elif(s3>=35 and s3<60):
    print("C")
elif(s3>=60 and s3<80):
    print("B")
elif(s3>=80):
    print("A")

if(s4<35):
    print("F")
elif(s4>=35 and s4<60):
    print("C")
elif(s4>=60 and s4<80):
    print("B")
elif(s4>=80):
    print("A")

if(s5<35):
    print("F")
elif(s5>=35 and s5<60):
    print("C")
elif(s5>=60 and s5<80):
    print("B")
elif(s5>=80):
    print("A")
"""

# 12- Sorting
# list=["Akshaya","Javiya","Vyshnavi","Manaswini","Gayatri","Anupama"]
# list.sort()
# print(*list)

# 13- Counting number of chocolates gopi gave to a person
persons=input().split(" ")
chocolate_count={}
for chocolate in persons:
    if chocolate in chocolate_count:
        chocolate_count[chocolate]+=1
    else:
        chocolate_count[chocolate]=1
print(chocolate_count)   