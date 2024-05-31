import discord
import responses
import safeconvert
import info

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



    client.run(TOKEN)

