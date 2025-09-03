def caesar(text:str, offset:int = 1) -> str:
    result = ""
    for char in text:
        # Lowercase
        if "a" <= char <= "z":
            index = ord(char) - ord("a")
            index = (index + offset) % 26
            result += chr(index + ord("a"))
            continue

        # Uppercase
        if "A" <= char <= "Z":
            index = ord(char) - ord("A")
            index = (index + offset) % 26
            result += chr(index + ord("A"))
            continue

        # Others
        result += char
    
    return result

def caesar_decipher(text):
    result = ""

    for char in text:
        if char != " ":
            code = ord(char)  # transforme la lettre en nombre
            code -= 1           # soustrait 1
            if code < ord("A"): # si on dépasse A, on recommence au début
                code += 26
            result += chr(code)  # retransforme en lettre
    return result

print(caesar_decipher("KT d'ftu dppm !"))