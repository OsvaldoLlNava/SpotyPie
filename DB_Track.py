import sqlite3

def main():
    conn = sqlite3.connect("Arma_tu_biblio.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Track
    (ID Text,
    Name Text,
    Artist Text,
    Album Text,
    Duration Text
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()