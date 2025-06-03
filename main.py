from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7675637455:AAHoyrmpuCpXsTUobb8MOmJxTP3a2cyC6bc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === Кнопка "Начать" ===
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("🚀 Начать"))

# === Главное меню ===
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(
    KeyboardButton("💰 Пополнение биржи"),
    KeyboardButton("🏦 Вывод на карту"),
)
main_kb.add(KeyboardButton("📞 Связь с овнером"))

# === /start команда ===
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(
        "Привет! 👋\nДобро пожаловать в крипто-обмен бот.\nНажмите кнопку ниже, чтобы начать:",
        reply_markup=start_kb
    )

# === Обработка кнопки "Начать" ===
@dp.message_handler(lambda m: m.text == "🚀 Начать")
async def show_main_menu(msg: types.Message):
    await msg.answer(
        "Выберите, что хотите сделать:",
        reply_markup=main_kb
    )

# === Пополнение биржи ===
@dp.message_handler(lambda m: m.text == "💰 Пополнение биржи")
async def deposit(msg: types.Message):
    await msg.answer(
        "**Пополнение биржи USDT → грн**\n\n"
        "Курс: *1 USDT = 39.5 грн*  📈\n\n"
        "Переведите сумму на адрес TRC20:\n"
        "`TXABC123456789XYZ`  ← 🔁 УКАЖИ СВОЙ АДРЕС!\n\n"
        "После перевода отправьте сюда последние 4 символа TX хэша.",
        parse_mode='Markdown'
    )

# === Вывод на карту ===
@dp.message_handler(lambda m: m.text == "🏦 Вывод на карту")
async def withdraw(msg: types.Message):
    await msg.answer(
        "**Вывод с биржи → на карту (грн)**\n\n"
        "Курс: *1 USDT = 39.0 грн* 🏦\n\n"
        "Отправьте сумму, которую хотите вывести, и номер карты в формате:\n"
        "`1000 UAH  5375 XXXX XXXX XXXX`",
        parse_mode='Markdown'
    )

# === Связь с овнером ===
@dp.message_handler(lambda m: m.text == "📞 Связь с овнером")
async def contact(msg: types.Message):
    await msg.answer(
        "📩 Напиши владельцу в Telegram:\n"
        "@yourusername  ← 🔁 ЗАМЕНИ НА СВОЙ @ЮЗЕРНЕЙМ"
    )

# === Обработка прочих сообщений ===
@dp.message_handler()
async def echo(msg: types.Message):
    await msg.answer("❗ Пожалуйста, выберите действие из меню.")

# === Запуск бота ===
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
