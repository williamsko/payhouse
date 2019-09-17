import json
from tastypie.exceptions import TastypieError
from tastypie.http import HttpAccepted
from transaction.errors import API_ERRORS
class TransactionPipelineError(TastypieError):
    """
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.
    """

    def __init__(self,message):
        self._response = {
            "message": message,
            "code": API_ERRORS[message]
            }

    @property
    def message(self):
        return self._response["message"]

    @property
    def response(self):
        return HttpAccepted(
            json.dumps(self._response),
            content_type='application/json')
