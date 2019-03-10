import string


def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    assert (0 <= shift) and (shift < 26)
    
    upper_case_letters = string.ascii_lowercase
    lower_case_letters = string.ascii_uppercase

    shift_dict = {}
    
    for case in (upper_case_letters, lower_case_letters):
        for letter in case:
            
            # Find index boundaries 
            first_index = ord(case[0]) - 1
            last_index = ord(case[-1])
            
            if shift + ord(letter) <= last_index:
                shifted_letter = chr(shift + ord(letter))
            else:
                new_shift = shift + ord(letter) - last_index
                shifted_letter = chr(first_index + new_shift) 

            shift_dict[letter] = shifted_letter

    print(shift_dict)

build_shift_dict(-5)
