# coding: utf-8

import asyncio
import discord
import discord.ext.commands

token = 'Njk4ODM4ODA1MDEyMTUyMzk0.XpO6mg.iWFycfAWkKSp_XWYC-5V9aQrQUg'
channel_id: int = 698051705715163196

bot = discord.ext.commands.Bot(command_prefix="1/")
game = discord.Game("v.0.0.1(beta)")


class MyBot(bot):
    def __init__(self):

        @bot.event()
        async def on_ready():
            print('We have logged in as {0.user}'.format(bot))
            await bot.change_presence(status=discord.Status.idle, activity=game)

        @bot.command(name="atk")
        async def atk(ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send("::atk")

        @bot.command(name="res")
        async def res(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::re')

        @bot.command(name='st')
        async def status(self, ctx):
            await ctx.channel.send('::st')
            await asyncio.sleep(3)
            await ctx.channel.send("0")

        @bot.command(name='i')
        async def item(self, ctx):
            await ctx.channel.send('::i')

        @bot.command(name='i i')
        async def itemi(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::i i')

        @bot.command(name='i e')
        async def iteme(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send(':i e')

        @bot.command(name='login')
        async def loginnn(self, ctx):
            await ctx.channel.send('::login')

        @bot.command(name='role0')
        async def role0(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::role')
            await asyncio.sleep(3)
            await channel.send('0')

        @bot.command(name='role1')
        async def role1(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::role')
            await asyncio.sleep(3)
            await channel.send(1)

        @bot.command(name='role2')
        async def role2(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::role')
            await asyncio.sleep(3)
            await channel.send('2')

        @bot.command(name='role3')
        async def role3(self, ctx):
            channel: object = bot.get_channel(channel_id)
            await channel.send('::role')
            await asyncio.sleep(3)
            await channel.send('3')

    async def process_commands(self, message):
        ctx = await self.get_context(message)
        await self.invoke(ctx)

bot.run(token)
