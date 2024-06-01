import discord
import responses
import safeconvert
import info
import log
import roleReactFind

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response != None:
            print(f"(in response): {response}")
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = info.bot_token

     # Define intents
    intents = discord.Intents.default()
    intents.message_content = True  # Adjust according to the events you want to listen to

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"client is now ready!")

    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return #dont reply to your own message
        
        username = safeconvert.convert(message.author, str)
        user_message = safeconvert.convert(message.content, str)
        channel = safeconvert.convert(message.channel, str)

        print(f"({username} @ {channel}): {user_message}")

        if user_message[0] == "=":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

        if user_message[0] == "+":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

    @client.event
    async def on_raw_reaction_add(payload):
        guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
        member = await guild.fetch_member(payload.user_id)
        
        log.i("@bot.py/on_raw_reaction_add", member)
        role = roleReactFind.process_payload(payload, client, guild)

        if role is not None and not roleReactFind.hasAClassRole(member, guild):
            await member.add_roles(role)
            log.d("@bot.py/on_raw_reaction_add/role!=None member role added!")
            log.m(f"user '{member}' has had role '{role}' added")
        else:
            log.i("@bot.py/on_raw_reaction_add/role!=None member role add illegal as role already present or failed!")


    @client.event
    async def on_raw_reaction_remove(payload):
        guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
        member = await guild.fetch_member(payload.user_id)
        
        log.i("@bot.py/on_raw_reaction_add", member)
        role = roleReactFind.process_payload(payload, client, guild)

        if role is not None:
            await member.remove_roles(role)
            log.d("@bot.py/on_raw_reaction_add/role!=None member role removed!")
            log.m(f"user '{member}' has had role '{role}' removed")
        else:
            log.i("@bot.py/on_raw_reaction_add/role!=None member role remove failed!")


    client.run(TOKEN)

