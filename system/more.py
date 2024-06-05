"""
Pазбивает строку или текстовый файл на страницы для интерактивного просмотра
"""


def more(text: str, numlines=15):
    lines = text.splitlines()  # подобно split(‘\n’) но без ‘’ в конце
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input("More? ") not in ['y', 'Y']:
            print(f'\n\n{"Breaking!!!":-^82}')
            break


if __name__ == '__main__':
    import sys  # если запускается как
    more(open(sys.argv[0]).read(), 10)  # отобразить постранично содержимое
                                                # файла, указанного в командной строке
