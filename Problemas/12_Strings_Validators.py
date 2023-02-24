"""
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""


if __name__ == '__main__':
    s = input()
    contadorAlpha = 0
    contadorAlfabetico = 0
    contadorDigitos = 0
    contadorLower = 0
    contadorUpper = 0
    for i in range (len(s)):
        if(s[i].isalnum()):
            contadorAlpha+=1
        if(s[i].isalpha()):
            contadorAlfabetico+=1
        if(s[i].isdigit()):
            contadorDigitos+=1
        if(s[i].islower()):
            contadorLower+=1
        if(s[i].isupper()):
            contadorUpper+=1
            
    if(contadorAlpha>0):print(True)
    else: print(False)
    
    if(contadorAlfabetico>0):print(True)
    else: print(False)
    
    if(contadorDigitos>0):print(True)
    else: print(False)
    
    if(contadorLower>0):print(True)
    else: print(False)
    
    if(contadorUpper>0):print(True)
    else: print(False)