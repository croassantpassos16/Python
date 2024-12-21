import pandas as pd
vendas_tabela = pd.read_excel('Vendas.xlsx')

import win32com.client as win32

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

faturamento = vendas_tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
qntProduto = vendas_tabela[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

ticketMedio = (faturamento['Valor Final'] / qntProduto['Quantidade']).to_frame()
ticketMedio = ticketMedio.rename(columns={0:'Ticket Médio'})

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'matheuspp.ronchi@gmail.com'
mail.Subject = 'Relatório Semestral de Vendas das lojas de SP'
mail.HTMLBody = f'''
<p>Prezado, Sr. Matheus</p>

<p>Segue relatório semestral de venda das lojas do estado de São Paulo:</p>

<p>FATURAMENTO:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>QUANTIDADE DE PRODUTOS:</p>
{qntProduto.to_html()}

<p>TICKET MÉDIO DOS PRODUTOS:</p>
{ticketMedio.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}

<p>Qualquer dúvida, estou a disposição</p>
<p>Entrar em contato: Matheus Ronchi, email: matheuspp.ronchi@gmail.com</p>
<p>Att.,</p>
<p>Matheus Ronchi</p>'''

mail.Send()

print('\n The Code Passed\n')
