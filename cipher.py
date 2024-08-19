your_message = input("Message you want encrypted: ")
encrypted_message = []

## Shift lower case letters 5 spots
def lowercase(char):
    if 'a' <= char <= 'z':  
        shift = 5
        if ord(char) + shift > ord('z'):
            shift -= 26
        return chr(ord(char) + shift)
    return char

## Shift upper case letters 5 spots
def uppercase(char):
    if 'A' <= char <= 'Z':  
        shift = 5
        if ord(char) + shift > ord('Z'):
            shift -= 26
        return chr(ord(char) + shift)
    return char

## Encryption
for z in your_message:
    if z == " ":
        encrypted_message.append(z)
    elif 'A' <= z <= 'Z':
        encrypted_message.append(uppercase(z))
    elif 'a' <= z <= 'z':
        encrypted_message.append(lowercase(z))

result = ''.join(encrypted_message)

print(result)

