def foundclef(text):
    keystart = text.find("<key>")
    keyend = text.find("</key>")
    clef = text[keystart+5:keyend]
    if ('<key>' in text) and ('</key>' in text):
        return clef
    else:
        return 'error0'


def foundreport(text):
    textstart = text.find("<text>")
    textend = text.find("</text>")
    report = text[textstart+6:textend]
    if ('<text>' in text) and ('</text>' in text):
        return report
    else:
        return 'error0'


def foundkey1(text):
    keystart = text.find("<key1>")
    keyend = text.find("</key1>")
    key1 = text[keystart+6:keyend]
    if ('<key1>' in text) and ('</key1>' in text):
        return key1
    else:
        return 'error0'


def foundkey2(text):
    keystart = text.find("<key2>")
    keyend = text.find("</key2>")
    key1 = text[keystart+6:keyend]
    if ('<key2>' in text) and ('</key2>' in text):
        return key1
    else:
        return 'error0'


def foundsignature(text):
    keystart = text.find("<sgn>")
    keyend = text.find("</sgn>")
    signature = text[keystart+5:keyend]
    if ('<sgn>' in text) and ('</sgn>' in text):
        return signature
    else:
        return 'error0'
