# writing a code where a number can be read from left to right and from rigth to left
number = int(input("enter a number:"))
if number < 0:
    print("it cannot be a palindrom, since it ias a negative number")
else:
    temp = number
    reverse = 0
    while temp != 0:
     remainder = temp %10
     reverse = (reverse *10) + remainder
     temp = temp//10
    if reverse == number:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")