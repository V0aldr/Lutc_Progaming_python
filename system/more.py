"""
Pазбивает строку или текстовый файл на страницы для интерактивного просмотра
"""


def more(text: str, numlines=15):
    lines = text.splitlines()  # подобно split(‘\n’) но без ‘’ в конце
    page_number = 1
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        print(f"\n{page_number:-^82}\n")
        for line in chunk:
            print(f"{line}")
        page_number += 1
        if not lines:
            print(f'\n{"END":-^82}\n')
            break
        print(f"\nNEXT PAGE {page_number}\n".center(82))
        if lines and input("More? ") not in ['y', 'Y', ' ']:
            print(f'\n\n{"Breaking!!!":-^82}')
            break


if __name__ == '__main__':
    import sys  # если запускается как

    more(open(sys.argv[0]).read(), 10)  # отобразить постранично содержимое
    # файла, указанного в командной строке
