from discord.ext import commands

class Wide:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wide(self, ctx, *, msg=""):
        """
        I don't know... It makes the text wide.

        Usage:
        [p]wide <message id>
            ＭＥＳＳＡＧＥ ＣＯＮＴＥＮＴＳ
        [p]wide <a string that you wish to be wide>
            <ＮＯＷ ＹＯＵＲ ＳＴＲＩＮＧ ＩＳ ＷＩＤＥ>
        [p]wide
            Makes last message in channel wide
        """

        if msg:
            if msg.isdigit():
                async for message in ctx.channel.history(limit=100):
                    if str(message.id) == msg:
                        msg = message.content
                        break
        else:
            switch = False
            async for message in ctx.channel.history(limit=2):
                if switch:
                    msg = message.content
                else:
                    switch = True

        result = ""

        substitution_dict = {
            "a": "Ａ",
            "b": "Ｂ",
            "c": "Ｃ",
            "d": "Ｄ",
            "e": "Ｅ",
            "f": "Ｆ",
            "g": "Ｇ",
            "h": "Ｈ",
            "i": "Ｉ",
            "j": "Ｊ",
            "k": "Ｋ",
            "l": "Ｌ",
            "m": "Ｍ",
            "n": "Ｎ",
            "o": "Ｏ",
            "p": "Ｐ",
            "q": "Ｑ",
            "r": "Ｒ",
            "s": "Ｓ",
            "t": "Ｔ",
            "u": "Ｕ",
            "v": "Ｖ",
            "w": "Ｗ",
            "x": "Ｘ",
            "y": "Ｙ",
            "z": "Ｚ",
            "1": "１",
            "2": "２",
            "3": "３",
            "4": "４",
            "5": "５",
            "6": "６",
            "7": "７",
            "8": "８",
            "9": "９",
            "0": "０",
            "!": "！",
            "?": "？",
            " ": "　"
            }

        result = msg.lower().translate(str.maketrans(substitution_dict))

        await ctx.message.delete()
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Wide(bot))


#Lyric you halp me so much
