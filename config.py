TOKEN = ' '  # enter your token

WELLCOMEMESSAGE = 'Впервые тут?\n' \
                  'Чтобы ознакомится с ботом напиши - /help'

HELP = 'Вот лови набор команд - это должно тебе помочь разобраться\n' \
                  '/aesen - Зашифровать с помощью aes - <key>ключ</key> <text>этот текст будет зашифрован</text>\n' \
                  '/gosten - Зашифровать с помощью ГОСТ 34.12-2018 - <key>ключ</key> <text>этот текст будет зашифрован</text>\n' \
                  '/hash - Хэширование - <key>метод свертывания</key> <text>этот текст будет захэширован</text>\n' \
                  '/aesde - Расшифровать с помощью aes - <key>ключ</key> <text>этот текст будет расшифрован</text>\n' \
                  '/gostde - Расшифровать с помощью ГОСТ 34.12-2018 - <key>ключ</key> <text>этот текст будет расшифрован</text>\n' \
                  '/mksign - сформировать электронную цифровую подпись - <key>секретный ключ</key> <text>этот текст будет зашифрован</text>\n' \
                  '/vrfsign - проверить электронную цифровую подпись - <key1>Публичный ключ1</key1> <key2>Публичный ключ2</key2> <text>этот текст пройдет проверку</text> <sgn>подпись</sgn>\n' \
       '===============================\n' \
       'Чтобы подробнее ознакомится с командами напиши следующее\n' \
       '/help_aes - узнать про aes \n' \
       '/help_gost - узнать про gost \n' \
       '/help_hash - узнать про hash \n' \
       '/help_sign - узнать про sign \n'

HELPAES = 'AES - криптостойкий симметричный алгоритм блочного шифрования\n' \
             'Подробнее в тексте документа - https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf\n' \
             'Пример зашифровывания\n' \
             '/aesen <key>ключ</key> <text>этот текст будет зашифрован</text>\n' \
             'Пример расшифровывания\n' \
             '/aesde <key>ключ</key> <text>gAAAAABgS4JVjvJ00i5d780FIj_IOqvho1deapTCPSlaoNks9TN6tzUM5fEje74BZtsEYvD6xwfWjP6zuO7f37YXtKZYtFIKIqAAZLO6uO0YQLXZy7uSedTJSpzJzgoq9_FbJJvh7nQKYJvZ_TC4jUHtFNn-q-mrOg==</text>'

GOSTHELP = 'ГОСТ 34.12-2018 криптостойкий симметричный блочный шифр с 256-битным ключом и 32 циклами преобразования, оперирующий 64-битными блоками\n' \
           'Подробнее в тексте документа - http://docs.cntd.ru/document/gost-28147-89\n' \
           'Пример зашифровывания\n' \
           '/gosten <key>ключ</key> <text>этот текст будет зашифрован</text>\n' \
           'Пример расшифровывания\n' \
           '/gostde <key>ключ</key> <text>0000000000000000020002f0d8b52c7e3a83c255462bb7625b4d79f56397c279b488c1e80f73176f445eaf0ca3fe9833364bfe20e17cf6d1a5c6c61b1a3e28cc</text>'

HASHHELP = 'Хеш-функция — функция, осуществляющая преобразование массива входных данных произвольной длины в (выходную) битовую строку установленной длины\n' \
           'На нашем боте реализованы следующие алгоритмы свертывания - sha1, sha256, sha512, md5, ГОСТ 34.11-2018(gost512, gost256) \n' \
           'Подробнее по ссылкам ниже\n' \
           'sha1 - https://ru.wikipedia.org/wiki/SHA-1\n' \
           'sha256, sha512 - https://ru.wikipedia.org/wiki/SHA-2\n' \
           'md5 - https://ru.wikipedia.org/wiki/MD5\n' \
           'ГОСТ 34.11-2018 - https://docs.cntd.ru/document/1200161707 \n' \
           'Пример свертывания\n' \
           '/hash <key>md5</key> <text>этот текст будет хэширован</text>'

HELPSIGN = 'ГОСТ 34.10-2018 -  действующий межгосударственный криптографический стандарт, описывающий алгоритмы формирования и проверки электронной цифровой подписи реализуемой с использованием операций в группе точек эллиптической кривой  \n' \
           'Подробнее в тексте документа - https://docs.cntd.ru/document/1200161706  \n' \
           'Пример формирования\n' \
           '/mksign <key>секретный ключ</key> <text>этот текст будет зашифрован</text>\n' \
           'Пример проверки\n' \
           '/vrfsign <key1>11084331005920272738002924377282183054471809002759055291950542225758371327129</key1> <key2>63869738057900090063525930438404014006196807260287243084544146712556567056706</key2> <text>этот текст будет зашифрован</text> <sgn>76fee15e7708ec9ad6fc2be43fc92f8c1b79bbf213aba45c52b2012126b8e2f1b8dd69e12b6436a1790dbd3b9eea8fdafad6b2e3a2775c503f2bdae9642d2d67</sgn>'