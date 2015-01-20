from unittest import TestCase

from mock import patch

from unicore.google.tasks import pageview


class TestTasks(TestCase):

    @patch('urllib2.urlopen')
    def test_pageview(self, mock_request):
        mock_request.return_value = True
        pageview('profile_id', 'client_id', {
            'path': 'foo',
            'user_agent': 'user agent',
            'uip': 'the-ip',
            'dr': 'referrer',
            'dh': 'domain',
        })
        mock_request.assert_called_with('foo')
