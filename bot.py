import os
from typing import Final
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ConversationHandler, ContextTypes


#TOKEN: Final = "7475838300:AAFp63ucpG1OnfTEpn0igVrpCRIXVlnLgyc"
TOKEN: Final = os.getenv('TELEGRAM_TOKEN')
BOT_USERNAME: Final = "@dopomoga_tartu_bot"

# Stages
START_ROUTES = range(1)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привіт! Задайте своє питання стосовно захисту в Естонії", reply_markup=reply_markup)
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Задайте інше питання стосовно захисту в Естонії", reply_markup=reply_markup)
    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Перейдіть за посиланням https://asylum.politsei.ee або зверніться безпосередньо до Департаменту поліції.Для подачі заявки необхідно обов’язково мати зареєстроване місце проживання (прописку).Тимчасовий захист подавати за 3 місяці і менше. Міжнародний захист подавати за  4 місяці і менше. Але! Бажано подати заяву на продовження не пізніше ніж за 1 місяць до закінчення дії наявної посвідки.", reply_markup=reply_markup)
    return START_ROUTES


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Нове цифрове фото є обов’язковим. Його необхідно зробити до або протягом 14 днів після подачі клопотання.Сфотографуватися Ви можете у найближчому відділку поліції, запис по живій черзі. Знайти найближче відділення поліції можна за посиланням: https://www.politsei.ee/ru/raspolozhenie/byuro-obsluzhivaniya (тільки російською мовою). З собою потрібно мати свою ID-картку.",
        reply_markup=reply_markup)    
    return START_ROUTES

async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Спочатку подавайте своє клопотання, а вже потім по черзі клопотання для своїх дітей.", reply_markup=reply_markup)
    return START_ROUTES

async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Спробуйте зайти через інший браузер. Для цього необхідно скопіювати посилання і вставити його в рядок адреси в іншому браузері. Або спробуйте подати пізніше.", reply_markup=reply_markup)
    return START_ROUTES

async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Тимчасовий захист подовжується до березня 2025 року", reply_markup=reply_markup)
    return START_ROUTES

async def six(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Електронну пошта поліції ppa@politsei.ee. Телефон 1247", reply_markup=reply_markup)
    return START_ROUTES

async def seven(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Перейдіть статус своєї заявки на продовження тимчасового захисту можна за посиланням https://www.politsei.ee/ru/zaprosy/status-zayavleniya-grazhdanina-estonii (тільки російською мовою)", reply_markup=reply_markup)
    return START_ROUTES

async def eight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Подати заяву на продовження", callback_data=str(ONE)),
            InlineKeyboardButton("Фото", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Захист для дитини", callback_data=str(THREE)),
            InlineKeyboardButton("Сайт не працює", callback_data=str(FOUR)) 
        ],
        [
            InlineKeyboardButton("Термін захисту", callback_data=str(FIVE)),
            InlineKeyboardButton("Контакти", callback_data=str(SIX)) 
        ],
        [
            InlineKeyboardButton("Перевірити статус", callback_data=str(SEVEN)),
            InlineKeyboardButton("Термін дії моєї посвідки вже закінчився, але немає нової", callback_data=str(EIGHT))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Не хвилюйтесь, це доволі типова ситуація (хоч і не дуже приємна). Ви можете перевірити статус своєї заявки на сайті https://www.politsei.ee/ru/zaprosy/status-zayavleniya-grazhdanina-estonii", reply_markup=reply_markup)
    return START_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Дякуємо, що скористались нашим ботом!")
    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(five, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(six, pattern="^" + str(SIX) + "$"),
                CallbackQueryHandler(seven, pattern="^" + str(SEVEN) + "$"),
                CallbackQueryHandler(eight, pattern="^" + str(EIGHT) + "$"),
            ]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":
    main()




