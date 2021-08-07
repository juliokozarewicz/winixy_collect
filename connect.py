from configs import *
import pandas as pd
from datetime import datetime
from connect_book import cnx_book
from email_report import *
from cnx_db import Sqlconex
import _thread
import socket
from cnx_server import *


status_cnx_ohlc = '0'
status_cnx_tt = '0'
status_book = '0'

cnx_server = Serverconex()

def cnx_ohlc():
    """
    Função que coleta os dados passados do ativo alvo:
    Open;
    High;
    Low;
    Close;
    Volume;
    Outras informações que podem ser úteis;
    """

    try:
        global status_cnx_ohlc
        date = datetime.now()
        current_date_time = pd.Series(date)

        cnx_server.server_conex()
        recebe = cnx_server.rec_data(ENV_OHLC)

        if len(recebe) < 250 or len(recebe) > 2000:
            return

        df_data_input = pd.DataFrame(recebe.decode('utf-8')).T
        df_data_input = df_data_input.drop(df_data_input.columns[
                                           [
                                           3, 6, 13, 15, 16, 17, 24, 26,
                                           27, 28, 29, 35, 36, 37, 38, 39,
                                           40, 41, 42, 43, 46, 47, 48, 49,
                                           50, 51, 52, 53, 54, 55, 56, 57,
                                           58, 59, 60, 61, 62, 63, 64, 65,
                                           66, 67, 68, 69, 70, 71, 72, 73,
                                           74, 75, 76, 77, 78, 79, 80, 81,
                                           82, 83, 84, 85, 86, 87, 88, 89
                                           ] ], axis = 1 )
        df_data_input = pd.concat( [current_date_time,
                                    df_data_input],
                                    axis=1,
                                    ignore_index=True).loc[0]

        sql = f"""

        INSERT INTO {OHLCV}

        (
        time_stamp,
        ticker,
        last_price,
        var_pts,
        price_buy,
        price_sell,
        open,
        high,
        low,
        close,
        volume,
        time,
        num_buss,
        status,
        due_date,
        lote_min,
        dias_venc,
        dias_uteis_venc,
        var_prct,
        data_current,
        var_prct_week,
        var_prct_mont,
        var_prct_year,
        var_prct_last_30d,
        var_prct_last_12mon
        )

        VALUES

        (
        '{df_data_input[0]}',
        '{df_data_input[1]}',
        '{df_data_input[2].replace('.', '')}',
        '{df_data_input[3].replace('.', '')}',
        '{df_data_input[4].replace('.', '')}',
        '{df_data_input[5].replace('.', '')}',
        '{df_data_input[6].replace('.', '')}',
        '{df_data_input[7].replace('.', '')}',
        '{df_data_input[8].replace('.', '')}',
        '{df_data_input[9].replace('.', '')}',
        '{df_data_input[10]}',
        '{df_data_input[11]}',
        '{df_data_input[12]}',
        '{df_data_input[13]}',
        '{df_data_input[14]}',
        '{df_data_input[15]}',
        '{df_data_input[16]}',
        '{df_data_input[17]}',
        '{df_data_input[18].replace(',', '.')}',
        '{df_data_input[19]}',
        '{df_data_input[20].replace(',', '.')}',
        '{df_data_input[21].replace(',', '.')}',
        '{df_data_input[22].replace(',', '.')}',
        '{df_data_input[23].replace(',', '.')}',
        '{df_data_input[24].replace(',', '.')}'
        )

        """

        env_dados_ohlc = Sqlconex(sql).env_com_db()
        status_cnx_ohlc = 1
        return 

    except Exception as erro :
        status_cnx_ohlc = f"ohlcv: {erro}"
        return 

def cnx_tt() :
    """
    Coleta de dados do Times and Trades, o sistema acessa a informação 
    disponibilizada, no momento, através do servidor e faz a coleta,
    salvando os dados ao longo do tempo.
    """

    try:
        global status_cnx_tt
        date_tt = datetime.now()
        current_date_time_tt = pd.Series(date_tt)

        cnx_server.server_conex()
        recebe_tt = cnx_server.rec_data(ENV_TT)
 
        df_data_input_tt = pd.DataFrame(recebe_tt.decode('utf-8'))
        df_data_input_tt = df_data_input_tt.replace(ENV_TT + ATIVO, ATIVO)
        df_data_input_tt = df_data_input_tt.T

        df_data_input_tt = pd.concat([current_date_time_tt, df_data_input_tt],
                                     axis=1, ignore_index=True).loc[0]

        sql_tt = f"""

        INSERT INTO {TIMES_TRADES}

        (
        time_stamp,
        ticker,
        numero,
        hora,
        price,
        qtd,
        corr_compr,
        corr_vend,
        tipo_agress
        )

        VALUES

        (
        '{df_data_input_tt[0]}',
        '{df_data_input_tt[1]}',
        '{df_data_input_tt[2]}',
        '{df_data_input_tt[3]}',
        '{df_data_input_tt[4].replace('.', '')}',
        '{df_data_input_tt[5]}',
        '{df_data_input_tt[6]}',
        '{df_data_input_tt[7]}',
        '{df_data_input_tt[8]}'
        )

        """

        env_dados_tt = Sqlconex(sql_tt).env_com_db()
        status_cnx_tt = 1
        return

    except Exception as erro_tt:
        status_cnx_tt = f"times and trades: {erro_tt}"
        return

def statuslog():
    """
    Função que gera o log de status do funcionamento da coleta.
    """

    try:
        date = datetime.now()

        status_log = pd.DataFrame(
                                  pd.concat(
                                  [
                                  pd.Series(date),
                                  pd.Series(status_cnx_ohlc),
                                  pd.Series(status_cnx_tt),
                                  pd.Series(status_book)
                                  ], 
                                  axis=1, ignore_index=True
                                  )
                                  ).loc[0]

        sql = f"""

        INSERT INTO {STATUS_CONEX}

        (
        time_stamp,
        status_ohlc,
        status_tt,
        status_book
        )

        VALUES

        (
        '{status_log[0]}',
        '{status_log[1]}',
        '{status_log[2]}',
        '{status_log[3]}'
        )

        """

        env_dados = Sqlconex(sql).env_com_db() 

        if (status_log[1] != 1 or
            status_log[2] != 1 ) :
            report_email_conex()

        return

    except Exception as erro_log :
        return f"connect: {erro_log}"


while True :
    date = datetime.now()
    current_hour = (f"{date.hour:02}:{date.minute:02}")

    if (current_hour >= OPEN_MKT and
        current_hour <  CLOSE_MKT and
        date.isoweekday() != 6 and
        date.isoweekday() != 7 ) :
        cnx_ohlc()
        cnx_tt()
        cnx_book()
        statuslog()
