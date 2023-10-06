def returnAllA(length):
    return  length * "a"

def getOptimizedString(input, maxOp):
    inputLength = len(input)
    baseValue = ord('a')
    maxValidElement = 'a'
    maxValidIndex = -1
    
    ## To check for cases where there is maxOp >= 25 (only 25 ops is needed to convert z to a) or input is empty)
    if maxOp >= 25 or len(input) == 0:
        return returnAllA(inputLength)
    
    ## Loop through input from the left and break if any of the character cannot be converted to 'a' within the maxOp.
    ## we also keep track of the largest character that can be converted to 'a'
    for index, element in enumerate(input):
        if ord(element) - baseValue > maxOp :
            break
        maxValidIndex = index
        maxValidElement = max(maxValidElement, element)
        
    ## return all 'a' if all element can be converted to 'a' within the maxOp
    if maxValidIndex == inputLength - 1:
        return returnAllA(inputLength)
    
    ## Generate 'a's for the elements that can be converted to 'a'
    output = ''
    if maxValidIndex > -1 :
        output = returnAllA(maxValidIndex + 1)
    
    ## Check if there is any remaining Ops after converting left elements to 'a'
    remainingOps = maxOp - (ord(maxValidElement) - baseValue)
    convertedChar = chr(ord(input[maxValidIndex + 1]) - remainingOps)
    if(remainingOps > 0):
        output += convertedChar
    else:
        output += input[maxValidIndex + 1]
        
        
    for element in input[maxValidIndex + 2: len(input)] :
        if element <= maxValidElement :
            output += 'a'
        elif remainingOps > 0 and element <= input[maxValidIndex + 1] and element > convertedChar:
            output += convertedChar 
        else:
            output += element

    return output
    
print(getOptimizedString("abceabc",3))