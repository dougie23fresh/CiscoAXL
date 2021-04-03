import urllib3
from requests.exceptions import RequestException, HTTPError
from requests.auth import HTTPBasicAuth
from requests import Session


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = 'HIGH:!DH:!aNULL'


class SOAP:
    def __init__(self, url, username=None, password=None, tls_verify=False, timeout=30):
        self.url = url
        self.session = Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.verify = tls_verify
        self.session.timeout = timeout
        # self.session.headers.update(headers)

    def _send_request(self, url, parameters={}, headers={}, payload=None, http_method='GET'):
        result = {'success': False, 'message': '', 'response': ''}
        try:
            self.session.headers = headers
            if http_method in ['GET', 'POST', 'PUT', 'DELETE']:
                if http_method == 'GET':
                    raw_response = self.session.get(url, params=parameters)
                elif http_method == 'POST':
                    raw_response = self.session.post(url, data=payload, params=parameters)
                result = {
                    'success': True,
                    'response': raw_response,
                    'message': f'Successful {http_method} request to: {url}',
                }

        except RequestException as e:
            result = {'success': False, 'message': f'RequestException {http_method} request to: {url} :: {e}'}
        return result

    def _check_response(self, raw_response):

        try:
            # Raise HTTPError error for non-2XX responses
            raw_response['response'].raise_for_status()
        except HTTPError as e:
            raw_response['success'] = False
            raw_response['message'] = f'HTTPError Exception: {e}'
        return raw_response
