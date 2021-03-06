import falcon, json

class ObjRequestClass(object):
    __json_content = {}

    user = {
        'AccNo': 4321,
        'Name': 'user1',
        'Balance': 2000,
        'Password': '9921'
    }

    #Checking json input
    def __validate_json_input(self, req):
        try:
            self.__json_content = json.loads(req.stream.read())
            print('json from client is validated!')
            return True
        except:
            self.__json_content = {}
            print('json from client is not validated!')
            return False

    #Get request to Check Account Balance
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

        validated = self.__validate_json_input(req)

        output = {
            'status' : 200,
            'msg' : None
        }

        if(validated == True):
            if 'AccNo' in self.__json_content and 'Password' in self.__json_content:
                if((self.__json_content['AccNo'] == self.user['AccNo']) and (self.__json_content['Password'] == self.user['Password'])):
                    output['msg'] = 'User Details \n Account Number : {0}\n Name : {1}\n Balance : {2}'.format(self.user['AccNo'], self.user['Name'], self.user['Balance'])  
                else:
                    output['msg'] = 'Please check Account number and password.'                      
            else:
                output['status'] = 404
                output['msg'] = 'json input need AccNo and Password params'                
        else:
            output['status'] = 404
            output['msg'] = 'json input is not validated'

        res.body = json.dumps(output)

    #Post request for Cash Withdrawal and Cash Deposit Actions
    def on_post(self, req, res):
        res.status = falcon.HTTP_200

        validated = self.__validate_json_input(req)

        output = {
            'status' : 200,
            'msg' : None
        }

        valid = True

        if(validated == True):
            if 'AccNo' not in self.__json_content:
                valid = False
            if 'Password' not in self.__json_content:
                valid = False
            if 'Action' not in self.__json_content:
                valid = False
            if 'Amount' not in self.__json_content:
                valid = False

            if(valid == True):
                if((self.__json_content['AccNo'] == self.user['AccNo']) and (self.__json_content['Password'] == self.user['Password'])):
                    if(self.__json_content['Action'] == 'withdrawal'):
                        if(self.user['Balance'] > self.__json_content['Amount']):
                            self.user['Balance'] = int(self.user['Balance']) - int(self.__json_content['Amount'])

                            output['msg'] = 'Withdrawal Successful! \n Current Balance : {0}'.format(self.user['Balance'])
                        else:
                            output['msg'] = 'Insufficient balance'
                        
                    elif(self.__json_content['Action'] == 'deposit'):
                        self.user['Balance'] = int(self.user['Balance']) + int(self.__json_content['Amount'])

                        output['msg'] = 'Deposit Successful! \n Current Balance : {0}'.format(self.user['Balance'])
                else:
                    output['msg'] = 'Please check Account number and Password.'
            else:
                output['status'] = 404
                output['msg'] = 'json input need AccNo, Password, Action and Amount params'
        else:
            output['status'] = 404
            output['msg'] = 'json input is not validated'

        res.body = json.dumps(output)

    #Put Request for Change Passward
    def on_put(self, req, res):
        res.status = falcon.HTTP_200

        validated = self.__validate_json_input(req)

        output = {
            'status' : 200,
            'msg' : None
        }

        update = False

        if(validated == True):
            if 'AccNo' in self.__json_content and 'OldPassword' in self.__json_content and 'NewPassword' in self.__json_content:
                if(self.__json_content['AccNo'] == self.user['AccNo']):
                    if(self.__json_content['OldPassword'] == self.user['Password']):
                        self.user['Password'] = self.__json_content['NewPassword']
                        output['msg'] = 'Password changed successfully.' 
                    else:
                        output['msg'] = 'Wrong Old Password.'  
                else:
                    output['msg'] = 'This Account number not exists.'                    
            else:
                output['status'] = 404
                output['msg'] = 'json input need AccNo, OldPassword, NewPassword params'
        else:
            output['status'] = 404
            output['msg'] = 'json input is not validated'

        res.body = json.dumps(output)

api = falcon.API()

obj = ObjRequestClass()

api.add_route('/example',obj)