import hashlib
from pygost import gost34112012256
from pygost import gost34112012512
from pygost.utils import hexenc


def hash(method, reportiontext):
    if method != 'error0' and reportiontext != 'error0':  # проверка правописания команды
        if method == 'md5':
            return (hashlib.md5(reportiontext.encode('utf-8'))).hexdigest()
        elif method == 'sha1':
            return (hashlib.sha1(reportiontext.encode('utf-8'))).hexdigest()
        elif method == 'sha256':
            return (hashlib.sha256(reportiontext.encode('utf-8'))).hexdigest()
        elif method == 'sha512':
            return (hashlib.sha512(reportiontext.encode('utf-8'))).hexdigest()
        elif method == 'gost256':
            return hexenc(gost34112012256.new(reportiontext.encode('utf-8')).digest())
        elif method == 'gost512':
            return hexenc(gost34112012512.new(reportiontext.encode('utf-8')).digest())
        else:
            return 'Введен неправильный алгоритм свертывания'
    elif method == 'error0' or reportiontext == 'error0':  # проверка правописания команды
        return 'Команда введена неверно, воспользуйтесь подсказкой - /help'
