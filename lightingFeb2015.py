### Begin Ifs in Python:
##
### Python ifs presented by Professor Reed
### last updated (11-DEC-2014)
### for Python 3.4+
### Lighting Talks -- Python User Group -- Feb. 2015
##
##
import string

def simpleIf(x):
    if x < 0:
        print("simple if test ran:", x)

def ifWithElse(x):
    if x < 0:
        print("with else test ran:", x)
    else:
        print("else x determines x is greater than a negative value")

def elseIf(x):
    if x < 0:
        print("with else elseif:", x)
    elif x == 0:
        print("elseif x is equal to zero")
    else:
        print("elseif final else x is greater than a negative value")

def simpleifalpha(x):
    if str.isalpha(x):
        print("simple if alpha test ran:", x)

def simpleifnumeric(x):
    if str.isnumeric(x):
        print("simple if numeric test ran: ", x)
       
def lowercasecheck(x):
    if str.islower(x):
        print("if lowercase found: ", x)
    else:
        print("x is not lowercase: ", x)

def caseChkelif(x):
    if str.islower(x):
        print("if case chk found lowercase: ", x)
    elif str.isupper(x):
        print("x is UPPERCASE by case chk: ", x)
    else:
        print("x is something other: ", x)
##        
##       
### --- Professor Reed's test driver area --- ###
##        
def testMyIfs():
##    
### Part I ###
    x = 'c' ## x is assigned lower case 'c' value
##    x = 'C' ## x is assigned upper case 'C' value
##    x = '22' ## x is assigned a value of 22
##    x =  22 ## x is assigned a numeric value of 22
##    x = -22 ## neg x is assigned value of -22
##
### Part II ###   
##    x = -1
##    x = 0
##    x = 1
    print()
    print("x is: ", x)
##        
    print()
    print("the value of x is: ", x)
##    simpleIf(x)
##    ifWithElse(x)
    simpleifalpha(x)
    simpleifnumeric(x)
    lowercasecheck(x)
    caseChkelif(x)
    print()

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()    
    
