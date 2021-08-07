from configs import *
from status_report import *
from datetime import datetime, timedelta
import smtplib


def report_email_conex():
    """
    Função que envia um email, a cada x tempo definido em minutos,
    acusando instabilidades na coleta.
    """

    try:
        date_report, status_ohlc, status_tt, status_book, qtd_db = status_cnx_repor()
        date = datetime.now()

        env_cnx_email = f"SELECT * FROM {EMAIL_REPORT} ORDER BY id DESC LIMIT 2;"
        recv_cnx_email = pd.DataFrame( Sqlconex(env_cnx_email).rec_data() )

        if len(recv_cnx_email) == 0:
            email_report_sleep = datetime.strptime('2000-01-01 00:00:00.0000', '%Y-%m-%d %H:%M:%S.%f')
        else:
            time_inc_email = timedelta( minutes = 5 )
            email_report_sleep = recv_cnx_email.iloc[ 0 , 1 ] + time_inc_email

        if date > email_report_sleep :
            cnx_email_erro = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            cnx_email_erro.login(EMAIL_REMETENTE, EMAIL_TOKEN)
            subject = "WINIXY COLLECT - Error Report"
            #--------------------------------------------------------------
            mensagem = (
                "*** Winixy Collect presents instabilities ***"
                f"\n\n{'-' * 55}"
                f"\ntime:\n{date_report}"
                f"\n{'-' * 55}"
                f"\nohlcv:\n{status_ohlc}"
                f"\n{'-' * 55}"
                f"\ntimes and trades:\n{status_tt}"
                f"\n{'-' * 55}"
                f"\nbook:\n{status_book}"
                f"\n{'-' * 55}" )
            #--------------------------------------------------------------
            send_email = f"subject: {subject} \n\n {mensagem}"
            cnx_email_erro.sendmail(EMAIL_REMETENTE,
                                    EMAIL_DESTINATARIO,
                                    send_email)
            cnx_email_erro.quit()
            sql = f"INSERT INTO winixy_collect_winfut.email_report (time_stamp) VALUES ('{date}')"
            env_dados = Sqlconex(sql).env_com_db()

        return

    except Exception as erro :
        return f"email: {erro}"

