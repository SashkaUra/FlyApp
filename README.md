# FlyApp

Добро пожаловать в приложение Flyhack, при помощи которого Вы сможете получить всю нужную информацию обо всех аэропортах в мире! 
Интерфейс приложения включает в себя две вкладки: "Find airports" и "Map".
Во вкладке "Find airports" Вы сможете получить информацию об аэропортах на интересующей Вас территории, задав ее координаты (широта от -90 до 90 и долгота от -180 до 180) 
и скачать csv файл для дальнейшей работы с нужными данными.
Во вкладке "Map" есть поле для ввода интересующего Вас города (на английском языке). После нажатия кнопки Search на карте отобразится интересующий Вас город.
После нажатия кнопки Show airport на карте отобразятся все аэропорты этого города. Примечание: иногда после нажатия этой кнопки необходимо изменить масштаб карты, чтобы увидеть аэропорты, поскольку многие аэропорты находятся далеко за пределами черты города.
Поменять масштаб можно при помощи + или - на карте или прокрутив колесико компьютерной мышки.

Прежде чем приступить к запуску приложения Вам необходимо сделать следующее.

1. Осуществить подключение к базе данных.
Данное приложение работает с базой данных MySQL. Дамп файл с базой данных также расположен в данном репозитории и называется data_dump.sql, с которым можно работать через MySQL Workbench, например.
Чтобы установить соединение Вам необходимо ввести Ваши параметры подключения в файле config.py: host, user name и password.
Также в файле data_base_query.py введите нужное название базы данных в переменной db_name.

2. Создать виртуальное окружение для данного проекта.
2.1 Скачайте все файлы из данного репозитория на Ваш компьютер в отдельный католог. 
2.2 При помощи модуля venv, который входит в стандартную поставку Python 3, создайте виртуальное окружение для данного каталога.
2.3 При помощи командной строки выполните установку следующих пакетов:
   - MySQL Connector/Python: pip install mysql-connector-python
   - пакет для отображение карты tkintermapview: pip install tkintermapview    

3. Запустите приложение через файл FlyApp.py.

