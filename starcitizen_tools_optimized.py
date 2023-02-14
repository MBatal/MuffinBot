import requests
from bs4 import BeautifulSoup
import interactions
from interactions import Embed
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def status_rsi():
    url = "https://status.robertsspaceindustries.com/"
    result = requests.get(url)
    page = BeautifulSoup(result.content, "html.parser")

    # Extract global status
    div = page.find('div', class_="global-status flex justify-center operational")
    global_status = div.text.strip()

    # Extract system titles
    systems = [d.text.split("\n")[1].strip() for d in page.find_all('div', class_="system-title")]

  # Extract system statuses
    statuses = [s.text.strip() for s in page.find_all('div', class_="system-status")]
    return {"global_status": global_status, "systems": systems, "statuses": statuses}


def star_embed():
    # Extract the statuses of the servers
    status = status_rsi()
    platform_status = status["statuses"][0]
    persistent_universe_status = status["statuses"][1]
    electronic_access_status = status["statuses"][2]

    # Extract the latest incidents
    url = 'https://status.robertsspaceindustries.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    latest_incident_date = soup.find('h3', {'class': 'timeline-incident-title'}).text
    latest_incident_description = soup.find('div', {'class': 'markdown'}).text

    # Create the embed
    embed = interactions.Embed(title="RSI Server Status", color=0x00ff00)
    embed.add_field(name="Platform", value=platform_status, inline=True)
    embed.add_field(name="Persistent Universe", value=persistent_universe_status, inline=True)
    embed.add_field(name="Electronic Access", value=electronic_access_status, inline=True)
    embed.add_field(name="Latest Incident", value=f'{latest_incident_date}: {latest_incident_description}', inline=False)
    return embed



def get_announcement_preview(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
  
    title = str(soup.title)[7:-8]
    preview = soup.find_all('meta')[1]["content"]
    embed = Embed(title=title, color=0x3e2c7f)
    embed.description = preview
    embed.add_field(name="See full post", value=f"[{title}]({url})", inline=False)
    embed.set_footer(text="Most recent post in Spectrum Announcements")
    return embed

'''Selenium is used here, need to add these pkgs to replit.nix (hidden file):
  { pkgs }: {
  deps = [
    pkgs.chromium
    pkgs.chromedriver
  ];
'''
def get_announcement(url):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.find('h1', attrs={'class':'forum-thread-subject'}).text
    if title.endswith('pinned'):
        title = title[:-6]
    post_content = soup.find('div', attrs={'class':'content-block text'}).text
    author = soup.find('span', attrs={'class':'nickname'}).text
    date = soup.find('div', attrs={'class':'forum-thread-time-created'}).text
    avatar_url = soup.find_all('div', attrs={'class':'avatar'})[5]['style'].split("\"")[1]
    # Create the embed
    embed = Embed(title=title, description=post_content, color=0x0077C9)
    embed.set_author(name=author, icon_url=avatar_url)
    embed.add_field(name='Date', value=date, inline=True)
    embed.add_field(name='Link', value=url, inline=False)
    embed.set_footer(text="Most recent post in Spectrum Announcements")
    return embed