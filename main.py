import mysql.connector
import telebot
from dotenv import load_dotenv
from handler import Handler
from repository import Repository
from servises import Service
import os


load_dotenv()
connection = mysql.connector.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                              host=os.getenv("DB_HOST"),
                              database=os.getenv("DB_NAME")) 
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

repository = Repository(connection)
servises = Service(repository)
handler = Handler(bot, servises)
if __name__ == "__main__":
    handler.run()
