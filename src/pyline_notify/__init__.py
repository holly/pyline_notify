import os, sys, io
import re
import requests

__author__      = "holly"

class PyLINENotify():

    LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, token):
        self.token = token

    def notify(self, message, **kwargs):

        data    = { "message": message }
        headers = { "Authorization": "Bearer {0}".format(self.token) }
        files   = {}

        for key in kwargs:
            if key == "imageFile":
                if type(kwargs[key]).__name__ == "BufferedReader":
                    files[key] = kwargs[key]
                else:
                    files[key] = open(kwargs[key], "rb")
            else:
                data[key] = kwargs[key]
        r = requests.post(self.__class__.LINE_NOTIFY_URL, headers=headers, data=data, files=files)
        rate_limit_headers = {}
        for key, val in  r.headers.items():
            if re.match(r'^X\-.*', key):
                rate_limit_headers[key] = val

        json = r.json()
        return Response(json=r.json(), rate_limit_headers=rate_limit_headers)

class Response():

    def __init__(self, json={}, rate_limit_headers={}):
        self.json = json
        self.rate_limit_headers = rate_limit_headers

    def is_success(self):
        return True if self.status() == 200 else False

    def status(self):
        return self.json["status"]

    def message(self):
        return self.json["message"]
