from pygost.gost3410 import CURVES
from pygost.gost3410 import public_key
from pygost.gost3410 import sign
from pygost.gost3410 import verify
from pygost.utils import bytes2long
from pygost import gost34112012256
from pygost.utils import hexdec
from pygost.utils import hexenc


def mksign(password, reportiontext):
    if (password != 'error0') and (reportiontext != 'error0'):  # проверка правописания команды
        curve = CURVES["id-GostR3410-2001-CryptoPro-A-ParamSet"]  # определяем точки кривой
        dgst = gost34112012256.new(reportiontext.encode('utf-8')).digest()  # получаем дайджест сообщения
        key = password.encode('utf-8')  # формирование ключа
        key = bytes2long(key)
        signature = sign(curve, key, dgst)  # формирование подписи
        signature = hexenc(signature)
        pub_x, pub_y = public_key(curve, key)  # формирование публичного ключа
        report = ('Подпись - ' + signature + '\nПубличный ключ1 - ' + str(pub_x) + '\nПубличный ключ2 - ' + str(pub_y))
        return report
    elif (password == 'error0') or (reportiontext == 'error0'):  # проверка правописания команды
        return 'Команда введена неверно, воспользуйтесь подсказкой  - /help'


def vrfsign(key_x, key_y, text, signature):
    if (key_x != 'error0') and (key_y != 'error0') and (text != 'error0') and (signature != 'error0'):  # проверка правописания команды
        curve = CURVES["id-GostR3410-2001-CryptoPro-A-ParamSet"]  # определяем точки кривой
        dgst = gost34112012256.new(text.encode('utf-8')).digest()  # получайем дайджест сообщения
        try:
            signature = hexdec(signature)
        except:
            return False
        is_signed = verify(curve, (int(key_x), int(key_y)), dgst, signature)  # проверка подписи
        return is_signed
    elif (key_x == 'error0') or (key_y == 'error0') or (text == 'error0') or (signature == 'error0'):  # проверка правописания команды
        return 'Команда введена неверно, воспользуйтесь подсказкой  - /help'
