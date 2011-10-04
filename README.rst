Tiny framework for building *good* API client libraries thanks to
`urllib3 <https://github.com/shazow/urllib3/>`_.

Highlights
==========

- Threadsafely reuses connections with Keep-Alive (via urllib3).
- Small and easy to understand codebase perfect for extending and building upon.
- Built-in support for rate limiting and request throttling.
- Functional examples for the
  `Klout API <https://github.com/shazow/apiclient/blob/master/examples/klout.py>`_
  and the
  `Facebook OpenGraph API <https://github.com/shazow/apiclient/blob/master/examples/facebook.py>`_.


Examples
========

How to make your own super-simple client API library::

    >>> from apiclient import APIClient
    >>> class AcmePublicAPI(APIClient):
    ...    BASE_URL = 'https://localhost:1234/'

    >>> acme_api = AcmePublicAPI()

    >>> acme_api.call('/hello')
    {'what': 'world'}
    >>> acme_api.call('/echo', params={"ping": "pong"})
    {'ping': 'pong'}


How to add rate limiting to your client API library so that we don't exceed 10
requests per minute::

    >>> from apiclient import RateLimiter
    >>> lock = RateLimiter(max_messages=10, every_seconds=60)
    >>> acme_api = AcmePublicAPI(rate_limit_lock=lock)

    >>> # Get the first 100 pages
    >>> for page in xrange(100):
    ...     # Whenever our request rate exceeds the specifications of the API's
    ...     # RateLimiter, the next request will block until the next request window
    ...     r = acme_api.call('/stream', page=str(page))

For more specific API examples, see the
`examples/ <https://github.com/shazow/apiclient/blob/master/examples/>`_ directory.


Extending
=========

To handle different calling conventions, ``apiclient`` can be extended through
subclassing.

For example, if an API requires that all arguments be JSON encoded, the
``_compose_url`` method could be implemented like this::

    >>> class JSONArgsAPIClient(APIClient):
    ...     def _compose_url(self, path, params=None):
    ...         if params is not None:
    ...             params = dict((key, json.dumps(val))
    ...                            for (key, val) in params.iteritems())
    ...         return APIClient._compose_url(self, path, params=params)

Or if an API returns YAML instead of JSON, the ``_handle_response`` method
could be overridden::

    >>> class YAMLResponseAPIClient(APIClient):
    ...     def _handle_response(self, response):
    ...         return yaml.load(response.data)


TODO
====

- Tests.
- More documentation.
- More types of API handshakes, like OAuth and OAuth2.
- More examples.


Contributing
============

Any contribution is highly encouraged and desired. :)

#. Fork on Github.
#. Make the changes. Bonus points if changes include documentation and tests.
#. Send a pull request.

If you're unsure if it's a good idea,
`open an Issue <https://github.com/shazow/apiclient/issues>`_ or
`contact me <https://github.com/inbox/new/shazow>`_ to discuss your proposal.
Extra juicy bonus points if you pick off some of the items in the **TODO** list.


License
=======

`MIT <https://github.com/shazow/apiclient/blob/master/LICENSE>`_
