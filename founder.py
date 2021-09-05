class FoundContentFromTag:

    start = 0
    end = 0
    content = ''

    @classmethod
    def found(cls, tag, text_from_message):
        tag_start = '<' + tag + '>'
        tag_end = '</' + tag + '>'
        if tag_start not in text_from_message or tag_end not in text_from_message:
            return 'error0'
        else:
            cls.start = text_from_message.find(tag_start)+len(tag_start)
            cls.end = text_from_message.find(tag_end)
            cls.content = text_from_message[cls.start:cls.end]
            return cls.content
