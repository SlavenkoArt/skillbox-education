
text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))

alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]

new_text = [alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
           if letter in alphabet else letter for letter in text.lower()]

print(''.join(new_text))