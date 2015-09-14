#!/usr/bin/env python3

encrypted_text = """
KRGBF IATEU VUNNW WAKAF RAPTU TCYNG ECWJH 
XYQFH HZMXR RBOCI WRIJU EWAHS MTGPA JIQGV 
RKBFT VBKJR EPAPN XYMZV GHVOQ GJYWU GWYUI 
NXBLG FCNYA XUHAF HFPFJ VKVNA OPEXT HHUQQ 
MKXTM NEBII TLVUX FSZCB NAUKI RGJQA ZGTOE 
CXUIJ MNVVB YBXUT RWGHD ZTEYO NRBDX LVSNK 
VJPQF BOBIG PJMTC PBENB OBIYU INEQH CRCYQ 
RACCQ FRLZW YXCCS SYEFS RYBTP PGRRG PIW"""
s_encrypted = "OMLBOMVYQIYRVVQSHTYBFLGCSIYRFIJGXUZYVTKB"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotation_right = True

known_words = ["FATALITIES","ALGO"]

# First we need to delete all spaces from encrypted text:
encrypted_text_new = ""
# First we remove spaces
for word in encrypted_text.split(" "): 
    encrypted_text_new += word
    
encrypted_text = ""
# And then, we remove breaklines
for word in encrypted_text_new.split("\n"):
    encrypted_text += word
    
# We need to calculate the half of alphabet:
alphabet_first, alphabet_last = [],[]    
for letter in alphabet[:len(alphabet)//2]:
    alphabet_first.append(letter)
for letter in alphabet[len(alphabet)//2:]:
    alphabet_last.append(letter)
#print(alphabet_last)

#Create dictionaries
dictionarie = {}

#for i in range(13): l[-i:]+l[:-i]

for letra in range(len(alphabet)):
    dictionarie[alphabet[letra]] = [alphabet_first,alphabet_last[-(letra//2):]+alphabet_last[:-(letra//2)]]

def return_pattern(word,alphabet_first,alphabet_last):
    word_pattern = ""
    for letter in word:
        if letter in alphabet_first:
            word_pattern += str(0)
        elif letter in alphabet_last:
            word_pattern += str(1)
        else:
            print("Unexpected Error")
            return
       
    return word_pattern

        
def invert_pattern(pattern):
    new_pattern = ""
    for num in pattern:
        if num == "0":
            new_pattern += "1"
        else:
            new_pattern += "0"
    return new_pattern



def find_match(encrypted,theory):
    # Search for a coincident match        
    pattern_encrypt = return_pattern(encrypted,alphabet_first,alphabet_last)
    # The theory pattern should be inverted
    pattern_theory = invert_pattern(return_pattern(theory,alphabet_first,alphabet_last))
    matches = pattern_encrypt.split(pattern_theory)
    results = []
    for match in matches:
        results.append(len(match))
    print (results)
    return results


def extract_word(encrypted_text,known_word):

    place = find_match(encrypted_text, known_word)
    encrypted_word = encrypted_text[place[0]:place[0]+len(known_word)]
    return encrypted_word

#extract_word(s_encrypted,known_words[1])

def extract_dictionary(theory_word, encrypted_word, dictionary):
    possible_key = []

    for char in range(len(theory_word)):
        pair = []
        
        if theory_word[char] in alphabet_first:
            for table in dictionary:
                indice = dictionary[table][1].index(encrypted_word[char])
                if dictionary[table][0][indice] is theory_word[char]:
                    pair.append(table)
        
        elif theory_word[char] in alphabet_last:
            for table in dictionary:
                lett = dictionary[table][1].index(theory_word[char])
                if dictionary[table][0][lett] is encrypted_word[char]:
                    pair.append(table)
        else:
            pair.append(NULL)
        possible_key.append(pair)
        
    return possible_key
        
print(extract_dictionary(known_words[0],extract_word(encrypted_text,known_words[0]),dictionarie))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




