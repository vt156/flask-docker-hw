import psycopg2
import os

def clean():
    query = "DELETE FROM token WHERE now()-created_at > interval '1 hour"
    conn, c = psycopg2.connect(creds)
    c.query(query)
