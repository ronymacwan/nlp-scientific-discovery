import sqlite3
from scrapping import fetch_arxiv_data

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # create a table for storing papers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            authors TEXT NOT NULL,
            published TEXT NOT NULL,
            summary TEXT,
            link TEXT NOT NULL,
            UNIQUE(title, authors, published)  -- Unique combination of title, authors, and published date
        )
    ''')
    conn.commit()
    return conn

def insert_paper(cursor, paper):
    # insert a paper into the database
    try:
        cursor.execute('''
            INSERT INTO papers (title, authors, published, summary, link) VALUES (?, ?, ?, ?, ?)
        ''', (paper['title'], ', '.join(paper['authors']), paper['published'], paper['summary'], paper['link']))
        return True  # Indicate that the paper was added
    except sqlite3.IntegrityError:
        # if the paper already exists (duplicate title, authors, published), just return False
        return False

def store_arxiv_data(search_query, max_results=100, db_name='arxiv_papers.db'):
    papers = fetch_arxiv_data(search_query, max_results)
    
    conn = create_database(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM papers')
    existing_count = cursor.fetchone()[0]

    new_papers_count = 0  # track the number of new papers added
    # insert each paper into the database
    for paper in papers:
        if insert_paper(cursor, paper):
            new_papers_count += 1  

    conn.commit()
    conn.close()

    total_entries = existing_count + new_papers_count
    print(f"{existing_count} papers were already present in the database.")
    print(f"Added {new_papers_count} papers (excluding duplicates).")
    print(f"Total entries: {total_entries}")

if __name__ == "__main__":
    store_arxiv_data("natural language processing", max_results=100)