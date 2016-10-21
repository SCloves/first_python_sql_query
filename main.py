import MySQLdb

# Open database connection
con = MySQLdb.connect(host='localhost', user='root', passwd='estatistica',db='Sakila_pt')

# prepare a cursor object using cursor() method
c = con.cursor()

# execute SQL query using execute() method.
c.execute("use Sakila_pt")
c.execute("select primeiro_nome, valor from cliente \
inner join pagamento \
on cliente.cliente_id = pagamento.cliente_id \
where valor > 5 \
order by valor desc")
resultado = c.fetchall()
