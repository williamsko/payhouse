from django.http import JsonResponse


class TransactionPipelineError :
    def __init__(self,message):
        self.message = message

    
