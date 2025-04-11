import os
import psycopg2

# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="microscope_db",
#         user="postgres",
#         password="password"  # <-- Replace this with your actual password
#     )


def get_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])


