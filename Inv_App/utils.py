import sys
sys.path.append('/c:/Users/User/Desktop/nebs-Invoice/Hq_Invoice/Inv_App/')

from telegram import Bot

def send_to_telegram(data):
    # Replace 'YOUR_BOT_TOKEN' with the actual token obtained from BotFather
    bot = Bot(token='6489391169:AAH1w_BoSEejQ8--1OBkmqU29OqLZzsYgzs')
    
    # Replace 'YOUR_CHAT_ID' with the actual chat ID where you want to send the message
    chat_id = '@pysenberg'
    
    message = f"New form submission:\n{data}"

    # Send the message to Telegram
    bot.send_message(chat_id=chat_id, text=message)
