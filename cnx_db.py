from configs import *
import psycopg2


class Sqlconex:
    """
    Faz conexão com o banco de dados, para facilitar a leitura, 
    posteriormente e conforme a demanda, será criado um método 
    separado para cada tipo de função executada.
    """

    def __init__(self, rec_info):
        self.cnx_sql = psycopg2.connect(host=SQL_HOST,
                                        database=SQL_DATABASE,
                                        user=SQL_USER,
                                        password=SQL_PASSWORD)
        self.env_sql = rec_info
        return

    def env_com_db(self):
        cur = self.cnx_sql.cursor()
        cur.execute(self.env_sql)
        self.cnx_sql.commit()
        self.cnx_sql.close()
        return

    def rec_data(self):
        cur = self.cnx_sql.cursor()
        cur.execute(self.env_sql)
        rec_db = cur.fetchall()
        self.cnx_sql.close()
        return rec_db

