import cgi


form = cgi.FieldStorage()               # парсинг данных формы
print("Content-type: text/html\n")      # http-заголовок плюс пустая строка
print('<title>REPLY</title>')           # html-разметка ответа
if not 'user' in form:
    print('<h1>Who are you?<h1>')
else:
    print(f'<h1>Hello <i>{cgi.escape(form["user"].value)}</i>!</h1>')

