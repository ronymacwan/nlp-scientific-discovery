import requests
from bs4 import BeautifulSoup

def fetch_arxiv_data(search_query, max_results=100):
    papers = []
    start = 0
    
    while True:
        url = f"http://export.arxiv.org/api/query?search_query={search_query}&start={start}&max_results={max_results}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml-xml')
            entries = soup.find_all('entry')

            if not entries:
                break  

            for entry in entries:
                title = entry.find('title').text
                authors = [author.find('name').text for author in entry.find_all('author')]
                published = entry.find('published').text
                summary = entry.find('summary').text
                link = entry.find('id').text

                # append the paper information to the list
                papers.append({
                    'title': title,
                    'authors': authors,
                    'published': published,
                    'summary': summary,
                    'link': link
                })
            
            start += max_results  
        else:
            print(f"Failed to fetch data: {response.status_code}")
            break
    
    return papers