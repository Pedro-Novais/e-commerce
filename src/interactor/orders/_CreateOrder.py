class CreateOrder:
    def __init__(self, request):
        self.request = request
        
    def action(self):
        print("teste de api")
        response = {
            "msg": "certo",
            "code": 200
        }
        return response
