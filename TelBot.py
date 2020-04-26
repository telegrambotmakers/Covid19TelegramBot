import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler,BaseFilter
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,MessageEntity
#import logging
import requests
import json
import configparser as cfg
from urllib.parse import urlparse

class Filtercovid(BaseFilter):
    def filter(self, message):
        return 'covid' in message.text.lower()

# Remember to initialize the class.
Filter_covid = Filtercovid()

config = 'config.cfg' # Telegram Token
tokenKey = read_token_from_config_file(config)

bot=telegram.Bot(token= tokenKey)
updater = Updater(token= tokenKey)

#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#Function to start the bot,initiated on /start command
def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi, I am AZ Covid19 Bot')

def covidText(bot,update):
    button_labels = [['Yes'], ['No']]
    reply_keyboard = telegram.ReplyKeyboardMarkup(button_labels)
    bot.send_chat_action(chat_id=update.effective_user.id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,text='Do You need any information about COVID19?',reply_markup=reply_keyboard)

def covidYesNo(bot,update):
    
    print("message sent by user",update.message.text)
    if update.message.text == 'Yes':
        covidYes(bot,update)
    elif update.message.text =='No':
        covidNo(bot,update)
        
def covidNo(bot,update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=update.message.chat_id,text="ok, thank You",reply_markup=reply_markup)

def covidYes(bot,update):
    #print("inside covidYes")
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=update.message.chat_id,text="Thank You! We will help you:",reply_markup=reply_markup)
    button_list=[
            InlineKeyboardButton('Symptoms',callback_data='SYS'),
            InlineKeyboardButton('Country Based',callback_data='COU')]
    reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=2))
    #update.message.reply_text("Please choose from the following : ",reply_markup=reply_markup)
    bot.send_message(chat_id=update.message.chat_id, text='Please choose from the following',reply_markup=reply_markup)

def Btn_Query_Back(bot,update):
    #print("inside Btn_Query_Back")
    query=update.callback_query
    bot.send_chat_action(chat_id=update.effective_user.id,action=telegram.ChatAction.TYPING)

    if update.callback_query.data == 'SYS':
        bot.edit_message_text(text="https://www.who.int/news-room/q-a-detail/q-a-coronaviruses#:~:text=symptoms",chat_id=query.message.chat_id,message_id=query.message.message_id)
        
    elif update.callback_query.data == 'COU':
        bot.edit_message_text(text="Please enter the country Name",chat_id=query.message.chat_id,message_id=query.message.message_id)

def covidCountry(bot,update):
    #print("country sent by user",update.message.text)
    if IsValidCounrty(update.message.text):
        Detail_str = FetchCountryDetails(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=Detail_str)
    else:
        #bot.send_message(chat_id=update.message.chat_id, text='Please enter a valid Country')
        pass
#----------------------------------------------------------------------------------------------------------

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds', 'token')

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
    
def IsTrustedURL(bot,update):
    #print("URL sent by user",update.message.text)
    # JSON file 
    f = open ('trustedURL.json', "r")   
    # Reading from file 
    data = json.loads(f.read()) 
    # Closing file 
    f.close()
    parsed_uri = urlparse(update.message.text)
    uri = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)	
	
    if data and uri in data: # test for emptiness and for membership
        bot.send_message(chat_id=update.message.chat_id, text="This news is from a trusted source" )
    else:
        bot.send_message(chat_id=update.message.chat_id, text="This news is not from a trusted source" )


def IsValidCounrty(Counrty_Name):
    # JSON file 
    f = open ('ValidCountry.json', "r")  
    # Reading from file 
    data = json.loads(f.read()) 
    # Closing file 
    f.close()
    if data and Counrty_Name.title() in data: # test for emptiness and for membership
        return True
    else:
        return False

def FetchCountryDetails(country):
    import urllib.request, json 
    with urllib.request.urlopen("http://api.coronatracker.com/v3/stats/worldometer/country") as url:
        data = json.loads(url.read().decode())
    out_str = ''
    Header = "country totalConfirmed totalDeaths totalRecovered"
    length = len(data) 
    for i in range(length): 
        str = json.dumps(data[i])
        res = json.loads(str) 
        if res.get("country").lower() == country.lower():
            for x, y in res.items():
                if x in Header:
                    out_str = out_str + "{} : {} \n".format(x.title(), y)
            print(out_str)
            return out_str
    
def main():
    updater.dispatcher.add_handler(CommandHandler('start',start))

    #covid19 URL
    url_handler = MessageHandler(Filters.text & Filter_covid & (Filters.entity(MessageEntity.URL) | Filters.entity(MessageEntity.TEXT_LINK)),IsTrustedURL)
    updater.dispatcher.add_handler(url_handler)

    #covid19 Text
    covidText_handler = MessageHandler(Filters.text & Filter_covid,covidText)
    updater.dispatcher.add_handler(covidText_handler)
    
    #covid19 Yes or No
    updater.dispatcher.add_handler(MessageHandler(Filters.text, covidYesNo),group=0)

    #covid19 Country
    updater.dispatcher.add_handler(MessageHandler(Filters.text, covidCountry),group=1)
    
    updater.dispatcher.add_handler((CallbackQueryHandler(Btn_Query_Back)))
    updater.start_polling()

main()
