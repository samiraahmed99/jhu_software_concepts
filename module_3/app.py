from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# 1. Function to connect to the PostgreSQL database

def get_db_connection():
    """Connect to PostgreSQL database"""
    connection = psycopg2.connect(
        dbname="postgres",
        user="samiraahmed",
        password="",
        host="localhost",
        port=5432
    )
    return connection

# 2. Home route that runs all 7 queries and passes the results to the template
@app.route('/')
def index():
        conn = get_db_connection()
        cur = conn.cursor()

        # Run SQL queries
        cur.execute("SELECT COUNT(*) FROM applicants WHERE term = 'fall 2025';")
        fall_2025_count = cur.fetchone()[0]

        cur.execute("""
                    SELECT ROUND(100.0 * COUNT(*) FILTER (
                        WHERE us_or_international = 'international'
                    ) / COUNT(*), 2)
                    FROM applicants;
                    """)
        percent_international = cur.fetchone()[0]

        cur.execute("""
                    SELECT ROUND(AVG(gpa)::numeric, 2),
                           ROUND(AVG(gre)::numeric, 2),
                           ROUND(AVG(gre_v)::numeric, 2),
                           ROUND(AVG(gre_aw)::numeric, 2)
                    FROM applicants
                    WHERE (gpa IS NULL OR (gpa >= 0 AND gpa <= 4.33))
                      AND (gre IS NULL OR (gre >= 130 AND gre <= 170))
                      AND (gre_v IS NULL OR (gre_v >= 130 AND gre_v <= 170))
                      AND (gre_aw IS NULL OR (gre_aw >= 0 AND gre_aw <= 6));
                    """)
        averages = cur.fetchone()

        cur.execute("""
                    SELECT ROUND(AVG(gpa)::numeric, 2)
                    FROM applicants
                    WHERE us_or_international = 'american'
                      AND term = 'fall 2025'
                      AND gpa IS NOT NULL
                      AND gpa BETWEEN 0 AND 4.33;
                    """)
        avg_gpa_american = cur.fetchone()[0]

        cur.execute("""
                    SELECT ROUND(100.0 * COUNT(*) FILTER (
                        WHERE status ILIKE 'Accepted%' AND term = 'fall 2025'
                    ) / NULLIF(COUNT(*) FILTER (WHERE term = 'fall 2025'), 0), 2)
                    FROM applicants;
                    """)
        percent_accept = cur.fetchone()[0]

        cur.execute("""
                    SELECT ROUND(AVG(gpa)::numeric, 2)
                    FROM applicants
                    WHERE term = 'fall 2025'
                      AND status ILIKE 'Accepted%'
                      AND gpa IS NOT NULL;
                    """)
        avg_gpa_accept = cur.fetchone()[0]

        cur.execute("""
                    SELECT COUNT(*)
                    FROM applicants
                    WHERE program ILIKE '%Johns Hopkins University%Computer Science%'
                      AND degree ILIKE '%master%';
                    """)
        jhu_cs_count = cur.fetchone()[0]

        cur.close()
        conn.close()

        # Pass data to template
        return render_template(
            'index.html',
            fall_2025_count=fall_2025_count,
            percent_international=percent_international,
            averages=averages,
            avg_gpa_american=avg_gpa_american,
            percent_accept=percent_accept,
            avg_gpa_accept=avg_gpa_accept,
            jhu_cs_count=jhu_cs_count
        )


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8000, debug = True)
