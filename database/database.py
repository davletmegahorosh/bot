import random
import sqlite3

db = sqlite3.connect('bot.sqlite3')
cursor = db.cursor()

def sql_create():
    if db:
        print('data base ')

    db.execute("CREATE TABLE IF NOT EXISTS mentorbot"
               "(id INTEGER PRIMARY_KEY, username TEXT, "
               "name TEXT, age INTEGER, gender TEXT, "
               "photo TEXT)")
    db.commit()

async def sql_command_create(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentorbot VALUES  "
                       "(?,?,?,?,?,?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentorbot").fetchall()
    random_user = random.choice(result)
    await message.answer_photo(f"{random_user[5]}",
                               caption=f"{random_user[2]}\n {random_user[3]}\n"
                                f" {random_user[4]}\n {random_user[1]}")


async def sql_command_all():
    result = cursor.execute("SELECT * FROM mentorbot").fetchall()

async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentorbot WHERE id= ?", (user_id,))
    db.commit()