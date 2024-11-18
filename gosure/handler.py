from gosure.gosure_api import GosureApi


class Handler:

    def __init__(self, token):
        self.g_api = GosureApi(token)