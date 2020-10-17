from django.db import connection
import pandas as pd
import json
# from Test_Task.task_app.Model import mfile


class Sales_Model():
    def process_payment(self):
        cursor = connection.cursor()
        parameters = (self.Action,self.jsonData,self.json_data, '')
        cursor.callproc('Sp_Credit_Set', parameters)
        cursor.execute('select @_Sp_Credit_Set_3')
        output_msg = cursor.fetchone()
        return output_msg

    def get_smry_data(self):
        cursor = connection.cursor()
        parameters = (self.Action,'{}','{}' ,'')
        cursor.callproc('Sp_Order_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        rows = list(rows)
        df_grndetail = pd.DataFrame(rows, columns=columns)
        return df_grndetail


    def get_login(self):
        cursor = connection.cursor()
        param = (0, self.code, converttoascii(self.password), '')
        cursor.callproc("sp_client_Get",param)
        columns = [d[0] for d in cursor.description]
        ldict = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.execute('select @_sp_client_Get_3')
        id = cursor.fetchone()
        ldist = [ldict, id]
        return ldist

def converttoascii(password):
    l=len(password)
    newuser=''
    for i in range(0,l):
        tmp=ord(password[i])
        temp = tmp - l
        g=len(str(temp))
        newuser = newuser + ("0" if g < 3 else "") + str(temp)
    return newuser


