import nextcord
from nextcord.ext import commands


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pongfinity! 😎")

    # welcome 
    @commands.command()
    async def joined(self, ctx, member: nextcord.Member):
        await ctx.send(f"howdy, {member.name}. joined in {member.joined_at}")

    # server info
    @commands.command()
    async def where(self, ctx):
        owner = str(ctx.guild.owner)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        

def setup(bot):
    bot.add_cog(basic(bot))