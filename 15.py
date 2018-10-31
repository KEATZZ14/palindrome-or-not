//reading the number
print("Please enter the number ")
n=int(input(""))
temp=n//storing the number in a variable named temp
rev=0// set rev equal to zero
while(n>0):
    dig=n%10// finding the remainder of the number by dividing with 10
    rev=rev*10+dig
    n=n/10
if(temp==rev)://check the number equal to rev if so palindrome 
    print(" The number is palindrome ")
else:
    print("The number is not palindrome ")
