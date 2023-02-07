import random
import os

from dotenv import load_dotenv
import requests
import telebot
from bs4 import BeautifulSoup as bs

NUM = random.randint(0, 9)
PAGE = random.randint(1, 500)

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

URL_ANECDOT = 'https://www.anekdot.ru/random/anekdot/'
URL_ALLANECDOT = 'https://allanecdots.ru/page/'

answer = ['да', 'ещё', 'еще', 'хочу', 'дальше', 'ну', 'ну давай', 'давай',
          'допустим', 'наверно', 'наверное', 'удиви меня', 'допустим',
          'рискни', 'погнали']


def parser_anecdot(url):
    """Парсинг анекдотов с сайта anekdot.ru"""
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anecdots = soup.find_all('div', class_='text')
    anecdot = [c.text for c in anecdots]
    return anecdot[0]


def parser_allanecdot(url):
    """Парсинг анекдотов с сайта allanekdot.ru"""
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anecdots = soup.find_all('p', class_='anekdot_body')
    anecdot = [c.text for c in anecdots]
    return anecdot[NUM]


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    """Функция приветствия"""
    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name} !'
        'Меня зовут Бот-Анекдот! Хочешь анекдот?')


@bot.message_handler(content_types=['text'])
def get_anekdot(message):
    if message.text.lower() in answer:
        PAGE = random.randint(1, 500)
        bot.send_message(
            message.chat.id,
            parser_allanecdot(URL_ALLANECDOT + str(PAGE) + '/'))
    elif message.text.lower() == '/new':
        PAGE = random.randint(1, 500)
        bot.send_message(
            message.chat.id,
            parser_allanecdot(URL_ALLANECDOT + str(PAGE) + '/'))
    else:
        bot.send_message(
            message.chat.id,
            'Никто не хочет слушать мои анекдоты :(')


bot.polling()
