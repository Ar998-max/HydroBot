from argparse import OPTIONAL
import discord 
from discord import app_commands
from typing import Literal, Optional
import asyncio
from pyparsing import Opt
from waterfacts import facts
import random
from hydronews import articles
from hydrowaterimg import data
import matplotlib.pyplot as plt


MY_GUILD = discord.Object(id=965953712147275816)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, application_id: int):
        super().__init__(intents=intents, application_id=application_id)


        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
  


intents = discord.Intents.all()

client = MyClient(intents=intents, application_id=989919619479400588) # replace with your bot's ID

@client.event
async def on_ready():
    print(f"Logged in as {client.user}\nUser id: {client.user.id}")



@client.tree.command(name="what-to-do", description='Tells you to do something fun')
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message('Drink water', ephemeral=True)

@client.tree.command(name='set-a-hydro-timer', description='A one time timer that reminds you to drink water after some preffered amount of time.')

async def slash(interaction: discord.Interaction, timeduration:float, timeunit:Literal['Hours', 'Minutes', 'Seconds']) -> None:
    await interaction.response.defer()
    await asyncio.sleep(5)
    time=str(timeduration)
    input= 'Drink water'+' After '+str(timeduration)+' '+timeunit
    await interaction.followup.send('Hydro reminder set. You will get a reminder after '+time+' '+timeunit)
    if timeunit == 'Seconds':
        converted_input = timeduration
        await asyncio.sleep(converted_input)
        embed = discord.Embed(title=f"> __** {timeduration} seconds passed, time to get hydrated**__",color=discord.Color.blue())
        await interaction.followup.send(interaction.user.mention,embed=embed)
    elif timeunit == 'Minutes':
        converted_input = timeduration * 60
        await asyncio.sleep(converted_input)
        embed = discord.Embed(title=f"> __**{timeduration} minutes passed, time to get hydrated**__",color=discord.Color.blue())
        await interaction.followup.send(interaction.user.mention,embed=embed)
    else:
        converted_input = timeduration * 3600
        await asyncio.sleep(converted_input)
        embed = discord.Embed(title=f"> __**{timeduration} hours passed, time to get hydrated**__",color=discord.Color.blue())
        await interaction.followup.send(interaction.user.mention,embed=embed)
    

@client.tree.command(name='hydro-fact', description='Get a random fact related to water.')

async def slash(interaction: discord.Interaction):
    await interaction.response.defer()
    await asyncio.sleep(5)
    rand_fact = random.choice(facts)
    embed = discord.Embed(title=f"> __** {rand_fact}**__",color=discord.Color.blue())
    await interaction.followup.send(embed=embed)


@client.tree.command(name='hydro-news', description='Get a random news article related to water.')

async def slash(interaction: discord.Interaction):
    await interaction.response.defer()
    await asyncio.sleep(5)
    news = random.choice(articles)
    news_src = news['source']['name']
    news_auth = news['author']
    news_title = news['title']
    news_url = news['url']
    news_img = news['urlToImage']

    if len(news_title) > 256:
        news_auth = news_auth.rstrip(str[-10])
        news_auth = news_auth + '....'
    
    embed = discord.Embed(title=f">>> __**{news_title}\n\n  **__",color=discord.Color.blue(),  description=f"__** \n\n {news_url} \n\n{news_src}          {news_auth}**__")
    #print(f">>> __**{news_title}\n\n {news_url} \n\n{news_src}          {news_auth} **__", description=f">>>__** {news_img} \n\n {news_url} \n\n{news_src}          {news_auth}**__", Color=discord.Color.blue())
    await interaction.followup.send(embed=embed.set_image(url=news_img) )

@client.tree.command(name='antartica-map', description='Gives a map of Antartica.')

async def slash(interaction: discord.Interaction):
    await interaction.response.defer()
    await asyncio.sleep(1)
    img = 'antartica.jpg'
    with open('antartica.jpg', "rb") as fh:
        f = discord.File(fh, filename='antartica.jpg')
        #embed = discord.Embed(title=f"> __** {}**__",color=discord.Color.blue())
        await interaction.followup.send(file=f)




@client.tree.command(name='water-image', description='Gives you a random images of water')

async def slash(interaction: discord.Interaction):
    await interaction.response.defer()
    await asyncio.sleep(1)
    
    img_list = data
    img = random.choice(img_list)
    img_url = img['urls']['regular']
    embed = discord.Embed(color=discord.Color.blue())
    #print(f">>> __**{news_title}\n\n {news_url} \n\n{news_src}          {news_auth} **__", description=f">>>__** {news_img} \n\n {news_url} \n\n{news_src}          {news_auth}**__", Color=discord.Color.blue())
    await interaction.followup.send(embed=embed.set_image(url=img_url) )


@client.tree.command(name='hydro-plotter', description='Plot the data of your water intake(max 5 inputs of hours and intakes each)')

async def slash(interaction: discord.Interaction, hour1:float, litres_of_water_consumed1:float, hour2:float, litres_of_water_consumed2:float, hour3:float, litres_of_water_consumed3:float, hour4:float, litres_of_water_consumed4:float, hour5:float, litres_of_water_consumed5:float):
    await interaction.response.defer()
    await asyncio.sleep(1)
    
    hours = [hour1, hour2, hour3, hour4, hour5]
    water_intake = [litres_of_water_consumed1, litres_of_water_consumed2, litres_of_water_consumed3, litres_of_water_consumed4, litres_of_water_consumed5]
    path = 'plot.jpg'
    plt.plot(hours, water_intake)
    plt.title('Your water intake')
    plt.xlabel('hours')
    plt.ylabel('litres of water consumed')
    plt.savefig(path)

    with open('plot.jpg', "rb") as pt:
        f = discord.File(pt, filename='plot.jpg')
        
        
        #embed = discord.Embed(color=discord.Color.blue())
    
        await interaction.followup.send(file=f)


client.run("OTg5OTE5NjE5NDc5NDAwNTg4.GPjFyK.friCruKENYW91hsqqhCbFgTdk26jkpmy8dCUjw")
