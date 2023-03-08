import pandas as pd
import openpyxl
from twilio.rest import Client
"""
programa que le arquivos excel
busca quem atingiu mais de 60000 em vendas
e envia um sms avisando o gerente de quem bateu a meta para ser bonificd
 usando a lib pandas e openpyxl para manipular arquivos do excel
 e twilio para enviar sms

"""

# Your Account SID from twilio.com/console
account_sid = "AC08a184ff6df695ee1c8fca5ab7dba2f7"
# Your Auth Token from twilio.com/console
auth_token  = "b5b10da5a844cd71fed16fb2728ac030"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
#print(lista_meses)

for mes in lista_meses:
    tb_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tb_vendas['Vendas'] > 55000).any():
       vendedor =  tb_vendas.loc[tb_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
       vendas = tb_vendas.loc[tb_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #print(f'No mes {mes}, o vendedor {vendedor} vendeu {vendas} e bateu a meta')

       message = client.messages.create(
           to="+14698199363",
           from_="+18776792541",
           body=f'teste de envio de sms pelo python,'
                f'no mes de  {mes}, o vendedor {vendedor} vendeu {vendas} e bateu a meta')

       print(message.sid)






   # print(tb_vendas)



