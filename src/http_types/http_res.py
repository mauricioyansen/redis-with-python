class HttpRes:
    def __init__(self, body: dict, status_code: int):
        self.body = body
        self.params = status_code
