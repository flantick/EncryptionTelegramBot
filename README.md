# EncryptionTelegramBot

__Что умеет делать бот?__
  * Шифрование сообщений с помощью алгоритмов AES и ГОСТ 34.12-2018 с длинной бока 64 бита (Магма);
  * Формирование и проверка цифровой подписи с помощью алгоритма ГОСТ Р 34.10-2018;
  * Вычисление хэш-сумм с помщью алгоритмов SHA-1, SHA-2, MD5, ГОСТ 34.11-2018 (Стрибог).
  
__Для запуска бота вы должны:__
    * Вписать token телеграм-бота в config.py;
    * Установить pyTelegramBotAPI (pip install pyTelegramBotAPI);
    * Установить cryptography (pip install cryptography);
    * Установить pygost (pip install pygost);
    * Установить hashlib (pip install hashlib).
  
