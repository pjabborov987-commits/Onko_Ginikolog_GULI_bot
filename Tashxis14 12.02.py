import telebot
from telebot import types

TOKEN = "8544034355:AAEWj3nXTVntPQc2Tp3h-ifKOnMSXao8RnY"
bot = telebot.TeleBot(TOKEN)

# ==================== CONFIG ====================
VRACH_IDS = [7373163984]

user_lang = {}
user_role = {}
user_data = {}
risk_score = {}

# ==================== TEXTS ====================
texts = {
    "uz": {
    "start": "Tilni tanlang:",
    "bemor": "Ayol",
    "doctor": "Vrach",
    "role": "Rolni tanlang:",
    "result": "📊 Boshlang‘ich risk balli:",
    "doctor_msg": "💡 Yakuniy xulosa faqat vrach tomonidan beriladi.",
    "motiv_low": "🟢 Sizning sog‘lig‘ingiz a’lo darajada. Faqat o‘zingiz uchun ehtiyot bo‘ling.",
    "motiv_mid": "🟡 Sog‘lig‘ingizda e’tiborli bo‘lishingiz tavsiya qilinadi. Vrachga uchrashing!\nAgar kerak bo‘lsa, Surxondaryo viloyati Onkologiya Dispensari Vrachi Onkoginikolog **Gulbaxor Anvarovna**ga murojaat qilishingiz mumkin.\n📞 Telefon: +998901234567\n🏥 Manzil: Surxondaryo viloyati, Termiz sh., Onkologiya Dispensari\n✉ Telegram: @GulbaxorAnvarovna",
    "motiv_high": "🔴 Sog‘lig‘ingizda xavf mavjud! Darhol vrachga murojaat qiling!\nSurxondaryo viloyati Onkologiya Dispensari Vrachi Onkoginikolog **Gulbaxor Anvarovna**ga murojaat qiling.\n📞 Telefon: +998901234567\n🏥 Manzil: Surxondaryo viloyati, Termiz sh., Onkologiya Dispensari\n✉ Telegram: @GulbaxorAnvarovna",
    "restart": "🏠 Boshidan boshlash"
},
"ru": {
    "start": "Выберите язык:",
    "bemor": "Женщина",
    "doctor": "Врач",
    "role": "Выберите роль:",
    "result": "📊 Начальный риск балл:",
    "doctor_msg": "💡 Окончательный вывод дается только врачом.",
    "motiv_low": "🟢 Ваше здоровье в порядке. Берегите себя.",
    "motiv_mid": "🟡 Обратите внимание на здоровье. Посетите врача!\nЕсли нужно, вы можете обратиться к врачу онкогинекологу **Гулбахор Анваровна**, Онкологический диспансер Сурхандарьинской области.\n📞 Телефон: +998901234567\n🏥 Адрес: Сурхандарьинская область, г. Теримз, Онкологический диспансер\n✉ Telegram: @GulbaxorAnvarovna",
    "motiv_high": "🔴 Есть риск для здоровья! Срочно обратитесь к врачу!\nОбратитесь к врачу онкогинекологу **Гулбахор Анваровна**, Онкологический диспансер Сурхандарьинской области.\n📞 Телефон: +998901234567\n🏥 Адрес: Сурхандарьинская область, г. Теримз, Онкологический диспансер\n✉ Telegram: @GulbaxorAnvarovna",
    "restart": "🏠 Начать заново"
},
"en": {
    "start": "Choose language:",
    "bemor": "Woman",
    "doctor": "Doctor",
    "role": "Choose your role:",
    "result": "📊 Initial risk score:",
    "doctor_msg": "💡 Final conclusion must be given by a doctor.",
    "motiv_low": "🟢 Your health is excellent. Take care of yourself.",
    "motiv_mid": "🟡 Pay attention to your health. Visit a doctor!\nIf needed, you can contact **Gulbaxor Alisherovna**, Oncogynecologist at Surxondaryo Oncology Dispensary.\n📞 Phone: +998901234567\n🏥 Address: Surxondaryo region, Termiz city, Oncology Dispensary\n✉ Telegram: @GulbaxorAnvarovna",
    "motiv_high": "🔴 Health risk detected! See a doctor immediately!\nContact **Gulbaxor Alisherovna**, Oncogynecologist at Surxondaryo Oncology Dispensary.\n📞 Phone: +998901234567\n🏥 Address: Surxondaryo region, Termiz city, Oncology Dispensary\n✉ Telegram: @GulbaxorAnvarovna",
    "restart": "🏠 Restart"
    }
}

# ==================== QUESTIONS & ANSWERS ====================
questions = {
    "uz": [
        "1. Necha yoshda turmushga chiqqansiz?",
        "2. Sizning yoshingiz nechida?",
        "3. Qaysi kasallik bilan davolanib yuribsiz?",
        "4. Tug‘ruqlar soni nechta?",
        "5. Necha marta abort o‘tkazilgan?",
        "6. Homiladorlikdan qanday saqlanasiz?",
        "7. Ayollik yo‘lidan suvli-hidli ajralma keladimi?",
        "8. Jinsiy aloqa, ginekolog ko‘rigi, tampon, defekatsiya yoki jismoniy zo‘riqishda qonni ko‘rasizmi?",
        "9. Kontaktda o‘z-o‘zidan qonli ajralma keladimi?",
        "10. So‘nggi oylar ichida semirish yoki qorinning kattalashishi kuzatildimi?",
        "11. Hayz vaqtida lahta-lahta qon ketadimi?",
        "12. Hayz tsiklida buzilish (bir oyda ikki marta hayz) kuzatiladimi?",
        "13. Poliklinikada kolposkopik tekshiruvdan o‘tganmisiz?",
        "14. UZI tekshiruvida bachadon miomasi yoki adenomiya aniqlanganmi?",
        "15. Sizga jinsiy yo‘l bilan yuqadigan virus (HPV) topilganmi?"
    ],
    "ru": [
        "1. В каком возрасте вы вышли замуж?",
        "2. Сколько вам лет?",
        "3. С каким заболеванием вы лечитесь?",
        "4. Сколько у вас родов?",
        "5. Сколько раз были аборты?",
        "6. Как вы предохраняетесь от беременности?",
        "7. Бывают ли водянистые/неприятно пахнущие выделения?",
        "8. Может ли появляться кровь при половом акте, визите к гинекологу, введении тампона, дефекации, физической нагрузке?",
        "9. Появляется ли кровь самостоятельно при контакте?",
        "10. За последние месяцы увеличился вес или живот?",
        "11. Кровотечение во время месячных?",
        "12. Нарушение цикла (два раза в месяц месячные)?",
        "13. Проходили ли колпоскопию в поликлинике?",
        "14. Выявлена ли миома или аденомиоз при УЗИ?",
        "15. У вас обнаружен вирус, передающийся половым путём (HPV)?"
    ],
    "en": [
        "1. At what age did you get married?",
        "2. How old are you?",
        "3. What disease are you being treated for?",
        "4. Number of deliveries?",
        "5. How many abortions have you had?",
        "6. How do you prevent pregnancy?",
        "7. Do you have watery or bad-smelling discharge?",
        "8. Does blood appear during intercourse, gynecologist visit, tampon, defecation, or physical activity?",
        "9. Does blood appear spontaneously during contact?",
        "10. Have you gained weight or enlarged abdomen recently?",
        "11. Bleeding during menstruation?",
        "12. Menstrual cycle disturbance (two periods per month)?",
        "13. Have you had colposcopy in your clinic?",
        "14. Was fibroid or adenomyosis detected in ultrasound?",
        "15. Have you been diagnosed with a sexually transmitted virus (HPV)?"
    ]
}

answers = {
    "uz": [
        ["17-19","20-35","35-45"],
        ["25gacha-35","35-45","45-55 va undan katta"],
        ["Qandli diabet","Semizlik","Qon bosimi","Hech qanaqa"],
        ["1-2 ta","3 ta","4 va undan ortiq","0 ta"],
        ["1-2 ta","3 ta","4 va undan ortiq","0 ta"],
        ["Prezervativ (rezinka)","Kontratseptsiya (tabletka, svyecha)","Bachadon ichi vositasi (spiral)","IJK", "Yoq"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q","Bazan"],
        ["Ha","Yo‘q"],
        ["Ha","Yo‘q"],
        ["Ha","Yo‘q"]
    ],
    "ru": [
        ["17-19","20-35","35-45"],
        ["до 35","35-45","45-55 и старше"],
        ["Сахарный диабет","Ожирение","Повышенное давление","Нет"],
        ["1-2","3","4 и более","0 "],
        ["1-2","3","4 и более","0"],
        ["Презерватив","Таблетки/свечи","Внутриматочная спираль","ИЖК","Нет"],
        ["Да","Нет","Иногда"],
        ["Да","Нет","Иногда"],
        ["Да","Нет","Иногда"],
        ["Да","Нет","Иногда"],
        ["Да","Нет","Иногда"],
        ["Да","Нет","Иногда"],
        ["Да","Нет"],
        ["Да","Нет"],
        ["Да","Нет"]
    ],
    "en": [
        ["17-19","20-35","35-45"],
        ["up to 35","35-45","45-55 and above"],
        ["Diabetes","Obesity","High blood pressure","None"],
        ["1-2","3","4 or more","0"],
        ["1-2","3","4 or more","0"],
        ["Condom","Pills/suppository","IUD","IJK", "No"],
        ["Yes","No","Sometimes"],
        ["Yes","No","Sometimes"],
        ["Yes","No","Sometimes"],
        ["Yes","No","Sometimes"],
        ["Yes","No","Sometimes"],
        ["Yes","No","Sometimes"],
        ["Yes","No"],
        ["Yes","No"],
        ["Yes","No"]
    ]
}

scores = [
    {"17-19":3,"20-35":0,"35-45":1},
    {"25gacha-35":1,"35-45":1,"45-55 va undan katta":3},
    {"Qandli diabet":1,"Semizlik":1,"Qon bosimi":1,"Hech qanaqa":0},
    {"1-2 ta":1,"3 ta":2,"4 va undan ortiq":3},
    {"1-2 ta":1,"3 ta":2,"4 va undan ortiq":3,"0 ta":0},
    {"Prezervativ (rezinka)":1,"Kontratseptsiya (tabletka, svyecha)":2,"Bachadon ichi vositasi (spiral)":2,"IJK":3},
    {"Ha":2,"Bazan":1,"Yo‘q":0},
    {"Ha":2,"Bazan":1,"Yo‘q":0},
    {"Ha":2,"Bazan":1,"Yo‘q":0},
    {"Ha":2,"Bazan":1,"Yo‘q":0},
    {"Ha":1,"Bazan":0,"Yo‘q":0},
    {"Ha":1,"Bazan":0,"Yo‘q":0},
    {"Ha":1,"Yo‘q":0},
    {"Ha":2,"Yo‘q":0},
    {"Ha":3,"Yo‘q":0}
]

# ==================== START ====================
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("UZ 🇺🇿","RU 🇷🇺","EN 🇬🇧")
    bot.send_message(message.chat.id, texts["uz"]["start"], reply_markup=markup)

# ==================== LANGUAGE ====================
@bot.message_handler(func=lambda message: message.text in ["UZ 🇺🇿","RU 🇷🇺","EN 🇬🇧"])
def select_lang(message):
    chat_id = message.chat.id
    lang = "uz" if "UZ" in message.text else "ru" if "RU" in message.text else "en"
    user_lang[chat_id] = lang

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(texts[lang]["bemor"], texts[lang]["doctor"])
    bot.send_message(chat_id, texts[lang]["role"], reply_markup=markup)

# ==================== ROLE ====================
@bot.message_handler(func=lambda message: message.text in [
    texts["uz"]["bemor"], texts["ru"]["bemor"], texts["en"]["bemor"],
    texts["uz"]["doctor"], texts["ru"]["doctor"], texts["en"]["doctor"]
])
def select_role(message):
    chat_id = message.chat.id
    lang = user_lang[chat_id]

    if message.text == texts[lang]["bemor"]:
        user_role[chat_id] = "bemor"
        risk_score[chat_id] = 0
        user_data[chat_id] = {"answers":{}}
        ask_question(chat_id, 0)
    elif message.text == texts[lang]["doctor"]:
        if chat_id in VRACH_IDS:
            user_role[chat_id] = "vrach"
            show_stats(chat_id)
        else:
            bot.send_message(chat_id,"❌ Siz vrach emassiz")

# ==================== ASK QUESTIONS ====================
def ask_question(chat_id,index):
    lang = user_lang[chat_id]
    if index < len(questions[lang]):
        q_text = questions[lang][index]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for option in answers[lang][index]:
            markup.add(option)
        msg = bot.send_message(chat_id, q_text, reply_markup=markup)
        bot.register_next_step_handler(msg, process_answer, index)
    else:
        finish(chat_id)

def process_answer(message,index):
    chat_id = message.chat.id
    lang = user_lang[chat_id]
    ans = message.text
    user_data[chat_id]["answers"][questions[lang][index]] = ans
    risk_score[chat_id] += scores[index].get(ans,0)
    ask_question(chat_id,index+1)

# ==================== FINISH ====================
def finish(chat_id):
    lang = user_lang[chat_id]
    ball = risk_score[chat_id]
    if ball <=7:
        text = f"🟢 {texts[lang]['result']} {ball}\n{texts[lang]['motiv_low']}"
    elif ball <=14:
        text = f"🟡 {texts[lang]['result']} {ball}\n{texts[lang]['motiv_mid']}"
    else:
        text = f"🔴 {texts[lang]['result']} {ball}\n{texts[lang]['motiv_high']}"

    text += f"\n\n{texts[lang]['doctor_msg']}"
    bot.send_message(chat_id, text)

    for v in VRACH_IDS:
        bot.send_message(v, f"🆕 Yangi bemor\nID:{chat_id}\nRisk:{ball}")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(texts[lang]['restart'])
    bot.send_message(chat_id, texts[lang]['restart'], reply_markup=markup)

# ==================== DOCTOR STATS ====================
def show_stats(chat_id):
    text = "📊 Bemorlar statistikasi:\n"
    for cid, data in user_data.items():
        score = risk_score.get(cid,0)
        text += f"ID:{cid} | Score:{score}\n"
    bot.send_message(chat_id, text)

# ==================== RESTART ====================
@bot.message_handler(func=lambda message: message.text in [
    texts["uz"]["restart"], texts["ru"]["restart"], texts["en"]["restart"]
])
def restart(message):
    start(message)

# ==================== POLLING ====================
bot.infinity_polling()
