import sqlite3
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def fetch_data_from_db(db_name):
    conn = sqlite3.connect(db_name)
    query = "SELECT title, authors, published, summary FROM papers"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    # set of English stop words
    stop_words = set(stopwords.words('english'))

    # step 1: lowercasing the summary
    df['cleaned_summary'] = df['summary'].str.lower()

    # step 2: tokenization and stop word removal
    df['cleaned_summary'] = df['cleaned_summary'].apply(word_tokenize) 
    df['cleaned_summary'] = df['cleaned_summary'].apply(lambda x: [word for word in x if word not in stop_words])  # Remove stop words

    # step 3: join words for display if necessary
    df['word_list'] = df['cleaned_summary'].apply(lambda x: ', '.join(x))  

    return df

if __name__ == "__main__":
    db_name = 'arxiv_papers.db'
    df = fetch_data_from_db(db_name)
    
    processed_df = preprocess_data(df)
    
    output_file = 'processed_arxiv_data.csv'
    processed_df.to_csv(output_file, index=False) 
    print(f"Processed data saved to {output_file}.")