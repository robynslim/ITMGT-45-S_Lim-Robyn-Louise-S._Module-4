'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
alphabet=[]
alpha = 'A'
letter= str('A')
shift=int(25)
i= int(0)
alphabet=[chr(x) for x in range(ord('A'), ord('Z') + 1)]
    
letter_s = alphabet.index(letter)
letter=letter_s
if letter_s == alphabet.index('Z'):
            letter_s = alphabet.index('A')
         
while i < shift:
            if letter_s == alphabet.index('Z'):
                    letter_s = alphabet.index('A')
                    i+=1
            else:    
                            
                letter_s = letter_s + 1
                letter=letter_s
                print(letter)
                i+=1
letter=letter_s
 
print(alphabet[letter])

 

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
alphabet=[]
alpha = 'A'
letter= str('Z')
shift_n=int(0)
shift=str('X')
i= int(0)
alphabet=[chr(x) for x in range(ord('A'), ord('Z') + 1)]
    
letter_s = alphabet.index(letter)

shift_n= alphabet.index(shift)

         
while i < shift_n:
            if letter_s == alphabet.index('Z'):
                    letter_s = alphabet.index('A')
                    i+=1
            else:    
                            
                letter_s = letter_s + 1
                letter=letter_s
             
                i+=1

 
print(alphabet[letter])

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
alphabet=[]
message= str('A C')
letter= str('')
shift_n=int(0)
shift=str('')
shift_s=int(3)
key=str('KEY')
i= int(0)
a= int(0)
x= int(0)
y= int(0)
message_s=[]
alphabet=[chr(x) for x in range(ord('A'), ord('Z') + 1)]


    
while a< shift_s:

    if message[x]==' ':
        message_s.append(' ')
        
        x+=1
        y+=1
        a+=1
    else:
        i= int(0)
        letter_s = alphabet.index(message[x])
        letter=letter_s
        if y ==3:
                    y= 0
        shift_n= alphabet.index(key[y])
                
                
                

                            
        while i < shift_n:
            if letter_s == alphabet.index('Z'):
                    letter_s = alphabet.index('A')
                    i+=1
            else:    
                            
                letter_s = letter_s + 1
                letter=letter_s
               
                i+=1
            
        letter=letter_s
        message_s.append(alphabet[letter])
        
        x+=1
        y+=1
        a+=1
      
print(message_s)