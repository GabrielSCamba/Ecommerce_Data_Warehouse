from datetime import date
from dateutil.relativedelta import relativedelta
import time


from gerar_dados_clientes import gerar_dados_clientes
from gerar_dados_enderecos import gerar_dados_enderecos


data_nasc_inicio = date(1944,1,1)
data_nasc_fim = date(2007,12,31)
data_inicio = date(2020,1,1)
data_fim = date(2020,1,5)



data_atual = data_inicio

while data_atual <= data_fim :
    
    gerar_dados_clientes(data_atual = data_atual,                                               
                    data_nasc_inicio = data_nasc_inicio,                
                    data_nasc_fim = data_nasc_fim                    
                    )
    time.sleep(5)
    gerar_dados_enderecos(data_atual)

    data_atual += relativedelta(days=1)

