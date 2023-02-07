## Telegram-бот, присылающий анекдоты по запросу в рандомном порядке. Выполнен парсинг анекдотов с двух сайтов.

### Технологии
- Python 3.9
- python-dotenv 0.19.0
- beautifulsoup4==4.11.2
- pyTelegramBotAPI==4.10.0
- requests==2.28.2

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/GeorgeMish/anecdote_bot.git
```

```
cd anecdote_bot/
```
- Установите и активируйте виртуальное окружение:

```
python3.9 -m venv venv
```
```
source venv/bin/activate
```

- Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создайту файл .env в этой директории и укажите собственные токены:

```
TELEGRAM_TOKEN = токен вашего бота Telegram полученный от BotFather.
```

### Получение токенов:

Зарегистрируйте бота в BotFather:<br>
<a href="https://t.me/BotFather" target="_blank">Регистрация бота и получение токена</a>


- Запуститe проект:

```
python3 anecdote_bot
```

### Автор проекта:
Юрий Мишкевич
