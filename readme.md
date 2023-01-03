# FlashCards
Бэкенд для системы интервального повторения с помощью карточек.

## Требования
```
python 3.11
```

## Настройка
Создать базу, для posgtresql можно так:
```sql
CREATE USER cards WITH PASSWORD 'cardscards';
ALTER ROLE cards SET client_encoding TO 'utf8';  
ALTER ROLE cards SET default_transaction_isolation TO 'read committed';  
ALTER ROLE cards SET timezone TO 'UTC';

CREATE DATABASE flashcards owner cards;
GRANT ALL PRIVILEGES ON DATABASE flashcards TO cards;
```

Для запуска проекта необходимо настроить переменные окружения через `.env` файл в корне проекта:
```env
DEBUG=True
SECRET_KEY=4eb)rqaat8cj25bj+hom@9r2go#(a$hb@4*w4_8w-by=2)pv^y
DATABASE_URL=postgresql://cards:cardscards@127.0.0.1:15432/flashcards
```


## Запуск
```
python -m pip install -r requirements.txt
python manage.py migrate
```