import discord
import random
from discord.ext import commands
from cogs.utils.checks import *

class autoquote:

	def __init__(self, bot):
			self.bot = bot
			config = load_config()
			self.cmd_prefix = config["cmd_prefix"]
	
	async def on_message(self, message):
		if message.content == "^" and message.author == self.bot.user:
			await self.bot.delete_message(message)
			channel = message.channel
			search = self.bot.all_log[message.channel.id + " " + message.server.id][-2]
			result = search[0]
			await self.bot.send_message(message.channel, "{}quote {}".format(self.cmd_prefix[0], result.id))

			
			
	@commands.command(pass_context=True)
	async def mock(self, ctx, *, msg=""):
		"""Use >mock to randomized capitalization on a message or string.
		More random comming soon™
		Usage:
		>mock a string
			A sTRiNg
		>mock
			laSt SeNT MeSsaGE
		>mock (message id)
			THaT mEsSAgE
		"""
		result = ""
		if msg:
			if msg.isdigit():
				async for message in self.bot.logs_from(ctx.message.channel, 100):
					if message.id == msg:
						msg = message.content
						break
		else:
			switch = False
			async for message in self.bot.logs_from(ctx.message.channel, 2):
				if switch:
					msg = message.content
				else:
					switch = True
		for char in msg:
			value = random.choice([True, False])
			if value == True:
				result += char.upper()
			if value == False:
				result += char.lower()
		await self.bot.delete_message(ctx.message)
		await self.bot.send_message(ctx.message.channel, result)
		
def setup(bot):
    bot.add_cog(autoquote(bot))
