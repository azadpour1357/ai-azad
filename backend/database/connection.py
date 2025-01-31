import psycopg2

def get_database_connection():
    return psycopg2.connect(
        dbname="tax_database", user="your_user", password="your_password", host="localhost"
    )
