
import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from InstagramIG import * 
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
    B = types.InlineKeyboardButton(text = "✅ صنع حساب",callback_data = "A")
    A.add(B)
    bot.send_message(message.chat.id, text = """
➖* 👋اهلا عزيزي*  [{}](tg://settings/)       
➖ *في بوت صنع حساب في استظافه*
➖ [Pythonanywhere](pythonanywhere.com)
*➖ أيدك :* [{}](tg://settings/)            
*➖ يوزرك ان وجد :* @{}
*➖ قناه المبرمج :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*➖ المبرمج :* [Alosh](https://t.me/aaalaaa)
""".format(Name,Id,User),parse_mode="markdown",disable_web_page_preview=True,reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def Hhh(call):
    if call.data == "A":
        A1(call.message)     
def A1(message):
	bot.send_message(message.chat.id,text="*✅ انتظر قليلآ جاري انشاء حساب*",parse_mode="markdown")
	a = 'djch102983645bdsndcjhbsndcjvh876tyu7654rt'
	user = ''.join(random.choice(a)for j in range(5))
	paas = ''.join(random.choice(a)for j in range(8))
	g=''.join(random.choice(a)for j in range(7))
	email =g+"@gmail.com" 
	url = 'https://www.pythonanywhere.com/registration/register/beginner/'
	hrs ={

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0', 
'Connection':'keep-alive', 
'Content-Length':'204',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'cookie_warning_seen=True; _ga=GA1.1.9823633.1642061837; _gid=GA1.1.1147915189.1642061837; csrftoken=sufjNFCDOqA0xy3LiA6GR94raYWbTfiHrbdnwTTRUpC0DRHiIL2P7XWeWdZFr8rI; sessionid=e42falh0airkxirkbo04473ne1xindkf',
'Host':'www.pythonanywhere.com',
'Origin':'https://www.pythonanywhere.com', 
'Referer':'https://www.pythonanywhere.com/registration/register/beginner/',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"', 
'Sec-Fetch-Dest':'document', 
'Sec-Fetch-Mode':'navigate', 
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',}
	da = {
'csrfmiddlewaretoken':'T3fVafK0liWb0oVMO90Uwz81NmOOJQQ9SKdZTt1erhYb6HzjekW3Mn0OzBRihJZa',
'username':user,
'email': email,
'password1':paas,
'password2':paas,
'tos':'on',
'recaptcha_response_token_v3':'',}
	re = requests.post(url,headers=hrs,data=da).text
	bot.send_message(message.chat.id,text=f"""
*✅ تم صنع استظافتك في نجاح √ *
⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯
➖ *User* : `{user}`
➖ *Email* : `{email}`
➖ *Pass* : `{paas}`
➖ [Open Hosting Pythonanywhere](pythonanywhere.com)
⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯
*➖ قناه المبرمج :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*➖ المبرمج :* [Alosh](https://t.me/aaalaaa)
*➖ بمساعده :* [𝖠 - Kabos<\>](https://t.me/NnKoNn)""",parse_mode="markdown",disable_web_page_preview=True)
bot.polling()
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://pythonaali.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
