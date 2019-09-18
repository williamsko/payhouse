
from transaction.services import Services as S


class Services (S):

    def __init__(self,data):
        S.__init__(self,data)

    def execute(self):
        service_reference = self.data["service_reference"]
        print (self.entity.brand_name)
        print (self.partner.brand_name)
        print (self.base_url)

        pass
