import discord
from discord import Client
from discord.ext.tasks import loop
from crypto_reader import btc_attuale, eth_attuale


TOKEN = "MTAyODAyNDQ2OTE1Mjg2MjMzOA.Gap6Wi.5d9Llm7cMFt2r0iVVsN67WHOO5oSNBxwxt7QGo"
TEST_ID = 831169527529734194
MAIN_ID = 798566791172456518

TARGET_PRICE = "prezzo_target.txt"

intents = discord.Intents.default()
intents.message_content = True
bot = Client(intents=intents)


def get_target():
    with open(TARGET_PRICE) as f:
        target = int(f.read())
        return target
def set_target(new_target):
    with open(TARGET_PRICE, "w") as f:
        f.write(new_target)


@bot.event
async def on_ready():
    channel = bot.get_channel(TEST_ID)
    await channel.send("Pronto🫡")
    send_quotation.start()
    
@loop(hours=24)
async def send_quotation():
    channel = bot.get_channel(MAIN_ID)
    text = f"Prezzo attuale di un 1 BTC: {btc_attuale}$, 1 ETH: {eth_attuale}$"
    await channel.send(text)
    if btc_attuale < get_target():
        await channel.send("E' il momento di investire💸")
    await channel.send("`$help`")

@bot.event
async def on_message(message):
    author = message.author
    testo = message.content
    channel = message.channel
    
    if author == bot.user:
        return


    print(f"AUTH: {author}")
    print(f"TXT: {testo}")
    print(f"CH: {channel}")
    print("------------")


    if testo.startswith("$btc"):
        await channel.send(f"Prezzo attuale di un 1 BTC: {btc_attuale}€")
        if btc_attuale < get_target():
            await channel.send("E' il momento di investire💸")

        return

    elif testo.startswith("$eth"):
        await channel.send(f"Prezzo attuale di un 1 ETH: {eth_attuale}€")

    elif testo.startswith("$target"):
        if len(testo.split())>1:
            new_target = testo.split()[1]
            set_target(new_target)
            await channel.send(f"Target impostato a {new_target}€")
        else:
            await channel.send(f"Target attuale: {get_target()}€")
        return

    elif testo.startswith("$help"):
        await channel.send(f"""Salve {author.name}.
Per visualizzare il prezzo di 1 BTC: `$btc`
Per visualizzare il prezzo di 1 ETH: `$eth`
Per impostare un target di prezzo: `$target <nuovo target>`
    In mancanza del parametro, sarà visualizzato il target preimpostato (`$target`).
    Target non aconcora disponibile per ETH.
        """)
        return

bot.run(TOKEN)
