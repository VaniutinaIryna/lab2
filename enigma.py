import sys
operation = input()
shift = int(input())

rotors = []
for i in range(3):
    rotors.append(input())

message = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if operation == "ENCODE":
    caesar_text = ""
    for i in range(len(message)):
        letter = message[i]
        old_index = alphabet.index(letter)
        new_index = (old_index + shift + i) % 26
        caesar_text += alphabet[new_index]

    
    current_text = caesar_text
    for rotor in rotors:
        next_text = ""
        for letter in current_text:
            idx = alphabet.index(letter)
            next_text += rotor[idx]
        current_text = next_text

    print(current_text)

else:  
    current_text = message
    for rotor in reversed(rotors):
        next_text = ""
        for letter in current_text:
            idx = rotor.index(letter)
            next_text += alphabet[idx]
        current_text = next_text

    original_text = ""
    for i in range(len(current_text)):
        letter = current_text[i]
        old_index = alphabet.index(letter)
        new_index = (old_index - (shift + i)) % 26
        original_text += alphabet[new_index]

    print(original_text)
