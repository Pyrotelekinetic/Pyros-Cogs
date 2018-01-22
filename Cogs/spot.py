import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class spot:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def spot(self, ctx, *, msg=""):

		"""
		testing...
		usage:
		stuff
		stuff
		"""

			#authorize via client credentials flow
		client_credentials_manager = SpotifyClientCredentials(client_id="", client_secret="")
		sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

		results = sp.search(q=msg, limit=1, offset=0, type="track", market=None)
		
		trackname = results['tracks']['items'][0]['name']
		
		trackpreview = results['tracks']['items'][0]['preview_url']
		
		if trackpreview == "null":
			prettyresult = discord.Embed(title = "Search Results", description = trackname + "Preview Unavailable")
		else:
			prettyresult = discord.Embed(title = "Search Results", description = trackname + trackpreview)
		
		await ctx.message.delete()
		await ctx.send(embed=prettyresult)
def setup(bot):
	bot.add_cog(spot(bot))
	
