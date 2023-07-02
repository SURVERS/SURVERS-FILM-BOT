import time
import telebot
from telebot import types


API_TOKEN = 'СЮДА ПИСАТЬ ТОКЕН БОТА' # telegram
bot = telebot.TeleBot(API_TOKEN)

print('\n')
print('===================================================')
print('               SURVERS FILM BOT v1.1               ')
print('             Создатель: SURVERS FAMILY             ')
print('     ВК: @vladkorobov Telegram: @surversfamily     ')
print('       Бот запущен, приятного использования :3     ')
print('===================================================')
print('\n')

CodeFilms = [
    ['0', 'Вино'], ['1', 'ОТ SPC не убежишь'], ['2', 'Бог это баг?'], ['3', 'лорды раздевалок'], 
    ['4', 'Здравствуйте, вам пора!'], ['5', 'Эскобар'], ['6', 'Солдаты'], ['7', '911 служба спасения'],
    ['8', 'Меню (2022 год)'], ['9', 'ДЕВУШКИ С МАКАРОВЫМ 3'], ['10', 'Жадность (2019)'], ['11', 'Зомбилэнд 2'],
    ['12', 'Сын отца народов (2013)']]

def print_bot(text):
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)
    return print(f'[{time_string}]: {text}')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    ButtonOpenURL_One = types.InlineKeyboardButton('Подписаться на GUMBALL FAMILY || ОБОИ, ОБРАБОТКИ (Удивительный Мир Гамбола)', url='https://t.me/gumball_family')
    ButtonCheck = types.InlineKeyboardButton("Проверить подписки", callback_data='checksubc')
    markup.add(ButtonOpenURL_One)
    markup.add(ButtonCheck)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Для того чтобы узнать название фильма, ты должен подписаться на каналы. После подписки, нажмите кнопку 'Проверить Подписки', если всё верно, вы сможете ввести код фильма. Желаем удачи :3".format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    user_id = message.chat.id
    channel_id = '@gumball_family'
    response = bot.get_chat_member(channel_id, user_id)

    if response.status == 'member' or response.status == 'creator':
        if message.text in [element for a_list in CodeFilms for element in a_list]:
            print_bot(f'Пользователь {message.chat.first_name} {message.chat.last_name} (id {user_id}) запросил название фильма. Код: {message.text}.')
            result_film = '🔥 Фильм - "' + CodeFilms[int(message.text)][1] + '"\nКуча интересных фильмов доступно тут: https://www.youtube.com/channel/UCV_NfrcNrvaTpIsgJS058rg\nСпасибо что вы пользуетесь нашим ботом :3'
            return bot.send_message(user_id, result_film)
        else:
            bot.send_message(user_id, 'Код фильма не найден!')
    else:
        bot.send_message(user_id, 'Вы не подписаны на нужные каналы, подпишитесь, и проверьте еще раз')
        print_bot(f'Пользователь {message.chat.first_name} {message.chat.last_name} (id {user_id}) не успешно запросил название фильма. Причина: Не подписан на один из каналов. Код: {message.text}.')
        start(message)
    
# >> Обработчики:
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    if req[0] == 'checksubc': # Проверка подписки
        user_id = call.message.chat.id
        channel_id = '@gumball_family'
        response = bot.get_chat_member(channel_id, user_id)

        if response.status == 'member' or response.status == 'creator':
            bot.send_message(user_id, 'Вам был предоставлен доступ к кодам, теперь можете вписать ниже код фильма, и получить название фильма: ')
            print_bot(f'Пользователь {call.message.chat.first_name} {call.message.chat.last_name} (id {user_id}) получил доступ к кодам!')
        else:
            bot.send_message(user_id, 'Вы не подписаны на нужные каналы, подпишитесь, и проверьте еще раз')
            print_bot(f'Пользователь {call.message.chat.first_name} {call.message.chat.last_name} (id {user_id}) не прошёл проверку на подписки')
            start(call.message)

bot.infinity_polling()