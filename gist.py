from pygost import gost28147
from pygost.utils import hexdec
from pygost.utils import hexenc
from pygost import gost34112012256


def gostcrypt(password, reportiontext, cryption):
    if (password != 'error0') and (reportiontext != 'error0'):  # проверка правописания команды
        if cryption is True:
            password = (gost34112012256.new(password.encode('utf-8'))).digest()  # формирование ключа
            cryptiontext = gost28147.cbc_encrypt(password, reportiontext.encode('utf-8'))  # шифрование
            return hexenc(cryptiontext)
        elif cryption is False:
            password = (gost34112012256.new(password.encode('utf-8'))).digest()  # формирование ключа
            try:
                bytecryptiontext = hexdec(reportiontext)
            except:
                return 'неверный ключ'
            try:
                decrypriontext = gost28147.cbc_decrypt(password, bytecryptiontext).decode('utf-8')  # расшифрование
            except:
                return 'неверный ключ'
            return decrypriontext
    elif (password == 'error0') or (reportiontext == 'error0'):  # проверка правописания команды
        return 'Команда введена неверно, воспользуйтесь подсказкой  - /help'
