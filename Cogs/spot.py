import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class spot:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def spot(self, ctx, *, msg = ""):

		"""
		Under Heavy Development
		Search for a track on Spotify and return name and url to 30 second preview
		usage:
		[p]spot <search term>
		"""

			#authorize via client credentials flow
		client_credentials_manager = SpotifyClientCredentials(client_id = "", client_secret = "")
		sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

		await ctx.message.delete()
		if msg == "":
			await ctx.send("You must enter a phrase to search for!")
		else:
				#hit api with search query
			results = sp.search(q = msg, limit = 1, offset = 0, type = "track", market = None)
				#check if no tracks were found
			if results["tracks"]["total"] == 0:
				await ctx.send(embed = discord.Embed(title = "No Results!", description = 'No tracks matching "{}" were found'.format(msg)))
				#grab the data data we want from api response
			else:
				trackname = results["tracks"]["items"][0]["name"]
				trackpreview = results["tracks"]["items"][0]["preview_url"]
				if trackpreview == None:
					trackpreview = ""
				albumcover = results["tracks"]["items"][0]["album"]["images"][2]["url"]
				trackdata = str(trackname) + str(trackpreview)
					#generate readable response embed
				prettyresult = discord.Embed(title = "Search: " + str(msg), description = str(trackname) + str(trackpreview), thumbnail = albumcover)
				await ctx.send(embed = prettyresult)
			#await ctx.send(results)
			#['tracks']['items']['albulm']['images'][3]['url']
def setup(bot):
	bot.add_cog(spot(bot))
