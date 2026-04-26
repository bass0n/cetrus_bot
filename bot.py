import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

MACRO_KEYWORDS = ["macro", "macros", "macroing", "macroed", "certus", "Certus"]
CHANNEL_MENTION = "<#1489277223755317498>"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    content = message.content.lower()
    if any(word in content for word in MACRO_KEYWORDS):
        await message.reply(f"The macro (Certus) can be found in <#1489277223755317498>.")

client.run("MTQ5Nzc0MzAwNDg2MDE1ODAwMg.GEVrmL.97uMuiZE4hXa6hJVfNq5RxuFAvWu_LH09ZaXi4")