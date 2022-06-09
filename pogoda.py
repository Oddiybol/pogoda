import telebot
import requests
from googletrans import Translator

token = '5556193609:AAEA9oLzXx4UjYuaw8c5gSB-_DDYTH5F6gA'

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start', 'hi'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
@bot.message_handler(content_types='text')
def sendMessage(message): 
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    else:    
        bot.send_message(message.chat.id, message.text)
        # print(type(message))
    API_KEY = '6621546e1a94625a215c063e4320d66d'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data_dict = response.json()     # json - > dict

    icon_id = data_dict['weather'][0]['icon']
    print(icon_id)

    translator = Translator()
    w_cond = translator.translate(data_dict['weather'][0]['description'], dest='ru').text
    Weather = f"Погода в городе {message.text.title()}: {w_cond}"
    # Temperature in city Osh: 295.51
    temp = f"Температура в городе {message.text.title()}: {data_dict['main']['temp'] }°C"
    # Condition of weather in city Osh: Rain
    cond = translator.translate(data_dict['weather'][0]['main'], dest='ru').text
    condition_weather = f"Прогноз погоды в городе {message.text.title()}: {cond}"
    # feels_like
    feels_like = f"Температура в городе {message.text.title()} ощущается как: {data_dict['main']['feels_like'] }°C"
    # temp_min
    min_temp = f"Минимальная температура в городе {message.text.title()}: {data_dict['main']['temp_min'] }°C"
    # temp_max
    max_temp = f"Максимальная температура в городе {message.text.title()}: {data_dict['main']['temp_max'] }°C"

    bot.send_message(message.chat.id,f'{Weather} \n {temp}')
    # bot.send_message(message.chat.id,message.text.title())
    bot.send_image(message.chat.id,f'http://openweathermap.org/img/wn/{{icon_id}}@2x.png')
    
print('Бот запушен')
bot.infinity_polling()