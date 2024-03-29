# Мини-проект «Отображение курсов валют»

Это Django-приложение отображает курс валюты по отношению к рублю на заданную дату. Данные по валютам хранятся в базе данных приложения и обновляются ежедневно с использованием данных от Центрального Банка.

## Стек технологий

- Python
- Django
- Django Crontab

## Как запустить

Клонируем себе репозиторий:

```
git clone git@github.com:AnastasDan/currency_project.git
```

Переходим в директорию:

```
cd currency_project
```

Cоздаем и активируем виртуальное окружение:

* Если у вас Linux/MacOS:

    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас Windows:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

Устанавливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создаем файл .env и заполняем его. Список данных указан в файле env.example.

Выполняем миграции:

```
python manage.py migrate
```

Создаем суперпользователя:

```
python manage.py createsuperuser
```

Запускаем проект:

```
python manage.py runserver
```

## Настройка и запуск планировщика задач (Crontab)

В проекте используется `django-crontab` для автоматического выполнения задач по расписанию для сбора данных о курсах валют.

### Добавление задач в Crontab

Чтобы добавить задачи в системный crontab, выполните команду:

```
python manage.py crontab add
```

### Проверка и удаление задач

- Чтобы проверить текущие задачи crontab:

```
python manage.py crontab show
```

- Чтобы удалить задачи из crontab:

```
python manage.py crontab remove
```

### Настройка времени выполнения задачи

В `CRONJOBS` время задается в формате cron, который состоит из пяти полей:

- Минута (от 0 до 59)
- Час (от 0 до 23)
- День месяца (от 1 до 31)
- Месяц (от 1 до 12)
- День недели (от 0 до 6, где 0 - это воскресенье)

Пример: `'0 3 * * *'` означает, что задача будет выполняться каждый день в 3:00 утра.

- `0 3` - в 3 часа ночи и 0 минут
- `* * *` - каждый день, каждый месяц, каждый день недели

### Ручной запуск команды

```
python manage.py load_data
```

## Как запросить курс валюты

### **Получение курса валюты**

Отображает курс выбранной валюты по отношению к рублю на заданную дату.

**Параметры:**

  - `charcode` (код валюты, например, "USD", "EUR").
  - `date` (дата в формате ГГГГ-ММ-ДД, например, "2024-01-01").

**Пример использования:**

  ```
  http://localhost:8000/rate/?charcode=AUD&date=2024-01-01
  ```

## Автор мини-проекта

[Anastas Danielian](https://github.com/AnastasDan)