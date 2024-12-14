# Scientific Discovery: Evaluating Feasibility of Using AI in Writing

This project is submitted for the course **INFO 555 - Applied NLP**. It focuses on the topic of **Scientific Discovery**. Please refer to this file for understanding the GitHub project structure.

**Author**: Rony Macwan  
**Term**: Fall 2024  
**Subject**: INFO 555 Applied NLP  
**Project Title**: Scientific Discovery: Evaluating Feasibility of Using AI in Writing

## GitHub Project Structure

- **`Code` folder**: Contains all necessary scripts to reproduce the results.  
  - Scripts with `.ipynb` extension can be imported into **Google Colab** for modification or execution.  
  - Scripts with `.py` extension can be downloaded on any machine with Python installed and executed directly.

- **`WriteUp` folder**: Contains the PDF version of the project paper for reference and documentation.

- **`Dataset` folder**: Contains the dataset used in the project.

## Code

This folder contains the following scripts:

- **fetch_papers.py**: Script for fetching papers from Hugging Face and storing them locally.  
  *(Dataset sourced from [Hugging Face](https://huggingface.co/datasets/zelalt/arxiv-papers))*

- **keyword_cosine_analysis.ipynb**: Script for computing cosine similarity between human keywords and BERT-generated keywords, as well as human keywords and AI-generated keywords.

- **automatic_hypotheses_generation.ipynb**: Script for using the Together AI API to automatically generate hypotheses.

- **hypotheses_human_ai_comparison.ipynb**: Script for evaluating human-written and AI-generated hypotheses, considering various factors.

- **hypotheses_comparison_evaluation.ipynb**: Script for evaluating the results of human and AI performance across various categories.

## License

Feel free to use, modify, and distribute this code. Please make sure to credit the author. 