import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text, shift_amount, action):
    cipher_text = ""
    shifted_position = 0
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            if action=="encode":
                shifted_position = alphabet.index(letter) + shift_amount
            elif action=="decode":
                shifted_position = alphabet.index(letter) - shift_amount
            else:
                print(f"Invalid action: {action}")
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {action}d result: {cipher_text}")

should_continue=True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(original_text=text, shift_amount=shift, action=direction)

    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue=False
        print("Goodbye!")