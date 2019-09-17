from entity.models import Entity
from partner.models import Partner, Service
from transaction.exceptions import TransactionPipelineError
import time
import uuid
import redis


class TransactionPipeline:

    def __init__(self,data):
        self.data = data
        self.entity = None
        self.partner = None
        self.service = None

        #Transaction amount
        self.amount = self.data['amount']

        #Redis object
        self.redis_connection = None
        self.HOST = "redis"
        self.PORT = 6379

        #queue jeton
        self.lockname = self.data['entity_reference']


    def retreive_entity(self):
        try:
            self.entity = Entity.objects.get(reference=self.data['entity_reference'],status=True)
            return self.entity
        except Entity.DoesNotExist:
            return TransactionPipelineError(message='INCORRECT_ENTITY_OR_INCORRECT_ENTITY_STATUS')

    def retreive_partner(self):
        try:
            self.service = Service.objects.get(reference = self.data['service_reference'])
            self.partner = self.service.partner
            return self.partner
        except Service.DoesNotExist:
            return TransactionPipelineError(message='INCORRECT_SERVICE_OR_INCORRECT_SERVICE_STATUS')


    def get_partner_package_obj(self):
        class_name = 'Services'
        module = __import__('transaction.services.%s'%self.partner.brand_name.lower(), fromlist=[class_name])
        klass = getattr(module, class_name)
        #Return obj
        return klass()

    def prepare(self):

        #set entity
        self.retreive_entity()

        #set partner
        self.retreive_partner()

        #Check entity balance
        if self.entity.has_enough_balance(self.amount) == False:
            return TransactionPipelineError(message='INSUFFICIENT_BALANCE_ERROR')

        return True


    def acquire_lock(self, _redis_connection, acquire_timeout=10):

        """
        Acquire queue lock in redis
        """

        try:
            identifier = str(uuid.uuid4())
            end = time.time() + acquire_timeout
            lockname = 'lock:' + self.lockname
            while time.time() < end:

                if _redis_connection.setnx(lockname, identifier):
                    return identifier

                time.sleep(.005)
        except Exception as err:
            print (err)

        return False

    def release_lock(self,identifier,_redis_connection):


        """
        Release queue lock in redis
        """
        pipe = _redis_connection.pipeline(True)
        lockname = 'lock:' + self.lockname
        while True:
            try:
                pipe.watch(lockname)
                if pipe.get(lockname).decode('utf-8') == identifier:
                    pipe.multi()
                    pipe.delete(lockname)
                    pipe.execute()
                    return True

                pipe.unwatch()
                break
            except redis.exceptions.WatchError as err:
                print (err)

        return False

    def connect_to_redis(self,host,port):
        try:
            return redis.Redis(host=host,port=port)
        except redis.exceptions.ConnectionError:
            return TransactionPipelineError(message='REDIS_CONNECTION_ERROR')
        except Exception:
            return TransactionPipelineError(message='REDIS_CONNECTION_ERROR')

    def close_connection_to_redis(self,_redis_connection):
        _redis_connection.close()


    def run(self):

        #redis connection
        self.redis_connection = self.connect_to_redis(host=self.HOST,port=self.PORT)

        identifier = self.acquire_lock(self.redis_connection)
        if identifier is False :
            #Reject transaction , unable to lock redis key
            return TransactionPipelineError(message='REDIS_KEY_LOCK_ERROR')

        partner_class_obj = self.get_partner_package_obj()

        pipe = self.redis_connection.pipeline(True)
        try:
            pipe.watch(identifier) # Watch the lockname

            #partner_class_obj.payment_confirmation(self.data)
            print ("A")
            print ("B")
            print ("C")

            pipe.unwatch() #Unwatch the lock

            return True
        except redis.exceptions.WatchError as err:
            print (err)
            return TransactionPipelineError(message='REDIS_WATCH_LOCK_ERROR')
        finally:
            #finally release lock
            self.release_lock(identifier,self.redis_connection)
