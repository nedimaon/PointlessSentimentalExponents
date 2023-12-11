import requests
from telegram.ext import Updater, CommandHandler, MessageHandler

# Токен бота
TOKEN = "6886952017:AAHKjtyTv7v6L9IcmMkVd2hs5fxaHoRK7L4"


# Обработчик сообщений
def get_address(update, context):
  # Получаем сообщение от пользователя
  message = update.message.text

  # Если сообщение содержит команду /find_address
  if message.startswith("/find_address"):
    # Получаем IP-адрес из сообщения
    ip_address = message.split()[1]

    # Формируем URL запроса
    url = "https://ipinfo.io/{}/json".format(ip_address)

    # Отправляем запрос
    response = requests.get(url)

    # Проверяем ответ
    if response.status_code == 200:
      # Получаем данные из ответа
      data = response.json()

      # Формируем сообщение с адресом
      message = "Адрес для IP-адреса {}:\n\nГород: {}\nРегион: {}\nСтрана: {}".format(
          ip_address, data["city"], data["region"], data["country"])

      # Отправляем сообщение пользователю
      context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
      # Отправляем сообщение об ошибке
      context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Ошибка получения адреса")


# Создаем бота
updater = Updater(TOKEN)

# Добавляем обработчик сообщений
updater.dispatcher.add_handler(MessageHandler(Filters.text, get_address))

# Запускаем бота
updater.start_polling()
updater.idle()
