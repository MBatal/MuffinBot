import requests
from bs4 import BeautifulSoup
from replit import db

'''Use to add The Office quotes to replit db'''
def scrape_office():
  office_db = []
  url = "https://www.scarymommy.com/the-office-quotes"
  print(f"Scraping {url}")
  result = requests.get(url)
  page = BeautifulSoup(result.content, "html.parser")
  quotes = page.find_all('li')
  for q in quotes:
    if '—' in q.text:
      office_db.append(q.text)
  db["office"] = office_db

'''Use to add Creed quotes to replit db'''
def scrape_creed():
  cree_db = []
  url = "https://www.anquotes.com/creed-bratton-quotes/"
  print(f"Scraping {url}")
  result = requests.get(url)
  page = BeautifulSoup(result.content, "html.parser")
  quotes = page.find_all('p')
  for q in quotes:
    if '#' in q.text:
      q_str = q.text.split(" ", 1)[1]
      cree_db.append(q_str)
  db["creed"] = cree_db