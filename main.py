
import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def A(message):
    Id =message.chat.id
    Name = message.chat.first_name
    User = message.from_user.username
    A = types.InlineKeyboardMarkup(row_width = 1)
    B = types.InlineKeyboardButton(text = "دخول البوت",callback_data = "A")
    A.add(B)
    bot.send_message(message.chat.id, text = """
*➖ 👋اهلا .عزيزي*  [{}](tg://settings/)       
*➖ أيدك :* [{}](tg://settings/)            
*➖ يوزرك ان وجد :* @{}
*➖ قناه المبرمج :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*➖ المبرمج :* [Alosh](https://t.me/aaalaaa)""".format(Name,Id,User),parse_mode="markdown",disable_web_page_preview=True,reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def Hhh(call):
    if call.data == "A":
        A1(call.message)
def A1(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*✅ send User*",parse_mode='markdown')
@bot.message_handler(content_types=['text'])
def code(message):
     ali(message)
def ali(message):
    try:                
        msg  = message.text 
        url =(f"https://www.instagram.com/{msg}/?__a=1")
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 6.2; en-US; rv:1.9.0.20) Gecko/20170715 Firefox/37.0',
  'Cookie':'91a6c65102046ea491a6c65102046ea4'}
        req =requests.get(url, headers=head).json()  
        following =req['graphql']['user']['edge_follow']['count']
        id=req['graphql']['user']['id']
        name=req['graphql']['user']['full_name']
        followes = req['graphql']['user']['edge_followed_by']['count']             
        bot.send_message(message.chat.id, f"""
*✅ ᯓ تم سحب معلومات الحساب بنجاح*
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯* 
*ᯓ name :* {name}
*ᯓ 𝚄𝚂𝙴𝚁 :* {message.text}           
*ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 :* {followes}
*ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 :* {following}
*ᯓ 𝙸𝙳 :* {id}
*ᯓ ʟɪɴᴋ :* [Link](https://instagram.com/{message.text})
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯*
*Dv :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*By :* [Alosh](https://t.me/aaalaaa)   
                          """, parse_mode="markdown",disable_web_page_preview="true")
    except:
                 
         bot.send_message(message.chat.id, text=f"*Erorr User ! *",parse_mode="markdown")            
bot.polling()
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://alitools.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
