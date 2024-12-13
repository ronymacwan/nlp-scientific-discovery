from datasets import load_dataset
import pandas as pd

#fetch the papers from huggingface
ds = load_dataset("zelalt/arxiv-papers")
ds_subset = ds['train'][:200]
df = pd.DataFrame(ds_subset)
df.to_csv('ml_papers.csv', index=False)


#clean the summary column
data = pd.read_csv('ml_papers.csv')  

def clean_summary(summary):
    # remove extra spaces, newlines, and quotation marks
    cleaned = summary.replace('\n', ' ').replace('"', '').strip()
    return cleaned

data['cleaned_summary'] = data['summary'].apply(clean_summary)

# reorder columns to place 'cleaned_summary' after 'summary'
columns = ['chunk', 'id', 'title', 'summary', 'cleaned_summary', 'source', 'authors', 'text_length']
data = data[columns]

data.to_csv('cleaned_ml_papers.csv', index=False)