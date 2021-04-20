import os
import speech_recognition as s
class Model:

    def __init__(self):
        self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5
    def encrypt(self, plaintext):
        result = ''
        for text in plaintext:
            try:
                i = (self.key.index(text)+self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += text

        return result

    def decrypt(self, ciphertext):
        result = ''
        for l in ciphertext:
            try:
                i = (self.key.index(l) - self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += l

        return result

    def save_file(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url
        filename, file_extension = os.path.splitext(file)
        if file_extension in '.ntxt':
            content = msg
            encrypted = self.encrypt(content)
            with open(file, 'w', encoding='utf-8') as fw:
                fw.write(encrypted)

        else:
            content = msg
            with open(file, 'w') as fw:
                fw.write(content)

    def save_as(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url
        with open(file, 'w') as fw:
            content = msg
            encrypted = self.encrypt(content)
            fw.write(encrypted)

    def read_file(self, url):
        base = os.path.basename(url)
        filename, file_extension = os.path.splitext(url)
        if file_extension in '.ntxt':
            fi = open(url, "r")
            msg1 = fi.read()
            decrypted = self.decrypt(msg1)
            fi.close()
            return decrypted, base
        else:
            fi = open(url, "r")
            msg1 = fi.read()
            fi.close()
            return msg1, base

    def takeQuery(self):
        sr = s.Recognizer()
        sr.pause_threshold = 1
        with s.Microphone() as m:
            print('speak..')
            try:
                sr.adjust_for_ambient_noise(m)
                audio = sr.listen(m)
                query = sr.recognize_google(audio, language='eng-in')
                return query

            except Exception as e:
                print("exception in this", e)
                print("not recognized")
