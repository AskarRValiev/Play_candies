from config import TOKEN
#global candies, max_cand
candies = 200
max_cand = 28
import functions



from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
ORDER, HUMAN = range(2)

# функция обратного вызова точки входа в разговор
def start(update, context):
    update.message.reply_text(
        f'Привет! Играем в игру с конфетами. Всего на столе {candies} конфет, '
        f'игрок может взять за один раз не более {max_cand} конфет '
        'проигрывает тоn, кто взял последнюю конфету. '
        'Если передумал или надоест играть напиши /cancel, ' 
        'если согласен напиши "да"')
    # переходим к этапу `ORDER`
    return ORDER


def order(update, context):    #определяем кто ходит первым
    if ORDER in context.user_data:
        return human(update,context)
    text = update.message.text
    if text.lower() != 'да':
        update.message.reply_text('Ответ неверный, нужно написать "да"')
        return ORDER
    else:
        update.message.reply_text('Определим, кто ходит первым')
        flag = functions.turn_order()
        context.user_data[ORDER] = flag
    if flag == 0:             
        update.message.reply_text('Ходи первым')
        return HUMAN
    else:
        #update.message.reply_text('Первым хожу я')
        bot(update, context)
    
    
def human(update, context):   #ход человека
    text = update.message.text
    global candies
    if text.isdigit() and int(text) <=28 and int(text) <= candies:
        candies = functions.step(candies, int(text))
        if candies <= 0:
            update.message.reply_text(f'Ты взял {int(text)} конфет, Конфет больше не осталось, ты проиграл!'
            'Спасибо за игру, заходи если будет скучно.')
            return ConversationHandler.END
        else:
            update.message.reply_text(f'Ты взял {int(text)} конфет, теперь осталось {candies} конфет. Мой ход.')
            bot(update, context)
    elif not text.isdigit():
        update.message.reply_text('Ты уверен, что это число? Переходи!')
        return HUMAN
    elif int(text) > 28:
        update.message.reply_text(f'Можно брать не больше {max_cand} конфет! Переходи!')
        return HUMAN
    else:
        update.message.reply_text('Ты хочешь взять конфет больше чем осталось? Перехаживай!')
        return HUMAN


def bot(update, context): #ход бота
    global candies
    candies = functions.bot_step(candies, max_cand)
    update.message.reply_text(f'Я взял {candies[1]} конфет, теперь осталось {candies[0]} конфет. Ходи ты.')
    candies = int(candies[0])
    if candies <= 0:
        update.message.reply_text('Конфет больше не осталось, я проиграл!'
        'Спасибо за игру, заходи если будет скучно.')
        return ConversationHandler.END
    else:
        return HUMAN


        # Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
    )
    # Заканчиваем разговор.
    return  ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями ORDER, HUMAN
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            ORDER: [MessageHandler(Filters.text & ~Filters.command, order)],
            HUMAN: [MessageHandler(Filters.text & ~Filters.command, human)],
                       
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],       
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('server started')
    updater.start_polling()
    updater.idle()