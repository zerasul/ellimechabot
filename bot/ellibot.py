import discord
from discord.ext import commands,tasks
from events import EventService
from datetime import datetime
from discord.ext.tasks import loop
from os import environ
import time

bot = commands.Bot(command_prefix='$elli',help_command=None)
eventService = EventService()
global channel_reminder
channel_reminder=None


@bot.event
async def on_ready():
    print('connect as {0.user}'.format(bot))
    
@bot.command(name='list')
async def listEvents(ctx):
    events=eventService.getTodayEvents()
    message='Shurmano; estos son los eventos de hoy:\n'
    message= message+_generatemessage(events)
    await ctx.send(message)

def _generatemessage(events):
    strevent=''
    for event in events:
        strevent=strevent+'* '
        strevent=strevent+str(event)+'\n'
    return strevent

@bot.command()
async def add(ctx, date, title):
    if not _check_roles(ctx):
        await ctx.send('Saecio; solo los administradores y los usuarios con rol "Pomponera" pueden usar este comando')
        pass

    eventdate = datetime.strptime(date,'%d-%m-%Y %H:%M')
    eventService.add_event(eventdate,title,ctx.author.name)
    await ctx.send('Añadiendo evento con fecha {0} y titulo "{1}"'.format(date, title))

@bot.command(name="autoreminder")
async def set_reminder(ctx):
    if not _check_roles(ctx):
       await ctx.send('Saecio; solo los administradores y los usuarios con rol "Pomponera" pueden usar este comando')
       pass
    channel_reminder=ctx.message.channel
    await ctx.send("Premoh; Estableciendo canal de eventos a #{}".format(channel_reminder.name))

def _check_roles(ctx):
    return ctx.author.top_role.permissions.administrator or len(list(filter(lambda r: r.name=='Pomponera',ctx.author.roles)))>0

@loop(hours=24)
async def reminder():
    print("Init Reminder")
    message="@everyone; estos son los eventos de hoy:\n"
    eventserv=EventService()
    events=eventserv.getTodayEvents()
    message+=_generatemessage(events)
    channels = bot.get_all_channels()
    if channel_reminder is None:
        for channel in channels:
            if channel.name=='general':
                await channel.send(message)
    else:
        await channel_reminder.send(message)
    

@bot.command(name="help")
async def help(ctx):
    message="Comandos de EllimechaBot:\n\n"
    message+="* Añadir un evento (solo administradores y Rol 'Pomponera': \n"
    message+="``` $elliadd '01-04-2021 22:00' 'La culpa es de Laikhas'```\n"
    message+="* Ver eventos del día:\n"
    message+="```$ellilist```\n"
    message+="* Ayuda: \n"
    message+="```$ellihelp```\n"
    message+="Canal de Recordatorios (solo administradores y Rol 'Pomponera'): \n"
    message+="```$elliautoreminder```"
    await ctx.send(message)

reminder.start()
bot.run(environ['DISCORD_TOKEN'])