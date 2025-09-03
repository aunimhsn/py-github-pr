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