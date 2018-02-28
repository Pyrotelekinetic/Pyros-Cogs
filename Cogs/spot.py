import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class spot:
	"""Still under development. May not work as expected."""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def search(self, ctx, *, msg = ""):

		"""
		Basic Spotify search
		usage:
		[p]search <search term> | <search type>
		Better docs comming soon™
		"""

			#authorize spotipy api requests via client credentials flow
		client_credentials_manager = SpotifyClientCredentials(client_id = clientid, client_secret = clientsecret)
		sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

		await ctx.message.delete()

			#check if search type is defined, set query and type
		if "|" in msg:
			query, qtype = msg.split("|", 1)
			query = query.strip()
			qtype = qtype.strip()
			qtype = qtype.lower()
			if qtype in ["artist", "artists", "album", "artists", "track", "tracks", "playlist", "playlists"]:
				if qtype[-1] == "s":
					qtype = qtype[:-1]
			else:
				qtype = "track"

			#if type not defined, set to default
		else:
			query = msg.strip()
			qtype = "track"

			#check if there is actually something to search for
		if query == "":
			await ctx.send("You must enter a phrase to search for!")

				#hit api with search query
		else:
			response = sp.search(q = query, limit = 10, offset = 0, type = qtype, market = None)

				#check if no results were found
			if response[qtype + "s"]["total"] == 0:
				await ctx.send(embed = discord.Embed(title = "No Results!", description = "No {} matching \"{}\" were found".format(qtype + "s", query)))

				#grab relevant data from api response
			else:
				trackname = response[qtype + "s"]["items"][0]["name"]
				trackpreview = response["tracks"]["items"][0]["preview_url"]
				albumcover = response["tracks"]["items"][0]["album"]["images"][2]["url"]
				if trackpreview == None:
					trackpreview = "Preview unavailable"

					#generate readable response embed
				prettyresponse = discord.Embed(title = "Search: " + query, description = trackname + "\n" + trackpreview).set_thumbnail(url = albumcover)

					#send response embed
				await ctx.send(embed = prettyresponse)

def setup(bot):
	bot.add_cog(spot(bot))
