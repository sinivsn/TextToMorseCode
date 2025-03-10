morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',  
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',  
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',  
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',  
    'Z': '--..',  
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',  
    ' ': '/'  # Space between words
}

input_text = input("Enter the text in English to convert to MORSE code - ")

print(f"The text entered - {input_text}" )

temp_text = input_text

input_text = input_text.upper()

morse_code = ""

for letter in input_text:

    morse_letter = morse_dict[letter]
    morse_code = morse_code+morse_letter

print(f"The Norse Code for the text {temp_text} is {morse_code}")