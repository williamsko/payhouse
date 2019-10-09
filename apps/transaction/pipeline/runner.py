from entity.models import Entity
from partner.models import Partner, Service
from utils.exceptions import TransactionPipelineError
import time
import uuid
import redis


class TransactionPipelineRunner :
    def __init__(self,t_pipeline):
        self.t_pipeline = t_pipeline

        #Redis object
        self.HOST = "redis"
        self.PORT = 6379
        self.redis_connection = None

    def run(self):
        #redis connection
        self.redis_connection = self.t_pipeline.connect_to_redis(host=self.HOST,port=self.PORT)

        identifier = self.t_pipeline.acquire_lock(self.redis_connection)
        if identifier is False :
            #Reject transaction , unable to lock redis key
            return TransactionPipelineError(message='REDIS_KEY_LOCK_ERROR')

        partner_api_class_obj = self.t_pipeline.get_partner_package_obj()
        partner_api_class_obj.set_entity(self.t_pipeline.entity)
        partner_api_class_obj.set_partner(self.t_pipeline.partner)
        partner_api_class_obj.set_service(self.t_pipeline.service)

        pipe = self.redis_connection.pipeline(True)
        try:
            pipe.watch(identifier) # Watch the lockname

            result = partner_api_class_obj.execute()
            print ("**********")
            print (result)
            print ("*********")

            partner_api_class_obj.create_transaction(result)

            pipe.unwatch() #Unwatch the lock

            return True
        except redis.exceptions.WatchError as err:
            print (err)
            return TransactionPipelineError(message='REDIS_WATCH_LOCK_ERROR')
        finally:
            #finally release lock
            self.t_pipeline.release_lock(identifier,self.redis_connection)
