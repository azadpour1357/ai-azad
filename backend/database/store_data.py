from connection import get_database_connection
from mongo_connection import documents_collection

def save_to_postgres(text):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tax_data (document_text) VALUES (%s)", (text,))
    conn.commit()
    cursor.close()
    conn.close()

def save_to_mongo(data):
    documents_collection.insert_one(data)
