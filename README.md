# 🚀 Учебный проект на Django

Учебный проект для освоения Django и современных веб-технологий.

## 🔍 Описание

Проект представляет собой систему управления клиентами с реализацией ключевых возможностей Django и смежных технологий.

## 🛠️ Функционал

### Основные возможности
- ✅ Полный CRUD функционал
- 📊 Администрирование через Django Admin
- 📱 Адаптивный интерфейс (Bootstrap 5)
- ⚡ Динамические элементы (jQuery)

### Дополнительные системы
- 🕒 Фоновые задачи (Celery)
- ⏰ Периодические задачи (Celery Beat)
- 📨 Очереди сообщений (Redis/RabbitMQ)
- 🔌 REST API (DRF)

## 🧰 Технологический стек

| Категория       | Технологии             |
|-----------------|------------------------|
| Бэкенд         | Python 3, Django 4     |
| Асинхронность  | Celery, Redis, RabbitMQ |
| Фронтенд       | Bootstrap 5, jQuery    |
| API            | Django REST Framework  |
| База данных    | PostgreSQL             |

## 🚀 Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/billy-juicy/Django-Utilities-App.git
cd Django-Utilities-App

# 2. Настроить виртуальное окружение
python -m venv venv
venv\Scripts\activate     # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настройка окружения
cp .env.example .env
# заполнить .env файл

# 5. Миграции
python manage.py migrate

# 6. Запуск
python manage.py runserver

## Для Celery в отдельном терминале

# Celery worker
celery -A config worker -l info

# Celery beat
celery -A config beat -l info