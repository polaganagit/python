import streamlit as st
import requests ## to get/connect URL 
from bs4 import BeautifulSoup ## to parse html
import wikipedia
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_wikipedia_url(search_term):
  try:
    logging.info(f"Searching Wikipedia for: {search_term}")
    page_title=wikipedia.page(search_term).title
    logging.info(f"Found page title: {page_title}")
    url=f"https://en.wikipedia.org/wiki/{page_title.replace(' ','_')}"
    logging.info(f"Generated URL: {url}")
    return url
  except wikipedia.exceptions.PageError as e:
    return None


def get_wikipedia_content(url, max_words=1000):
  try:
    logging.info(f"Attempting to scrape url: {url}")
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response=requests.get(url,headers=headers)
    response.raise_for_status()
    soup=BeautifulSoup(response.text,'html.parser')
    paragraphs=soup.find_all('p')
    logging.info(f"Found {len(paragraphs)} paragraphs on the page.")
    
    collected_paragraphs = []
    current_word_count = 0
    
    for p in paragraphs:
        p_text = p.get_text() + '\n'
        p_words = p_text.split()
        p_word_count = len(p_words)
        
        if current_word_count + p_word_count >= max_words:
            # Take only the remaining words needed to reach max_words
            words_needed = max_words - current_word_count
            truncated_p_text = ' '.join(p_words[:words_needed])
            collected_paragraphs.append(truncated_p_text)
            logging.info(f"Reached max_words threshold of {max_words}. Stopped reading further paragraphs.")
            break
        else:
            collected_paragraphs.append(p_text)
            current_word_count += p_word_count
            
    content = ' '.join(collected_paragraphs)
    return content
  except requests.exceptions.RequestException as e:
      logging.error(f"Error while scraping URL: {e}")
      return None
  except Exception as e:
      logging.error(f"An unexpected error occurred: {e}")
      return None
  def main():
    st.set_page_config(page_title="Wikipedia Scraper", layout="centered")
    st.title("Wikipedia Content Scraper")
    search_term = st.text_input("Enter a search term for Wikipedia:")
    if search_term:
      with st.spinner("Scraping Wikipedia..."):
        url=get_wikipedia_url(search_term)
        if url:
          content=get_wikipedia_content(url)
        if content and not content.startswith("Error:"):
          st.subheader("Scraped Content:")
          st.text_area("Extracted content: ",value=content, height=500)
        elif content.startswith("Error:"):
          st.error(content)
        else:
          st.warning("No content found on the Wikipedia page.")
          
  if __name__=="__main__":
    main()
    

  
