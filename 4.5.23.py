"""Структура архива 🌶️🌶️
Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую
структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив
имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB"""

from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'
with ZipFile('desktop.zip', 'r') as zip_open:
    file = zip_open.infolist()
    for f in file:
        string = f.filename
        space = (string.count('/')-1) * '  '

        if f.is_dir():
            print_line = f.filename.split('/')[-2]
            print(f'{space}{print_line}')
        else:
            print_line = f.filename.split('/')[-1]
            space = (string.count('/')) * '  '
            print(f'{space}{print_line} {convert_bytes(f.file_size)}')