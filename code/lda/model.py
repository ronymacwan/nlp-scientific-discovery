import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('processed_arxiv_data.csv') 

# document-term matrix using the cleaned summaries
vectorizer = CountVectorizer()
doc_term_matrix = vectorizer.fit_transform(df['cleaned_summary']) 

# initialize and fit the LDA model
n_components = 5  # number of topics
lda_model = LatentDirichletAllocation(n_components=n_components, random_state=42)
lda_model.fit(doc_term_matrix)

def print_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx + 1}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

feature_names = vectorizer.get_feature_names_out()
print_topics(lda_model, feature_names, no_top_words=20) 