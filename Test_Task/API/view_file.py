from rest_framework.views import APIView
from rest_framework.response import Response
import json
from Test_Task.task_app.Model import filemodel

class ProcessPayment(APIView):
    def post(self, request):
        try:
            if self.request.query_params.get("Action") == "INSERT":
                jsondata = json.loads(request.body.decode('utf-8'))
                obj = filemodel.Sales_Model()
                obj.Action = self.request.query_params.get("Action")
                value = int(jsondata.get('Params').get('credit_amount'))
                if (value < 20):
                    jsondata.get('Params').update({"credit_gateway":"CheapPaymentGateway"})
                elif (value > 20 and value <= 500) :
                    jsondata.get('Params').update({"credit_gateway": "ExpensivePaymentGateway"})
                else:
                    jsondata.get('Params').update({"credit_gateway": "PremiumPaymentGateway"})
                obj.jsonData = json.dumps(jsondata.get('Params'))
                obj.json_data = {}
                ld_out_message = obj.process_payment()
                msg = ld_out_message[0].split(",")
                if msg[0] == 'SUCCESS':
                    ld_dict = {
                               "MESSAGE": msg[0]}
                else:
                    ld_dict = {"MESSAGE": 'ERROR_OCCURED.' + ld_out_message.get("MESSAGE")}

                return Response(ld_dict)

            elif self.request.query_params.get("Group") == "FILE_SUMMARY":
                jsondata = json.loads(request.body.decode('utf-8'))
                obj = filemodel.Sales_Model()
                obj.Action = jsondata.get('Params').get('Action')
                ld_out_message = obj.get_smry_data()
                ld_dict = {"DATA": json.loads(ld_out_message.to_json(orient='records')),
                           "MESSAGE": "FOUND"}
                return Response(ld_dict)
        except Exception as e:
            return Response({"MESSAGE": "ERROR_OCCURED", "DATA": str(e)})

