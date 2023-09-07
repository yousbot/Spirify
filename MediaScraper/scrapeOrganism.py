import sys
import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_document_links(base_url, session):
    response = session.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [a_tag['href'] for a_tag in soup.find_all('a', href=True) if a_tag['href'].startswith('https://www.organism.earth/library/document/')]

def fetch_document_data(document_url, session):
    response = session.get(document_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        author = soup.find(class_='author-portrait-name').text.strip()
        title = soup.find('div', id='doc-header-width-limiter').find('h1').text.strip()
        date = soup.find('h3').text.strip()
        summary = soup.find(id='doc-header-summary').text.strip()
        referenced_authors_section = soup.find(id='referenced-authors')
        references = [ref.text.strip() for ref in referenced_authors_section.find_all('a')] if referenced_authors_section else None        
        audio_element = soup.find(id='audioPlayer')
        video_element = soup.find(id='videoPlayer')
        document_body = soup.find(class_='document-body').get_text()
    except AttributeError as e:
        print(f"Skipping {document_url} due to missing attributes. Error: {e}")
        return None

    media_link = {"type": "none", "url": None}
    if audio_element:
        media_link = {"type": "audio", "url": "https://www.organism.earth/library" + audio_element.find('source')['src']}
    elif video_element:
        media_link = {"type": "video", "url": "https://www.organism.earth/library" + video_element.find('source')['src']}
    
    return {
        "author": author,
        "title": title,
        "date": date,
        "summary": summary,
        "References": references,
        "media": media_link,
        "talk": document_body
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrapeOrganism.py <author_list>")
        sys.exit(1)

    author_list = sys.argv[1]
    all_documents = []
    
    with requests.Session() as session:
        with ThreadPoolExecutor() as executor:
            with open(author_list, 'r') as file:
                for base_url in file:
                    base_url = base_url.strip()
                    document_links = fetch_document_links(base_url, session)
                    document_data_futures = {executor.submit(fetch_document_data, url, session): url for url in document_links}
                    
                    for future in as_completed(document_data_futures):
                        url = document_data_futures[future]
                        try:
                            document_data = future.result()
                            if document_data:
                                all_documents.append(document_data)
                        except Exception as e:
                            print(f"Skipping {url} due to an error: {e}")


    with open('transcripts/lectures_dump.json', 'w') as json_file:
        json.dump(all_documents, json_file, indent=4)
