import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def aescrypt(password, reportiontext, cryption):
    if (password != 'error0') and (reportiontext != 'error0'):  # проверка правописания команды

        kdf = PBKDF2HMAC(  # формирование ключа
        algorithm=hashes.SHA256(),
        salt=b'\xef\x1e\x92{2\xd0\xe9Fj\xeeW\xe12\xcf\xb0\xa8',
        length=32,
        iterations=100000,)

        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
        f = Fernet(key)
        if cryption is True:
            token = f.encrypt(reportiontext.encode('utf-8'))  # шифрование
        elif cryption is False:
            try:
                token = f.decrypt(reportiontext.encode('utf-8'))  # расшифрование
            except:
                return 'Неверный ключ'
        token = token.decode('utf-8')
        return token
    elif (password == 'error0') or (reportiontext == 'error0'):  # проверка правописания команды
        return 'Команда введена неверно, воспользуйтесь подсказкой  - /help'
