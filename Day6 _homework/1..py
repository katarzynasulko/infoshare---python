import csv
from collections import defaultdict


def add_contact(contact_book, person):
    contact_book[person['nazwisko']].append(
        {
            'imie': person['imie'],
            'nazwisko': person['nazwisko'],
            'tel': person['numer'],
            'miasto': person['miasto'],
            'ulica': person['ulica'],
            'nr_domu': person['nr']
        }
    )

def export_to_csv(header, contact_book, filename='contacts.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for last_name in contact_book:
            for person in contact_book[last_name]:
                writer.writerow(person.values())


def import_from_csv(filename='adresy.csv', delimiter=','):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        contacts = defaultdict(list)

        for line in reader:
            add_contact(contacts, line)

        return contacts, reader.fieldnames


def search(contact_book, firstname, lastname):
    people = contact_book[lastname]
    for person in people:
        if firstname == person['imie']:
            return person['tel']


def search_person(contact_book, firstname, lastname):
    people = contact_book[lastname]
    for person in people:
        if firstname == person['imie']:
            return person


contact_book, header = import_from_csv(delimiter=';')  # -> (contacts, ['imie', 'nazwisko'])
tel = search(contact_book, 'Adam', 'Mickiewicz')
print('Nr telefonu Anny Nowak: ', tel)

imie = input('Podaj imię do zmiany: ')
nazwisko = input('Podaj nazwisko do zmiany: ')
tel = input('Podaj nowy numer telefonu: ')

person_to_update = search_person(contact_book, imie, nazwisko)
print('Znalazlam obiekt do zmiany: ', person_to_update)

person_to_update['tel'] = tel

contact_book.update(person_to_update)

print('Nowy numer telefonu dla', imie, nazwisko, 'to:', tel)

print('Zaktualizowany obiekt: ', contact_book[nazwisko])

tel = search(contact_book, imie, nazwisko)

print('Nr telefonu', imie, nazwisko, 'to', tel)