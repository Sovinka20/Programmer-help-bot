import os
from dotenv import load_dotenv
import telebot
import psycopg2

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение секретов из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Проверка наличия всех необходимых переменных окружения
if not all([TELEGRAM_BOT_TOKEN, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    raise ValueError("Не все необходимые переменные окружения установлены")

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Подключение к базе данных PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
except psycopg2.Error as e:
    print(f"Ошибка подключения к базе данных: {e}")
    exit()

# Создание таблицы keywords, если она не существует
create_table_query = """
CREATE TABLE IF NOT EXISTS keywords (
    id SERIAL PRIMARY KEY,
    keyword TEXT NOT NULL UNIQUE,
    info TEXT NOT NULL
);
"""

# Вставка данных в таблицу keywords, если они ещё не существуют
insert_data_query = """
INSERT INTO keywords (keyword, info) VALUES
('react', 'Информация по React:\n\n1. Создание проекта:\n   npx create-react-app my-app\n\n2. Установка библиотек:\n   npm install react-router-dom\n   npm install axios\n\n3. Запуск проекта:\n   npm start'),
('python', 'Информация по Python:\n\n1. Установка Python:\n   sudo apt-get install python3\n\n2. Создание виртуального окружения:\n   python3 -m venv myenv\n\n3. Активация виртуального окружения:\n   source myenv/bin/activate'),
('sourcetree', 'Информация по SourceTree:\n\nСброс настроек по адресу C:\\Users\\<User>\\AppData\\Local\\Atlassian\\SourceTree.exe')
ON CONFLICT (keyword) DO NOTHING;
"""

try:
    cursor.execute(create_table_query)
    cursor.execute(insert_data_query)
    conn.commit()
except psycopg2.Error as e:
    print(f"Ошибка при создании таблицы или вставке данных: {e}")
    conn.rollback()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот-справочник. Напиши мне ключевое слово, и я дам тебе информацию.')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    try:
        # Запрос к базе данных с использованием LIKE для частичного поиска
        cursor.execute("SELECT info FROM keywords WHERE keyword LIKE %s", (f"%{text}%",))
        result = cursor.fetchone()
        
        if result:
            response = result[0]
        else:
            response = "К сожалению, я не знаю такого ключевого слова."
        
        bot.reply_to(message, response)
    except psycopg2.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        bot.reply_to(message, "Произошла ошибка при обработке вашего запроса.")

# Запуск бота
bot.polling()

# Закрытие соединения с базой данных после завершения работы бота
cursor.close()
conn.close()