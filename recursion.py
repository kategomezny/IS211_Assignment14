""" Recursion to implement algorithms"""

def fibonnaci(n):
    """accepts a parameter n to return the nth
       element of the Fibonnaci sequence.
       
       Args:
           n (int):  Number which represents the n item in a sequence
           
       Returns:
           int:   the nth element of the Fibonnaci sequence
           
       Examples:
            fibonnaci(3)
            Out[2]: 2
            
            fibonnaci(8)
            Out[4]: 21      
       """
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fibonnaci(n-1)+fibonnaci(n-2)  
    

def gcd(a, b):
    """ takes parameters a and b and returns their 
        greatest common divisor.
        
        Args:
            a,b (int)
            
        Returns:
            int:  greatest common divisor between a and b.
            
        Examples:
            
            gcd(12,30)
            Out[15]: 6
            
            gcd(50,36)
            Out[16]: 2
            """
    if b % a == 0:
        return a
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
        
        
def  compareTo(s1, s2):
    """ compares two strings
    
    Args:
        s1, s2(str):  Strings to be compared.
        
    Returns:
        a negative number if s1 < s2,
        0 if s1 == s2, and
        a positive number if s1 > s2
    
    Examples:
        
        compareTo('ab', 'ba')
        Out[21]: -1

        compareTo('ba', 'ab')
        Out[22]: 1

        compareTo('ab', 'ab')
        Out[23]: 0
    """
    if s1 < s2: 
        return -1
     
    elif s1 == s2:
        return 0
    
    else:
        return 1
        
