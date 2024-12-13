import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis

def fetch_data_from_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        query = "SELECT title, authors, published, summary FROM papers"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching data from database: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def preprocess_data(df):
    df['cleaned_summary'] = df['summary'].str.lower()

    # create the CountVectorizer with stop words removal
    vectorizer = CountVectorizer(stop_words='english')
    
    # fit and transform the cleaned summaries
    corpus_matrix = vectorizer.fit_transform(df['cleaned_summary'])
    
    return df, vectorizer, corpus_matrix  

# topic modeling with LDA
def perform_lda(processed_df, vectorizer, n_topics=5):
    
    lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_model.fit(corpus_matrix)

    return lda_model, corpus_matrix

# function to visualize topics
def visualize_topics(lda_model, vectorizer, corpus_matrix):
    topic_word_matrix = lda_model.components_  # Topic-Word matrix
    doc_topic_dists = lda_model.transform(corpus_matrix)  # Document-Topic matrix
    vocab = vectorizer.get_feature_names_out()
    term_frequency = corpus_matrix.sum(axis=0)

    vis_data = pyLDAvis.prepare(topic_term_dists=topic_word_matrix,
                                 doc_topic_dists=doc_topic_dists,
                                 doc_lengths=[len(d) for d in corpus_matrix.toarray()],
                                 vocab=vocab,
                                 term_frequency=term_frequency.A1)

    pyLDAvis.save_html(vis_data, 'lda_visualization.html')
    print("LDA visualization saved as lda_visualization.html")

if __name__ == "__main__":
    db_name = 'arxiv_papers.db'
    df = fetch_data_from_db(db_name)
    
    if not df.empty:
        processed_df, vectorizer, corpus_matrix = preprocess_data(df)
        
        lda_model, corpus_matrix = perform_lda(processed_df, vectorizer)
        visualize_topics(lda_model, vectorizer, corpus_matrix)
    else:
        print("No data available for processing.")