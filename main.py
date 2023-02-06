import os
import random
import interactions
from replit import db
from keep_alive import keep_alive
from eggys import *
from starcitizen_tools_optimized import *
import openai
from interactions import Embed
from mod import *
import requests
import json

# Dunmiff/Sys

client = interactions.Client(token=os.environ['MUFFIN'])

openai.api_key = os.environ['OPENAI_API_KEY']
if "creed" not in db.keys():
    scrape_creed()
if "office" not in db.keys():
    scrape_office()


@client.event
async def on_ready():
    print('setting up')
    print('We have loggen in ')


@client.command(
    name="creed_thoughts",
    description="Retrieve a Creed Bratton quote",
    scope=int(os.environ['GUILD_ID']),
)
async def creed_thoughts(ctx: interactions.CommandContext):
    print(ctx.author)  # nickname
    await ctx.send(random.choice(db["creed"]))

@client.command(
    name="dunmiff",
    description="Retrieve a quote from The Office",
    scope=int(os.environ['GUILD_ID']),
)
async def dunmiff(ctx: interactions.CommandContext):
    await ctx.send(random.choice(db["office"]))

@client.command(
    name="test_ai",
    description="Change presence of Bot",
    scope=os.environ['GUILD_ID'],
)
@interactions.option()
async def test_ai(ctx: interactions.CommandContext, text: str):
    print(ctx.author.name)
    print(type(ctx.author))
    if ctx.author.name != "DaMuffinMann217": #ctx.author.id
        await ctx.send("Right now this feature is offline")
        return
    await ctx.send("Generating response...\n")
    response = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=450,  # around 100 words
        prompt=text,
        temperature=0.6
    )

    msg = response['choices'][0]['text']
    print(msg)
    await ctx.send(msg)

@client.command(
    name="server_status",
    description="Test the discord embed system",
    scope=os.environ['GUILD_ID'],
)
async def server_status(ctx: interactions.CommandContext):
    embed = star_embed()
    await ctx.send(embeds=embed)

@client.command(
    name="rules",
    description="Retrieve StaRP's rules",
    scope=os.environ['GUILD_ID'],
)
async def rules(ctx: interactions.CommandContext):
    await ctx.send("Generating response...\n")
    embed = get_rules()
    await ctx.send(embeds=embed)

print("HEEER")
keep_alive()
client.start()