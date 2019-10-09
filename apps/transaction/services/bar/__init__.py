
from transaction.services import Services as S
import requests
import requests_mock

class Services (S):

    def __init__(self,data):
        S.__init__(self,data)

    def execute(self):
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount('mock', adapter)
        adapter.register_uri('GET', 'mock://test.com', text='data')
        resp = session.get('mock://test.com')
        resp.status_code, resp.text
        return resp.status_code, resp.text
