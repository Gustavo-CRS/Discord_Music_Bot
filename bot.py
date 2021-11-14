from discord.ext import commands

bot = commands.Bot(command_prefix='.')

bot.lava_nodes = [{
    'host': 'lava.link',
    'port': 80,
    'rest_uri': 'http://lava.link:80',
    'identifier': 'MAIN',
    'password': 'teste',
    'region': 'singapore'
}]

@bot.event
async def on_ready():
    print('Darth Music Bot está pronto para tocar músicas.')
    bot.load_extension('dismusic')
    bot.load_extension('dch')

bot.run('OTA5MjM0MTg4NTk3NzU1OTA2.YZBUUw.TZumvNqFAKzd2RUIWZJrAkAR0yY')
