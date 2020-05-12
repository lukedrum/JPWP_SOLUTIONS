import mysql.connector


def create_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE kalamburyzawody")

def create_tables():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
        database="kalamburyzawody"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE hasla ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     " tresc VARCHAR(255) NOT NULL,"
                     " kategoria VARCHAR(255) NOT NULL,"
                     " UNIQUE(tresc)"
                     ")")

    mycursor.execute("CREATE TABLE zawodnicy ("
                     "id INT AUTO_INCREMENT PROMARY KEY,"
                     " imie VARCHAR(255) NOT NULL,"
                     " nazwisko VARCHAR(255) NOT NULL,"
                     " numer INT NOT NULL,"
                     " UNIQUE(tresc)"
                     ")")

def add_val():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
        database="kalamburyzawody"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO hasla (tresc, kategoria) VALUES (%s, %s)"

    val = [
        ("Strazak", "Zawody"),
        ("Policjant", "Zawody"),
        ("Lekarz", "Zawody"),
        ("Nauczyciel", "Zawody"),
        ("Sarna", "Zwierzęta"),
        ("Dzik", "Zwierzęta"),
        ("Kot", "Zwierzęta")
    ]

    mycursor.execute(sql, val)

    mydb.commit()

def add_players():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
        database="kalamburyzawody"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO zawodnicy (imie, nazwisko, numer) VALUES (%s, %s, %)"

    val = [
        ("Jan", "Kowalski", 1),
        ("Jan", "Nowak", 2),
        ("Fryderyk", "Chopin", 3),
        ("Tadeusz", "Pan", 4)
        ]

    mycursor.execute(sql, val)


    mydb.commit()


def pobierz_hasla(kategoria):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
        database="kalamburyzawody"
    )

    mycursor = mydb.cursor()

    kategoria = "Zawody"

    mycursor.execute("SELECT tresc FROM hasla WHERE kategoria = " + "'" + kategoria + "'")

    myresult = mycursor.fetchall()

    hasla_z_kategorii = []

    for x in myresult:
        hasla_z_kategorii.append(x[0])

    return hasla_z_kategorii


def pobierz_numer_zawodnika():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin",
        database="kalamburyzawody"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT tresc FROM zawodnicy")

    myresult = mycursor.fetchall()

    numery_zawodnikow = []

    for x in myresult:
        numery_zawodnikow.append(x[2])

    return numery_zawodnikow
