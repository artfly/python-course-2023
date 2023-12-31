# Задание 6

### 1. Pysearch (6 баллов)

Напишите программу, которая будет искать строки с заданной подстрокой в указанном файле 

Пример работы программы:
```
> python3 src/main.py test.txt he
< 
Found file: ./tests/test.txt
1: hello
3: hehe
```

#### 1.1 Cтруктура проекта

Создайте проект под управлением [pipenv](https://pipenv.pypa.io/en/latest/). В зависимости добавьте [pytest](https://docs.pytest.org/en/7.4.x/).
У вас должна получиться вот такая структура проекта:  
```
- src
  - main.py
  - find.py
  - grep.py
- tests
- Pipfile
- Pipfile.lock
```

#### 1.2 find

В файле `find.py` напишите функцию find. Она:
- принимает на вход название файла
- ищет такой файл начиная с текущей директории вглубь (проверяет полное совпадение имени)
- если находит, то возвращает полный путь до этого файла
- если нет, то возвращает `None`

Для поиска файла начиная с текущей директории можно воспользоваться функцией [os.walk](https://docs.python.org/3/library/os.html#os.walk)  
С тем, как она работает, рекоммендуется ознакомиться сначала самостоятельно, потом спросить непонятные моменты

#### 1.3 grep (FileLines)

В файле `grep.py` напишите класс `FileLines`. Он:
- в конструкторе (в методе `__init__`) получает список строк и запоминает себе в аттрибуты
- определяет метод `__iter__` этот метод возвращает другой класс - `Iter`, который является итератором по списку строк (определяет метод `__next__`)

#### 1.4 grep

В файле `grep.py` напишите функцию grep. Она принимает на вход путь до файла и подстроку, которую нужно искать в этом файле.  
В самой функции:
  - открываем файл для чтения, смотрим в нем строки одна за другой
  - если строка содержит в себе данную подстроку, то запоминаем эту строку в список в формате `номер_строки: содержимое_строки`
  - возвращаем из функции объект класса `FileLines`, который проинициализирован списком с нумерованными строками

#### 1.5 main

В файле `main.py` напишите функцию `main`. Эта функция ничего не принимает на вход.  
В самой функции:
- проверить, сколько аргументов подали на вход скрипту. чтобы получить их количество можно воспользоваться [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
  - если их 3 штуки, то записать их в переменные (на первой позиции - имя скрипта, на второй - имя файла, в котором искать, на третьем - подстрока)
  - если их другое количество, то напечатать ошибку в sys.stderr и завершить программу (`print("ваше сообщение", file=sys.stderr)`, `sys.exit(1)`)
- вызвать функцию find из `find.py` (не забудьте про импорты!). если она вернула `None`, то показать ошибку и завершить программу (аналогично предыдущему пункту)
- напечатать на экран `Found file: имя_файла`
- в цикле итерироваться по строкам, полученным после вызова `grep` из `grep.py`. Напечатать все строки  

Вызовите `main` из под условия `if __name__ == "__main__":`