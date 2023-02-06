import requests
from bs4 import BeautifulSoup
import interactions
from interactions import Embed


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