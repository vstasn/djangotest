from django.test import TestCase
from elasticsearch.connection import RequestsHttpConnection
from elasticsearch.helpers.test import ElasticsearchTestCase
from unittest.mock import Mock


class TestElastic(ElasticsearchTestCase):
    def test_get(self):
        self.client.get()


"""
class TestRequestsConnection(TestCase):
    def _get_mock_connection(
        self, connection_params={}, status_code=200, response_body="{}"
    ):
        con = RequestsHttpConnection(**connection_params)

        def _dummy_send(*args, **kwargs):
            dummy_response = Mock()
            dummy_response.headers = {}
            dummy_response.status_code = status_code
            dummy_response.text = response_body
            dummy_response.request = args[0]
            dummy_response.cookies = {}
            _dummy_send.call_args = (args, kwargs)
            return dummy_response

        con.session.send = _dummy_send
        return con

    def _get_request(self, connection, *args, **kwargs):
        if "body" in kwargs:
            kwargs["body"] = kwargs["body"].encode("utf-8")

        status, headers, data = connection.perform_request(*args, **kwargs)
        self.assertEquals(200, status)
        self.assertEquals("{}", data)

        timeout = kwargs.pop("timeout", connection.timeout)
        args, kwargs = connection.session.send.call_args
        self.assertEquals(timeout, kwargs["timeout"])
        self.assertEquals(1, len(args))
        return args[0]

    def test_body_attached(self):
        con = self._get_mock_connection()
        request = self._get_request(con, 'GET', '/', body='{"answer": 42}')

        self.assertEquals('http://localhost:9200/', request.url)
        self.assertEquals('GET', request.method)
        self.assertEquals('{"answer": 42}'.encode('utf-8'), request.body)

    def test_http_auth_attached(self):
        con = self._get_mock_connection({'http_auth': 'username:secret'})
        request = self._get_request(con, 'GET', '/')

        self.assertEquals(request.headers['authorization'], 'Basic dXNlcm5hbWU6c2VjcmV0')
"""