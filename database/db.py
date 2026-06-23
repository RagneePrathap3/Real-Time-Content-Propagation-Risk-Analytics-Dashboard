import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="community_risk",
        user="postgres",
        password="Ragnee@postgre33",
        port="5432"
    )

    return conn