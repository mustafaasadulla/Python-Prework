#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name +'!')
hello_name('USERNAME')


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for a in range(1,100,2):
        return a


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = a_list[ 0 ]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,12,5,3,7,3,9]))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).
def is_leap_year(a_year):
    leap = False
    
    if (a_year%4 ==0 and a_year%100 !=0) or a_year%400 ==0:
        leap = True
    else:
        leap = False

    return leap
year = int(input("Enter a year:"))
print(is_leap_year(year))


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    newlist=list(range(a_list[0],a_list[-1]+1)) 
    if a_list== newlist:
        return True 
    else: 
        return False 
number =[1,2,3,4,5,6,7,]
number2=[1,2,4,3,5,6,7]  
print(is_consecutive(number)) #True 
print(is_consecutive(number2))#False

     

