import mysql.connector

# Adapted from https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file
secrets = {}
with open("secrets_sqlmode.txt") as myfile:
    for line in myfile:
        key, value = line.partition("=")[::2]
        secrets[key.strip()] = value.strip()

def get_pdf_from_doi(given_doi):
  mydb = mysql.connector.connect(
    host=secrets['host'],
    user=secrets['user'],
    password=secrets['password'],
    database=secrets['database']
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT doi, pdf FROM papers")
  myresult = mycursor.fetchall()

  known_dois = {}
  for x in myresult:
    known_dois[x[0]] = x[1]

  return known_dois[given_doi]