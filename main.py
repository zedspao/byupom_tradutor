#!/usr/bin/env python3

frase = input("insira a frase: ")
frase = list(frase)

for i in range(len(frase)):
  if((ord(frase[i]) == 32)):
    frase[i] = " "
  elif ((ord(frase[i])- 96)) % 2 != 0:
    frase[i] = "."
  elif ((ord(frase[i])- 96)) % 2 == 0:
    frase[i] = "-"

frase_string = ''.join(frase)

morse_dict = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..'
}

def decifrar_morse(frase_string):
  msg = ''
  frase_string = frase_string.split(' ')
  for cod in frase_string:
    for bla, mors in morse_dict.items():
      if mors == cod:
        msg += bla
  return msg

texto = decifrar_morse(frase_string)
print(texto)
