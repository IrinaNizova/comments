Эта программа с помощью кастомной команды django принимает данные из socket’a. Данные должны быть в формате json, содержать ключи name и  comment. Пример клиента, который шлёт сообщения находтся в файле client.py. Пример запуска: python client.py localhost '{"name":"ira","comment":"go with he"}'. Получив сообщение, программа сохраняет его в базу данных. Содержимое таблицы выводится на страницу по адресу http://127.0.0.1:8000/ (при запущеном django-сервере)

Чтобы программа заработала надо установить нужные библиотеки: pip install -r requirements.txt
создать в mysql базу с названием comments
в файле comments/settings.py в блоке DATABASES прописать юзера и пароль для базы
сделать команды python manage.py makemigrations и python manage.py migrate чтобы создалась таблица в базе данных
затем запустить команду python manage.py waitmessages
после этого запустить сервер django python manage.py runserver
