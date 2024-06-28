def isPalindrome(x):
    temp=x
    reverse=0
    while (x>0):
        digit=x%10
        reverse=reverse*10+digit
        x=x//10
    if(temp==reverse):
        return True
    else:
        return False
result = isPalindrome(121)
print(result)