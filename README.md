Название
Платформа для трейдинга для анализа курсов кросс пар

Описание (краткое описание)

Программа позволяет анализировать курсы кросс пар на историческом интервале с 2006 по 2024 годы.В программе реализован интерактивный интерфейс для просмотра графиков валютных пар. Для заданного временного интервала и выбранной пары можно вывести график фьючерсов. 
UI - интерфейс позволяет пользователям построить свою стратегию в трейдинге анализируя графики на истории.

Используемые технологии
 - Python 3.11
 - Matplotlib
 - Pandas
 - Tkinter 
 - Pydantic

Схема программной реализации (детально по блокам или по шагам)

Программа разделена на 3 логические части
1. Обработка данных пользвательского запроса
2. Отправка данных в БД
3. Отображение данных в UI

Первая часть посвящена обработки пользовательского ввода и формированию json. Также здесь предусмотрена обработка ошибок на pydantic.
Вторая часть - запрос к API Alpha Vantage для получения данных о курсах валют. 
Третья часть предусматривает построение и отображение результатов вывода на окно пользовательского интерфейса.


Схема запуска программы (Windows or Linux)
1. Склонровать репозиторий
git clone https://github.com/
cd ...

2. Содание виртуального окружения и активация
python -m venv venv
source env/bin/activate

3. Установка всех зависимостей. 
pip install -r requirements.txt

4. Запуск проекта.
python main.py


Лицензия (MIT License)
MIT

Авторы и контакты:
To contact the author, write to the following email A7010020@yandex.ru








