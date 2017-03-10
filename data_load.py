import csv
import psycopg2

PATH = 'invincibles.csv'
try:
    conn = psycopg2.connect("dbname=invincibles0304 user=Emanon805 host=/tmp/")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS squad (kit_num serial PRIMARY KEY, name varchar, pos varchar, dob varchar, nat varchar, apps varchar, goals integer, assists integer, mins integer);")

    with open(PATH, 'r') as f:
        catergories = {'fieldnames': ('kit_num', 'name', 'pos', 'dob', 'nat', 'apps', 'goals', 'assists', 'mins'), 'delimiter': ','}
        reader = csv.DictReader(f, **catergories)
        next(reader, None)
        for row in reader:
            cur.execute("INSERT INTO squad (kit_num, name, pos, dob, nat, apps, goals, assists, mins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (row['kit_num'], row['name'], row['pos'], row['dob'], row['nat'], row['apps'], row['goals'], row['assists'], row['mins']))

    cur.execute("SELECT * FROM squad;")
    cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

except psycopg2.OperationalError:
    print("The database does not exist")
except FileNotFoundError:
    print("File: {} does not exist".format(PATH))
except psycopg2.IntegrityError:
    print("The contents of {} have already been uploaded to the database".format(PATH))
