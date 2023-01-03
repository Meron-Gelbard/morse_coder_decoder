import csv

class MorseDictionary:
    def __init__(self):
        self.code_dict = {}
        self.decode_dict = {}
        self.MAX_INPUT = 25
        with open('morse.csv', "r", newline='') as morse_csv:
            reader = csv.reader(morse_csv)
            for row in reader:
                self.code_dict[row[0]] = row[1]
                self.decode_dict[row[1]] = row[0]
        self.coded_msg = ''
        self.decoded_msg = ''

    def coder(self, message):
        coded_msg = ''
        for i in message.upper():
            if i == ' ':
                coded_msg += i + i
            else:
                coded_msg += f'{self.code_dict[i]} '
        self.coded_msg = coded_msg
        return

    def decoder(self, coded_msg):
        code = coded_msg.split(' ')
        for i in code:
            if i == '':
                self.decoded_msg += ' '
            else:
                self.decoded_msg += f'{self.decode_dict[i]}'
                self.decoded_msg = self.decoded_msg.replace('  ', ' ')
        return self.decoded_msg

