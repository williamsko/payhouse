from django.test import TestCase
from transaction.pipeline import TransactionPipeline
from transaction.exceptions import TransactionPipelineError
from transaction.errors import API_ERRORS
from entity.models import Entity, EntityBalance
from partner.models import Partner, Service

# Create your tests here.
class TestTransactionPipeline (TestCase):

    def createEntity(self):
        entity = Entity()
        entity.brand_name = "foo"
        entity.reference = "68625189"
        entity.status = True
        entity.save()

    def createPartnerAndService(self):
        partner = Partner()
        partner.brand_name = "bar"
        partner.status = True
        partner.save()

        service = Service()
        service.brand_name = "Cash to Cash"
        service.partner = partner
        service.reference = "78625189"
        service.status = True
        service.save()


    def setUp(self):

        self.HOST = "redis"
        self.PORT = 6379

        self.createEntity()
        self.createPartnerAndService()

        self.data = {"entity_reference" : "68625189","service_reference":"78625189","amount" : 1000}
        self.t_pipeline = TransactionPipeline(self.data)

    def tearDown(self):
        self.data = {}

    def test_retreive_entity_pass(self):
        self.assertEqual("foo",self.t_pipeline.retreive_entity().brand_name)

    def test_retreive_partner_pass(self):
        self.assertEqual("bar",self.t_pipeline.retreive_partner().brand_name)

    def test_connect_to_redis_pass(self):
        self.assertEqual(True,self.t_pipeline.connect_to_redis(self.HOST,self.PORT).ping())


    def test_prepare_fail(self):
        self.assertEqual('INSUFFICIENT_BALANCE_ERROR',self.t_pipeline.prepare().message)


    def test_acquire_and_release_lock(self):
        _redis_connection = self.t_pipeline.connect_to_redis(self.HOST,self.PORT)
        identifier = self.t_pipeline.acquire_lock(_redis_connection)
        self.assertNotEqual(False,identifier)
        self.assertEqual(True,self.t_pipeline.release_lock(identifier,_redis_connection))
        self.t_pipeline.close_connection_to_redis(_redis_connection)


    def test_prepare_pass(self):
        entity = self.t_pipeline.retreive_entity()
        entity.credit(1000,"test_prepare_pass")
        self.assertEqual(True,self.t_pipeline.prepare())

    def test_run_pass(self):
        self.t_pipeline.prepare()
        self.assertEqual(True,self.t_pipeline.run())
