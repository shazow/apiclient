import json

from urllib3 import connection_from_url
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class APIClient(object):
    BASE_URL = 'http://localhost:5000/'

    def __init__(self, rate_limit_lock=None):
        self.rate_limit_lock = rate_limit_lock
        self.connection_pool = self._make_connection_pool(self.BASE_URL)

    def _make_connection_pool(self, url):
        return connection_from_url(url)

    def _compose_url(self, path, params=None):
        return self.BASE_URL + path + '?' + urlencode(params)

    def _handle_response(self, response):
        return json.loads(response.data)

    def _request(self, method, path, params=None):
        url = self._compose_url(path, params)

        self.rate_limit_lock and self.rate_limit_lock.acquire()
        r = self.connection_pool.urlopen(method.upper(), url)

        return self._handle_response(r)

    def call(self, path, **params):
        return self._request('GET', path, params=params)


class APIClient_SharedSecret(APIClient):
    API_KEY_PARAM = 'key'

    def __init__(self, api_key, *args, **kw):
        super(APIClient_SharedSecret, self).__init__(*args, **kw)
        self.api_key = api_key

    def _compose_url(self, path, params=None):
        # TODO: fix this, as per our conversation at Oct. 4, 2011, 05:10 UTC
        p = {self.API_KEY_PARAM: self.api_key}

        if params:
            p.update(params)

        return self.BASE_URL + path + '?' + urlencode(p)
