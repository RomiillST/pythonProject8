from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from User_class import User
from sql_req import *
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

def press_f(update, context):
    u = User(update)
    user_id, text = u.bervor()
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    if text.upper() == 'F':
        c = cur.execute(counter_in_table.format(user_id)).fetchone()[0]
        c+= 1
        cur.execute(update_counter.format(c, user_id))
        conn.commit()
def score(update,context):
    u = User(update)
    user_id, text = u.bervor()
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    c = cur.execute(counter_in_table.format(user_id)).fetchone()[0]
    button = [InlineKeyboardButton(text=c, callback_data='aoe')]
    context.bot.send_message(text='Лови свой счёт', chat_id = user_id, reply_markup=InlineKeyboardMarkup([button]))