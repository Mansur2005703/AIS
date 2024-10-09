import json


class Car():
    models = ['Lexus 1', 'Toyota 1', 'BMW 2']
   
    def get(self, model_name):
        return [model for model in self.models if model_name in model]

        
        
class Response():
    response_data = None
    
    def __init__(self, data):
        self.response_data = data
            
    def __str__(self) -> str:
        return json.dumps({
            "data": self.response_data
        })
    
        
car = Car().get('2')
    
def user(request):
    return Response(car)
