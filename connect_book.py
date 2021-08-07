import socket
import pandas as pd
import time
import csv
from datetime import datetime
from configs import ATIVO, HOST, PORT


def cnx_book():
    '''
    
    Montagem da primeira linha do book de ofertas, será importante para
    uma análise de quantidade disponível do ativo na hora de execução
    de uma ordem. Salva um csv na pasta do coletor.

    Para montar um book com mais linhas:
        * A quantidade de linhas será determinada pela variável 'qtd_lin_book';
        * Por padrão será montado apenas a primeira linha;
        * qtd_lin_book = quantidade de linhas desejadas do book;
    
        O book ainda não está finalizado, será melhorado posteriormente a fim
        de se obter mais performance e fidelidade dos dados disponibilizados,
        já que o volume negociado em alguns ativos são tão grandes que o tipo
        de conexão com o servidor não consegue acompanhar.
    
    '''

    try:
        #-----------------------------------------------------------------------
        socket_cnx_book = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cnx_book.settimeout(1)
        socket_cnx_book.connect((HOST, PORT))
        #-----------------------------------------------------------------------

        book_qtdcp = []
        book_pccp = []
        book_pcvd = []
        book_qtdvd = []
        ln_book = 0
        recv_b = 500
        qtd_lin_book = 1

        while ln_book <= qtd_lin_book :

            # QUANTIDADE COMPRA
            #-----------------------------------------------------------------------
            env_paramet_book_qtdcp = str.encode(ENV_BOOK)
            socket_cnx_book.sendall(env_paramet_book_qtdcp)
            recebe1 = socket_cnx_book.recv(recv_b)
            dados_rece_1 = recebe1.decode('utf-8')split()[-1]
            book_qtdcp.append(dados_rece_1)

            # PREÇO COMPRA
            #-----------------------------------------------------------------------
            env_paramet_book_pccp = str.encode(ENV_BOOK)
            socket_cnx_book.sendall(env_paramet_book_pccp)
            recebe2 = socket_cnx_book.recv(recv_b)
            dados_rece_2 = recebe2.decode('utf-8')split()[-1]
            book_pccp.append(dados_rece_2)

            # PREÇO VENDA COMPRA
            #-----------------------------------------------------------------------
            env_paramet_book_pcvd = str.encode(ENV_BOOK)
            socket_cnx_book.sendall(env_paramet_book_pcvd)
            recebe2 = socket_cnx_book.recv(recv_b)
            dados_rece_2 = recebe2.decode('utf-8')split()[-1]
            book_pcvd.append(dados_rece_2)

            # QUANTIDADE VENDA
            #-----------------------------------------------------------------------
            env_paramet_book_qtdvd = str.encode(ENV_BOOK)
            socket_cnx_book.sendall(env_paramet_book_qtdvd)
            recebe4 = socket_cnx_book.recv(recv_b)
            dados_rece_4 = recebe4.decode('utf-8')split()[-1]
            book_qtdvd.append(dados_rece_4)

            # INCREMENTO DO CONTADOR
            ln_book = ln_book + 1

        line1 = pd.concat([pd.DataFrame(book_qtdcp),
                           pd.DataFrame(book_pccp),
                           pd.DataFrame(book_pcvd),
                           pd.DataFrame(book_qtdvd)], 
                           axis=1, ignore_index=True)

        line1 = pd.DataFrame(line1.iloc[1,:]).T
        line1 = line1.rename(columns={0: "qtd_cp", 1: "prc_cp",
                                      2: "prc_vd", 3: "qtd_vd"})

        line1.to_csv('df_book/db_book.csv', index=False)

        status_cnx_book = 1
        return status_cnx_book

    except Exception as erro:
        status_cnx_book = erro

