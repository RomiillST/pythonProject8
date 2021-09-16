from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
from User_class import User
from sql_req import *
import time
def start(update, context):
    u = User(update)
    user_id, text = u.bervor()
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    id = cur.execute(tg_id_in_table.format(user_id)).fetchone()
    if id == None:
        cur.execute(first_insert.format(user_id))
        conn.commit()
    context.bot.send_message(text = 'Вы знаете что делать ༼ つ ◕_◕ ༽つ', chat_id = user_id)

# def press_f(update, context):
#     u = User(update)
#     user_id, text = u.bervor()
#     conn = sqlite3.connect('identifier.sqlite')
#     cur = conn.cursor()
#     if text.upper() == 'F':
#         c = cur.execute(counter_in_table.format(user_id)).fetchone()[0]
#         c+= 1
#         cur.execute(update_counter.format(c, user_id))
#         conn.commit()
# def score(update,context):
#     u = User(update)
#     user_id, text = u.bervor()
#     conn = sqlite3.connect('identifier.sqlite')
#     cur = conn.cursor()
#     c = cur.execute(counter_in_table.format(user_id)).fetchone()[0]
#     button = [InlineKeyboardButton(text=c, callback_data='aoe')]
#     context.bot.send_message(text='Лови свой счёт', chat_id = user_id, reply_markup=InlineKeyboardMarkup([button]))
# def adm(update, context):
#     user_id = update.message.chat_id
#     if user_id == 94835800:
#         photo_id = update.message.photo[-1].file_id
#         file = context.bot.getFile(photo_id)
#         file.download('Photos/RecLAMA.jpeg')
#         text = update.message.caption
#         if text == None:
#             pass
#         else:
#             conn = sqlite3.connect('identifier.sqlite')
#             cur = conn.cursor()
#             ids = cur.execute('''
#             SELECT TG_ID
#             FROM Users
#             WHERE TG_ID != 0
#             ''').fetchall()
#             for e in ids:
#                 e = e[0]
#                 context.bot.send_chat_action(chat_id = e, action=telegram.ChatAction.UPLOAD_PHOTO)
#                 time.sleep(2)
#                 context.bot.send_photo(photo = open('Photos/RecLAMA.jpeg', 'rb'), chat_id=e, caption=text)