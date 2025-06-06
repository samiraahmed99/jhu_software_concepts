# Answer following questions by creating queries

# Something to keep in mind :
# | Field    | Min | Max  | Notes                             |
# | -------- | --- | ---- | --------------------------------- |
# | `gpa`    | 0.0 | 4.33 | Some schools use 4.0, others 4.33 |
# | `gre`    | 260 | 340  | Total GRE score                   |
# | `gre_v`  | 130 | 170  | Verbal score                      |
# | `gre_aw` | 0.0 | 6.0  | In 0.5 increments                 |

import psycopg2

conn_info = {
    "dbname": "postgres",
    "user": "samiraahmed",
    "password": "",
    "host": "localhost",
    "port": 5432
}

# 1. How many entries do you have in your database who have applied for Fall 2025?

def query_1(cur):
    cur.execute("SELECT COUNT(*) FROM applicants WHERE term = 'fall 2025';")
    count = cur.fetchone()[0]
    print(f"1. Number of applicants for Fall 2025: {count}")


# 2. What percentage of entries are from international students (not American or Other) (to two decimal places)?

def query_2(cur):
    cur.execute("""
        SELECT ROUND(100.0 * COUNT(*) FILTER (
            WHERE us_or_international = 'international'
        ) / COUNT(*), 2) FROM applicants;
    """)
    print("2. The percentage of International Students:", f"{cur.fetchone()[0]}%")


# 3. What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?

def query_3(cur):
    cur.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2),
               ROUND(AVG(gre)::numeric, 2),
               ROUND(AVG(gre_v)::numeric, 2),
               ROUND(AVG(gre_aw)::numeric, 2)
        FROM applicants
        WHERE
            (gpa IS NULL OR (gpa >= 0 AND gpa <= 4.33)) AND
            (gre IS NULL OR (gre >= 130 AND gre <= 170)) AND 
            (gre_v IS NULL OR (gre_v >= 130 AND gre_v <= 170)) AND
            (gre_aw IS NULL OR (gre_aw >= 0 AND gre_aw <= 6));
    """)
    gpa, gre, gre_v, gre_aw = cur.fetchone()
    print(f"3. The average GPA: {gpa}, GRE: {gre}, GRE V: {gre_v}, GRE AW: {gre_aw}")

# 4. What is their average GPA of American students in Fall 2025?

def query_4(cur):
    cur.execute("""
                SELECT ROUND(AVG(gpa)::numeric, 2)
                FROM applicants
                WHERE us_or_international = 'american'
                  AND term = 'fall 2025'
                  AND gpa IS NOT NULL
                  AND gpa BETWEEN 0 AND 4.33;
                """)
    print("4. The average GPA of American students in Fall 2025:", cur.fetchone()[0])


# 5. What percent of entries for Fall 2025 are Acceptances (to two decimal places)?

def query_5(cur):
    cur.execute("""
        SELECT ROUND(100.0 * COUNT(*) FILTER (
            WHERE status ILIKE 'Accepted%' AND term = 'fall 2025'
        ) / NULLIF(COUNT(*) FILTER (WHERE term = 'fall 2025'), 0), 2)
        FROM applicants;
    """)
    print("5. The percent of Acceptances for Fall 2025:", f"{cur.fetchone()[0]}%")


# 6. What is the average GPA of applicants who applied for Fall 2025 who are Acceptances?

def query_6(cur):
    cur.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE term = 'fall 2025'
          AND status ILIKE 'Accepted%'
          AND gpa IS NOT NULL;
    """)
    print("6. The average GPA of Acceptances for Fall 2025:", cur.fetchone()[0])



# 7. How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?

def query_7(cur):
    cur.execute("""
        SELECT COUNT(*)
        FROM applicants
        WHERE program ILIKE '%Johns Hopkins University%Computer Science%'
          AND degree ILIKE '%master%';
    """)
    print("7. The amount of JHU CS Masters Applicants:", cur.fetchone()[0])

# Find invalid entries

# def find_invalid_scores(cur):
#     cur.execute("""
#         SELECT *
#         FROM applicants
#         WHERE
#           gpa IS NOT NULL AND (gpa < 0 OR gpa > 4.33)
#           OR gre IS NOT NULL AND (gre < 260 OR gre > 340)
#           OR gre_v IS NOT NULL AND (gre_v < 130 OR gre_v > 170)
#           OR gre_aw IS NOT NULL AND (gre_aw < 0 OR gre_aw > 6);
#     """)
#     rows = cur.fetchall()
#     print(f"\n🔍 Found {len(rows)} invalid entries:")
#     for row in rows:
#         print(row)

# We define a main function where we call all queries
def main():
    with psycopg2.connect(**conn_info) as conn:
        with conn.cursor() as cur:
            query_1(cur)
            query_2(cur)
            query_3(cur)
            query_4(cur)
            query_5(cur)
            query_6(cur)
            query_7(cur)
          # find_invalid_scores(cur)


if __name__ == "__main__":
    main()