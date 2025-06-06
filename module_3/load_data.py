# Takes cleaned grad cafe entries and loads into PostgreSQL database

import json
import psycopg2
from datetime import datetime

# ---- CONFIGURE CONNECTION ----
conn_info = {
    "dbname": "postgres",
    "user": "samiraahmed",
    "password": "",
    "host": "127.0.0.1",  # or another host
    "port": 5432
}

# ---- LOAD JSON FILE ----
def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# ---- CREATE TABLE ----
def create_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            p_id SERIAL PRIMARY KEY,
            program TEXT,
            comments TEXT,
            date_added DATE,
            url TEXT,
            status TEXT,
            term TEXT,
            us_or_international TEXT,
            gpa FLOAT,
            gre FLOAT,
            gre_v FLOAT,
            gre_aw FLOAT,
            degree TEXT
        );
    """)

# ---- TRANSFORM AND INSERT DATA ----
def insert_data(cur, data):
    for entry in data:
        program = f"{entry['university']} - {entry['program']}"
        comment = entry.get("comment")
        try:
            date_added = datetime.strptime(entry.get("added_on"), "%B %d, %Y").date()
        except:
            date_added = None
        url = entry.get("applicant_url")
        status = entry.get("decision")
        term = entry.get("semester")
        nationality = entry.get("nationality")
        gpa = float(entry["gpa"]) if entry.get("gpa") else None
        gre = float(entry["gre"]) if entry.get("gre") else None
        gre_v = float(entry["gre_v"]) if entry.get("gre_v") else None
        gre_aw = float(entry["gre_aw"]) if entry.get("gre_aw") else None
        degree = entry.get("degree")

        cur.execute("""
            INSERT INTO applicants (
                program, comments, date_added, url, status, term,
                us_or_international, gpa, gre, gre_v, gre_aw, degree
            ) VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            );
        """, (
            program, comment, date_added, url, status, term,
            nationality, gpa, gre, gre_v, gre_aw, degree
        ))

# ---- MAIN ----
def main():
    data = load_data("applicant_data.json")
    with psycopg2.connect(**conn_info) as conn:
        with conn.cursor() as cur:
            create_table(cur)
            insert_data(cur, data)
            conn.commit()

if __name__ == "__main__":
    main()
