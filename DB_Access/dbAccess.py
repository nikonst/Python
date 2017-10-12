import mysql.connector

try:
   cnx = mysql.connector.connect(user='root', password='12345',host='127.0.0.1',database='adatabase')
except mysql.connector.Error as err:
   print(err)
else:
    print "Connected..."
    print "------------"

    cur = cnx.cursor()
    cur.execute("SELECT book.title, book.price, author.name, author.sirname FROM book INNER JOIN author ON book.author = author.idauthor ORDER BY book.title")
    print "{:30} {:<10} {:20}".format("Title", "Price", "Author")
    print ""
    for title, price, name, sirname in cur.fetchall():
        print "{:30} {:<10} {:10} {:20}".format(title, price, name, sirname)
    cnx.close()

    print "-----"
    print "Done!"
