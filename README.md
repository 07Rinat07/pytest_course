<div align="center">
  <img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" width="600" height="300"/>
</div>

### Тестирование - PYTEST
#### Подготовка окружения
* или с файла установить сразу зависимости
* pip install  -r .\requirements.txt
* py -m venv venv
* .\venv\Scripts\activate
*  pip install pytest    
#### Со всего проекта берет все установленные зависимости в файл для последующей установки например через Docker.
* pip freeze > requirements.txt

### Описание логики приложения
* Запуск проекта:
* Убедитесь, что данные в .env файлах правильные
* Создайте таблицу candies в БД:
 CREATE DATABASE candies;
* Создайте виртуальное окружение и активируйте его:
python3 -m venv .venv
source .venv/bin/activate - Linux
.\venv\Scripts\activate.ps1 - Windows
* Установите зависимости из requirements.txt:
pip install -r requirements.txt
* Запустите миграции:
alembic upgrade head
* Теперь можно запускать проект: python3 src/main.py