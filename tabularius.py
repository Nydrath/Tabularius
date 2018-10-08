import json
import discord

with open("client_data.json", "r") as f:
    clientdata = json.load(f)

myself = discord.Client()

@myself.event
async def on_message(message):
    if myself.user.mention in message.content and not message.author.bot and not message.channel.is_private:
        offeringreads = [role for role in message.server.roles if role.id == "297842699480858625"][0]
        if "start" in message.content.lower():
            if not offeringreads in message.author.roles:
                await myself.add_roles(message.author, offeringreads)
                await myself.send_message(message.channel, message.author.mention+" is now offering readings.")
        elif "stop" in message.content.lower():
            if offeringreads in message.author.roles:
                await myself.remove_roles(message.author, offeringreads)
                await myself.send_message(message.channel, message.author.mention+" is no longer offering readings.")

@myself.event
async def on_member_join(member):
    channels = member.server.channels
    botlog = [channel for channel in channels if channel.id == "311888667947827200"][0]
    await myself.send_message(botlog, member.mention+" has joined the server.")

@myself.event
async def on_member_remove(member):
    channels = member.server.channels
    botlog = [channel for channel in channels if channel.id == "311888667947827200"][0]
    await myself.send_message(botlog, member.mention + " has left the server.")

@myself.event
async def on_message_delete(message):
    channels = message.server.channels
    botlog = [channel for channel in channels if channel.id == "311888667947827200"][0]
    await myself.send_message(botlog, message.author.mention + " has deleted a message from "+message.channel.name+": " + message.content)

myself.run(clientdata["token"])
