from utils.aws.aws import BackEnd


class Service:
    def __init__(self):
        self.back_end = BackEnd()

    def get(self, filename):
        return self.back_end.get(filename)

    def post(self, name, file):
        return self.back_end.post(name, file)
