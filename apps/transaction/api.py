from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from transaction.models import Transaction
from entity.models import Entity
from django.conf.urls import url
from transaction.pipeline import TransactionPipeline
from utils.exceptions import TransactionPipelineError
import json


class TransactionResource(ModelResource):

    def prepend_urls(self):
        return [
           url(r"^transaction/create%s$"  %(trailing_slash()), self.wrap_view('create'), name="create"),
       ]

    class Meta:
        always_return_data = True
        resource_name = 'transaction'
        name = 'transaction'
        queryset = Transaction.objects.all()

    def create(self ,request, **kwargs):
        data = json.loads(request.body)
        try:
            t_pipeline = TransactionPipeline(data)
            t_pipeline.prepare()
            bundle = self.build_bundle(obj=Transaction(), request=request)  # take  obj & request
            bundle = self.full_dehydrate(bundle)
        except Exception as e:
            print (e)
            raise TransactionPipelineError(message="UNKNOWN_ERROR")

        return self.create_response(request, bundle)
