# SERVIDOR
ATIVO = ""
HOST = ""
PORT = 80001
ENV_OHLC = ""
ENV_TT = ""
ENV_BOOK = ""

# BANCO DE DADOS
SQL_HOST = HOST
SQL_DATABASE = 'winixy_collect'
SQL_SCHEMA_ATIVO = f"{SQL_DATABASE.lower()}_{ATIVO.lower()}"
SQL_USER = ''
SQL_PASSWORD = ''
EMAIL_REPORT = f"{SQL_SCHEMA_ATIVO}.email_report"
OHLCV = f"{SQL_SCHEMA_ATIVO}.ohlcv"
STATUS_CONEX = f"{SQL_SCHEMA_ATIVO}.ohlcv"
STATUS_CONEX = f"{SQL_SCHEMA_ATIVO}.status_conex"
TIMES_TRADES = f"{SQL_SCHEMA_ATIVO}.times_trades"

# EMAIL
EMAIL_REMETENTE = ''
EMAIL_DESTINATARIO = ['', '']
EMAIL_TOKEN = ''

#OUTRAS
OPEN_MKT = '10:00'
CLOSE_MKT = '18:00'
