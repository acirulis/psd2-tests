import psycopg2
import logging

# https://docs.python.org/3/howto/logging.html#logging-levels
logging.basicConfig(filename='application.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

try:
    conn = psycopg2.connect("dbname=psd2 user=psd2")
    cur = conn.cursor()
    cur.execute('select * from settings')
    x = cur.fetchall()
    for i in x:
        print(i)
except Exception as ex:
    # except psycopg2.OperationalError as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
