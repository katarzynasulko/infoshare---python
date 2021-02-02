import re

haslo = input('Podaj haslo: ')

if not re.search('[a-z]', haslo):
    print('Nie zawiera malej litery')

if not re.search('[A-Z]', haslo):
    print('Nie zawiera wielkiej litery')

if not re.search('[0-9]', haslo):
    print('Nie zawiera cyfry')

if not(any(not letter.isalnum() for letter in haslo)):
    print('Nie zawiera znakow specjalnych')

if not(len(haslo) > 8 and len(haslo) < 64):
    print('Haslo musi zawierac od 8 do 64 znakow')