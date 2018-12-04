from app.exception.exception import FileDoesNotExist, GetFileError, PostFileError
from utils.exception.exception import BackEndError

from utils.aws.aws import BackEnd


class Service:
    back_end = BackEnd()

    @classmethod
    def get(cls, filename):
        try:
            return cls.back_end.get(filename)
        except FileDoesNotExist:
            raise GetFileError

    @classmethod
    def post(cls, name, file):
        try:
            return cls.back_end.post(name, file)
        except BackEndError:
            raise PostFileError
