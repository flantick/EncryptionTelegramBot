class FoundContent:

    def __init__(self, message, for_vrfsign=False):

        self.brackets = [['(', ')'], ['[', ']']]
        self.content = []
        self.max_split = 1

        if for_vrfsign is True:
            self.max_split = 2
            self.brackets.insert(1, ['{', '}'])

        self.message = message.split('\n', maxsplit=self.max_split)
        self.step = 0

        self.key = ''
        self.cipher_or_text = ''
        self.text_for_sgn = ''

    def set_values(self):
        for bracket in self.brackets:

            if bracket[0] not in self.message[self.step] or bracket[1] not in self.message[self.step]:
                self.key = 'error0'
                self.cipher_or_text = 'error0'
                self.text_for_sgn = 'error0'
                return None

            start = self.message[self.step].find(bracket[0])
            end = self.message[self.step].rfind(bracket[1])
            self.content.append(self.message[self.step][start+1:end])
            self.step = self.step + 1

        self.key = self.content[0]
        self.cipher_or_text = self.content[1]
        self.text_for_sgn = self.content[2] if len(self.content) > 2 else None

        return None
