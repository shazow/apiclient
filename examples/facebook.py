"""
Facebook OpenGraph API. Usage:

api = FacebookAPI()
r = api.call('/', ids='shazow,minecraft')
"""

from apiclient import APIClient


class FacebookError(Exception):
    def __init__(self, type, message, response=None):
        self.type = type
        self.message = message
        self.response = response

    def __str__(self):
        return "%s (%s)" % (self.type, self.message)

    def __repr__(self):
        return "%s(type=%s)" % (self.__class__.__name__, self.type)


class FacebookAPI(APIClient):
    BASE_URL = 'https://graph.facebook.com/'

    def _handle_response(self, response):
        r = super(FacebookAPI, self)._handle_response(response)

        has_error = r.get('error')
        if not has_error:
            return r

        raise FacebookError(has_error['type'], has_error['message'], response=response)
