class Error(Exception):
    pass


class NotFoundError(Error):
    def __init__(self, message):
        self.message = message
