# Scientific Discovery: Evaluating Feasibility of Using AI in Writing

This project is submitted for the course **INFO 555 - Applied NLP**. It focuses on the topic of **Scientific Discovery**. Please refer to this file for understanding the GitHub project structure.

**Author**: Rony Macwan  
**Term**: Fall 2024  
**Subject**: INFO 555 Applied NLP  
**Project Title**: Automatic Keyword Extraction, Hypothesis Generation, and Topic Modeling: Evaluating the Feasibility

## GitHub Project Structure

- **`code` folder**: Contains all necessary scripts to reproduce the results.  
  - Scripts with `.ipynb` extension can be imported into **Google Colab** for modification or execution.  
  - Scripts with `.py` extension can be downloaded on any machine with Python installed and executed directly.

- **`writeup` folder**: Contains the PDF version of the project paper for reference and documentation.

- **`dataset` folder**: Contains the dataset used in the project.

## Code

This folder contains the following scripts:

**`automatic keyword generation` folder:**

- **fetch_papers.py**: Fetches papers from Hugging Face and stores them locally.  
  *(Dataset sourced from [Hugging Face](https://huggingface.co/datasets/zelalt/arxiv-papers))*

- **automatic_keyword_generation.ipynb**: Uses the Together AI API to automatically generate keywords.

- **keyword_cosine_analysis.ipynb**: Computes cosine similarity between human keywords and BERT-generated keywords, as well as human keywords and AI-generated keywords.

**`automatic hypotheses generation` folder:**

- **automatic_hypotheses_generation.ipynb**: Uses the Together AI API to automatically generate hypotheses.

- **hypotheses_human_ai_comparison.ipynb**: Evaluates human-written and AI-generated hypotheses, considering various factors.

- **hypotheses_comparison_evaluation.ipynb**: Evaluates the results of human and AI performance across various categories.

**`lda` folder:**

- **scrapping.py**: Scrapes papers from arXiv.

- **store_data.py**: Stores metadata of papers in a relational database.

- **data_preprocessing.py**: Cleans and preprocesses the data.

- **model.py**: Performs topic modeling using Latent Dirichlet Allocation (LDA) on the processed paper summaries.

- **topic_interpretation.py**: Generates an interactive visualization of the topics, saving it as an HTML file.


## License

Feel free to use, modify, and distribute this code. Please make sure to credit the author. 