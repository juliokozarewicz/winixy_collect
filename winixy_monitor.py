from configs import *
from status_report import *
import time
import os


while True:
    """
    Módulo visual de monitoramento básico do status.
    """

    try:
        time.sleep(1)
        data_report, status_ohlc, status_tt, status_book, qtd_db = status_cnx_repor()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""\033[2;0H \033[1;96m
    =======================================================
    -------------------------------------------------------

         ██     ██ ██ ███    ██ ██ ██   ██ ██    ██
         ██     ██ ██ ████   ██ ██  ██ ██   ██  ██
         ██  █  ██ ██ ██ ██  ██ ██   ███     ████
         ██ ███ ██ ██ ██  ██ ██ ██  ██ ██     ██
          ███ ███  ██ ██   ████ ██ ██   ██    ██

              - C    O   L   L   E   C   T  -


    =======================================================
    -------------------------------------------------------

        \033[;1mATIVO: {ATIVO}
        DATA: {data_report}

        \033[1;97mSTATUS DO OHLCV: {status_ohlc}\033[0;0m
        \033[1;97mSTATUS DO TIMES AND TRADES: {status_tt}\033[0;0m
        \033[1;97mSTATUS DO BOOK: {status_book} \033[0;0m

        \033[1;94mTOTAL DE OBSERVAÇÕES: \033[1;35m{qtd_db}\033[0;0m

    \033[1;96m-------------------------------------------------------
    =======================================================
    """)

    except Exception as erro :
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n\n{erro}')
        time.sleep(1)

