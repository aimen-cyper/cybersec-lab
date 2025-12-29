import os
import telebot
from telebot import types

# نأخذ التوكن من الإعدادات (أمان)
TOKEN = os.getenv("8521816992:AAHKWDtrZplSPegYJKOefEfu2CAnsXUz8aw")

bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("🧪 محاكاة التصيّد", callback_data="phishing"),
        types.InlineKeyboardButton("🧠 اختبار أمني", callback_data="quiz"),
        types.InlineKeyboardButton("🌐 شرح IP", callback_data="ip"),
        types.InlineKeyboardButton("🛡️ طرق الحماية", callback_data="defense"),
        types.InlineKeyboardButton("📋 فحص أمني", callback_data="checklist"),
        types.InlineKeyboardButton("ℹ️ عن المختبر", callback_data="about")
    )
    return keyboard

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 مرحبًا بك في *CyberSec Lab*\n\n"
        "مختبر تدريبي تعليمي لفهم الهجمات السيبرانية وطرق الحماية.\n\n"
        "اختر من القائمة:",
        parse_mode="Markdown",
        reply_markup=main_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    chat_id = call.message.chat.id

    if call.data == "phishing":
        bot.send_message(chat_id, "🧪 هذا مثال محاكاة تصيّد (تعليمي فقط).")

    elif call.data == "quiz":
        bot.send_message(chat_id, "🧠 اختبار أمني قادم قريبًا.")

    elif call.data == "ip":
        bot.send_message(chat_id, "🌐 عنوان IP هو رقم يعرّف جهازك على الشبكة.")

    elif call.data == "defense":
        bot.send_message(chat_id, "🛡️ لا تضغط روابط مشبوهة وفعّل 2FA.")

    elif call.data == "checklist":
        bot.send_message(chat_id, "📋 تحقق من الدومين ولا تشارك معلوماتك.")

    elif call.data == "about":
        bot.send_message(
            chat_id,
            "ℹ️ مشروع تعليمي لطلاب الأمن السيبراني.\n"
            "لا يتم جمع أي بيانات."
        )

bot.infinity_polling()