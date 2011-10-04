"""
Klout API client. Usage:

    api = KloutAPI('xxxxx')
    r = api.call('/users/show', users='shazow,limedaring')
"""

from apiclient import APIClient_SharedSecret
from urllib import urlencode


class KloutError(Exception):
    STATUS_MAP = {
        200: "OK: Success",
        202: "Accepted: Your request was accepted and the user was queued for processing.",
        401: "Not Authorized: either you need to provide authentication credentials, or the credentials provided aren't valid.",
        403: "Bad Request: your request is invalid, and we'll return an error message that tells you why. This is the status code returned if you've exceeded the rate limit (see below).",
        404: "Not Found: either you're requesting an invalid URI or the resource in question doesn't exist (ex: no such user in our system).",
        500: "Internal Server Error: we did something wrong.",
        501: "Not implemented.",
        502: "Bad Gateway: returned if Klout is down or being upgraded.",
        503: "Service Unavailable: the Klout servers are up, but are overloaded with requests. Try again later.",
    }

    def __init__(self, status, response=None):
        self.status = status
        self.response = response

    def __str__(self):
        return "%s (%s)" % (self.status, self.STATUS_MAP.get(self.status, 'Unknown error.'))

    def __repr__(self):
        return "%s(status=%s)" % (self.__class__.__name__, self.status)


class KloutAPI(APIClient_SharedSecret):
    """
    Methods:
    - klout
    - users/show
    - users/topics
    - soi/influenced_by
    - soi/influencer_of
    """
    BASE_URL = 'http://api.klout.com/1/'

    def _compose_url(self, path, params=None):
        p = dict(key=self.api_key, **(params or {}))

        if params:
            p.update(params)

        return self.BASE_URL + path + '.json' + '?' + urlencode(p)

    def _handle_response(self, response):
        if response.status > 299:
            raise KloutError(response.status, response=response)

        return super(KloutAPI, self)._handle_response(response)

    def call(self, path, **params):
        return self._request('GET', path, params=params)
