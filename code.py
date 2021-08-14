# --------------
def palindrome(num):

    while True:
        num+=1
        numS = str(num)  # stringify the number
        reversenum = numS[::-1]  # reverse the number
        if numS == reversenum:
            break
    return num


# --------------
def a_scramble(str_1, str_2):
    """Challenge 2 - Return whether str_1 characters can make str_2"""
    arr1 = list(str_1.lower());
    arr2 = list(str_2.lower());
    for i in arr2:
        try:
            arr1.remove(i)
        except ValueError:
            return False
    
    return True


# --------------
def check_fib(num):
    fibosum = 0
    secondlast = 1
    last = 1
    """Check if the number is a part of the Fibonacci sequence"""
    while num>last:
        fibosum = secondlast + last
        secondlast = last
        last = fibosum
        
    return True if last == num else False


# --------------
#Code starts here
def compress(word):
    """Return 'a3b2c4' if input is 'aaabbcccc'"""
    result = []
    counter = 0
    word = word.lower()
    
    last = word[0]
    
    for i in word:
        if last == i:
            counter += 1
        
        else:
            result.append(last)
            result.append(str(counter))
            counter = 1
            last = i
    
    result.append(last)
    result.append(str(counter))
    return("".join(result))


# --------------
#Code starts here
def k_distinct(string,k):
    """checks whether the 'string' has 'k' distinct characters"""
    return True if len(set(string.lower()))>=k else False


