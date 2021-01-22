import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
conn = sqlite3.connect('chinook.db')

query_invoice = '''
        SELECT customers.FirstName|| ' ' ||customers.LastName AS 'name', SUM(invoices.Total) AS 'total_expense'
        FROM invoices
        JOIN customers ON customers.CustomerId=invoices.InvoiceId
        WHERE InvoiceDate BETWEEN "2009-02-01 00:00:00" AND "2009-06-23 00:00:00"
        GROUP BY name ORDER BY total_expense DESC
        '''
data_invoice = pd.read_sql_query(query_invoice,conn)
data_invoice.head()

plt.figure(figsize=(14,8))
plt.bar(data_invoice['name'], data_invoice['total_expense'], color='b')
plt.xticks(rotation=90)
plt.grid(True, axis='y')

query_country = '''
                SELECT BillingCountry, COUNT(BillingCountry) AS 'count_country'
                FROM invoices
                WHERE InvoiceDate BETWEEN '2009-02-01 00:00:00' AND '2009-06-23 00:00:00'
                GROUP BY BillingCountry
                ORDER BY count_country DESC;
                '''
data_country = pd.read_sql_query(query_country, conn)
data_country.head()

plt.figure(figsize=(12,8))
plt.bar(data_country['BillingCountry'], data_country['count_country'], color='b')
plt.xticks(rotation=90)