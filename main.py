import MySQLdb
import pandas as pd
from date import *

def main():
    db = MySQLdb.Connection(host='localhost', user='root', passwd='estatistica',db='Sakila_pt')
    query = ("select primeiro_nome, valor from cliente \
    inner join pagamento \
    on cliente.cliente_id = pagamento.cliente_id \
    where valor > 5 \
    order by valor desc")
    cursor = db.cursor()

    cursor.execute(query, args = None)
    rows = cursor.fetchall()
    lrows = []
    for row in rows:
        lrows.append(list(row))

    #colnames = tuple([desc[0] for desc in cursor.description])
    colnames = []
    for desc in cursor.description:
        colnames.append(desc[0])
    tuple(colnames)

    df = pd.DataFrame(lrows, columns = colnames)

    df.to_csv("data_frame", sep='\t', encoding='utf-8')
if __name__ == "__main__":
    main_date()
    main()
