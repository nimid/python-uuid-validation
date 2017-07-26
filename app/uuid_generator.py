import uuid


class UuidGenerator(object):
    @staticmethod
    def generate():
        return str(uuid.uuid4())
