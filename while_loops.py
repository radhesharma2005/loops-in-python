#loops are used to repeat instructions
#syntax of while loop
"""while condition:
    #statement"""

# num=1
# while num<=10:
#     print("hello",num)
#     num+=1

# i=5
# while i>=1:                 #reverse condition
#     print(i)
#     i-=1
# print("loop ended")

# #print num 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# #print num 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i-=1
# #table
# n=int(input("enter the valid number:"))
# i=1
# while i<=10:
#     multi=n*i
#     print(f"{n}*{i}={multi}")
#     i+=1

# #print the numbers in list using while loop
# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(nums):
#     print(nums[i])
#     i+=1

# #write a program to find the number x in following tuple
# nums=(1,4,9,16,25,36,49,64,81,100)

# x=int(input("Enter the number you want to search : "))
# i=0
# while i<len(nums):
#     if (nums[i]==x):
#         print("FOUND at index value:",i)
#     i+=1


# #break : used to terminate the loop when encountered
# #continue : used to skip the current iteration and continues execution with next iteration

# i=1
# while i<=10:
#     print(i)
#     if(i == 5):
#         break       #exit the loop as soon as i==5
#     i +=1
# print("End of the loop")

# i=1
# while i<=15:
#     if(i==10):
#         i+=1
#         continue       #skipped the number 10
#     print(i)
#     i +=1
# print("number 10 is skipped")

#printing even nummbers using continue

a=int(input("Enter the number : "))
i=0
while i<=a:
    if(i%2!=0):
        i+=1
        continue
    print("Even number : ",i)
    i+=1


#printing odd nummbers using continue

a=int(input("Enter the number : "))
i=0
while i<=a:
    if(i%2==0):
        i+=1
        continue
    print("Odd number : ",i)
    i+=1