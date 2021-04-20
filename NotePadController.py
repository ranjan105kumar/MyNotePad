import NotePadModel

class Controller:

    def __init__(self):
        self.model = NotePadModel.Model()

    def save_file(self, msg, url):
        self.model.save_file(msg, url)

    def save_as(self, msg, url):
        self.model.save_file(msg, url)

    def read_file(self, url):
        self.msg, self.base = self.model.read_file(url)
        return self.msg, self.base

    def saysomeThing(self):
       self.takeAudio = self.model.takeQuery()
       return  self.takeAudio
