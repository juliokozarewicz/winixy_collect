from configs import *
from cnx_db import Sqlconex
from datetime import datetime
import pandas as pd


def status_cnx_repor():
    """
    Função responsável por devolver o status descritivo da
    coleta de dados do Winixy.
    """

    date = datetime.now()
    current_hour = (f'{date.hour:02}:{date.minute:02}')
    df_req = f"SELECT * FROM {STATUS_CONEX} ORDER BY id DESC;"
    df = pd.DataFrame(Sqlconex(df_req).rec_data())

    status_run = 'Runing...'
    mkt_close = 'CLOSED MARKET'
    date_report = df.iloc[ 1 , 1 ]
    qtd_db = len(df)
    #--------------------------------------------------------------------------
    if (df.iloc[ 1 , 2 ] == '1' and current_hour >= OPEN_MKT and
        current_hour < CLOSE_MKT and df.iloc[ 1 , 1 ] != df.iloc[ 2 , 1 ]):
        status_ohlc = status_run

    elif current_hour < OPEN_MKT or current_hour > CLOSE_MKT  :
        status_ohlc = mkt_close

    else:
        status_ohlc = df.iloc[ 1 , 2 ]
    #--------------------------------------------------------------------------
    if (df.iloc[ 1 , 3 ] == '1' and current_hour >= OPEN_MKT and
       current_hour < CLOSE_MKT and df.iloc[ 1 , 1 ] != df.iloc[ 2 , 1 ]):
        status_tt = status_run

    elif current_hour < OPEN_MKT or current_hour > CLOSE_MKT  :
        status_tt = mkt_close

    else:
        status_tt = df.iloc[ 1 , 3 ]
    #--------------------------------------------------------------------------
    if (df.iloc[ 1 , 4 ] == '1' and current_hour >= OPEN_MKT and
       current_hour < CLOSE_MKT and df.iloc[ 1 , 1 ] != df.iloc[ 2 , 1 ]):
        status_book = status_run

    elif current_hour < OPEN_MKT or current_hour > CLOSE_MKT  :
        status_book = 'CLOSED MARKET'

    else:
        status_book = df.iloc[ 1 , 4 ]
    #--------------------------------------------------------------------------

    return (date_report, status_ohlc, status_tt, status_book, qtd_db)

