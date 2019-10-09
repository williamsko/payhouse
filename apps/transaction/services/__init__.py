from os import environ
from transaction.models import Transaction
class Services :

    def __init__(self,data):
        self.data = data
        self.entity = None
        self.partner = None
        self.base_url = None
        self.service = None


    def set_entity(self,entity):
        self.entity = entity

    def set_partner(self,partner):
        self.partner = partner

    def set_service(self,service):
        self.service = service
        self.set_base_url()

    def set_base_url(self):
        local_settings = environ.get("DJANGO_SETTINGS_MODULE")
        if local_settings == "playoff.settings.local":
            self.base_url = self.service.demo_base_url
        else:
            self.base_url = self.service.prod_base_url



    def create_transaction(self,request_response):
        print ("create_transaction")
        transaction = Transaction()

        pass
