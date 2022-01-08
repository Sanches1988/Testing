documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name_people(documents):
    doc_number = input('Введите номер документа: ')
    for doc in documents:
        if doc_number == doc['number']:
            return doc['name']
    return f'Введённый Вами № {doc_number} в каталоге докуметов отсутсвует.'


def get_shelf_number(doc_number):
    doc_number = input('Введите номер документа: ')
    for shelf in directories:
        if doc_number in directories[shelf]:
            return f'Указанный Вами документ находится на полке № {shelf}'
    return f'Указанный Вами документ № {doc_number} на полках отсутствует.'


def get_list_docs():
    print('Список всех документов:\n')
    for current_document in documents:
        get_list_docs(current_document)


def add_new_doc(documents, directories):
    typ = input("Укажите тип документа: ")
    number = input("Укажите номер документа: ")
    name = input("Укажите имя: ")
    new_dct = {'type': typ, 'number': number, 'name': name}
    documents.append(new_dct)
    shelf = input("укажите номер полки: ")
    for k in directories.items():
        if shelf in k:
            directories[shelf].append(number)
            break
    else:
        print('Такой полки не существует')
    return documents, directories


def main(documents, directories):
    cmd = str(input("Введите команду: "))
    if cmd == 'p':
        return (print(get_name_people(documents)))
    elif cmd == 's':
        return (print(get_shelf_number(directories)))
    elif cmd == 'l':
        return get_list_docs(documents)
    elif cmd == 'a':
        return (print(add_new_doc(documents, directories)))
    else:
        print("Вы ввели не верную команду")


main(documents, directories)















