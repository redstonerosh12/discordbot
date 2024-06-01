import log
import info
import discord

def process_payload(payload, client, guild):
    log.i("@on_raw_reaction_add")
    message_id = payload.message_id
    log.i("@on_raw_reaction_add/message_id", message_id)
    if message_id == info.role_react_messageID:
        log.i("@on_raw_reaction_add/if_message_id")
        # guild_id = payload.guild_id
        # guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        role = None
        log.i("@on_raw_reaction_add/if_message_id/role=None", role)
        log.i("@on_raw_reaction_add/if_message_id/payload.emoji.name", payload.emoji.name)
        if payload.emoji.name == "🟡":
            role = discord.utils.get(guild.roles, name=info.rol25) 
        elif payload.emoji.name == "🟢":
            role = discord.utils.get(guild.roles, name=info.rol24)
        elif payload.emoji.name == "🔴":
            role = discord.utils.get(guild.roles, name=info.rol23)
        elif payload.emoji.name == "🟣":
            role = discord.utils.get(guild.roles, name=info.rol22)
        elif payload.emoji.name == "🔵":
            role = discord.utils.get(guild.roles, name=info.rol21)


        log.d("@on_raw_reaction_add/if_message_id/role!=None", role)

        return role
        

def hasAClassRole(member, guild):
    uniquerolels = [
        discord.utils.get(guild.roles, name=info.rol25),
        discord.utils.get(guild.roles, name=info.rol24),
        discord.utils.get(guild.roles, name=info.rol23),
        discord.utils.get(guild.roles, name=info.rol22),
        discord.utils.get(guild.roles, name=info.rol21),
    ]

    for role in uniquerolels:
        if role in member.roles:
            return True
    return False