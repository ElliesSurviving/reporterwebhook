# WintersAPI Reporter - Reporter webhook for the WintersAPI
# Written by Sienna & Ellie, of the Winters Collective
# Written on 24/03/2024

from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from time import gmtime, strftime
import requests
import os
import psutil
import time
import datetime

# quick setup var(s), always handy ~ Sienna
webhookurl = ("webhook url here")

# fun shit totally real ios 19 rootful untethered unc0ver black edition cydia free mr beast verified suck balls piss shit god fucking damn aaa ~ Sienna

# system infooooooooooooo linux makes this easy i think ~ Ellie

# shittiest shit uve seen in ur life ~ Ellie+Sienna
#i = 1
#while i < 6 # this shit became unused after switching to a cron job:
cpu_usage = psutil.cpu_percent(interval=60)
memory_usage = psutil.virtual_memory().percent 
swap_usage = psutil.swap_memory().percent 
disk_usage = psutil.disk_usage('/').percent
now = strftime("%X", gmtime()) 

# finally sending the webhook ~ Ellie
webhook = DiscordWebhook(url=webhookurl) 
embed = DiscordEmbed(title='System Resources Report', description=(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Swap Usage: {swap_usage}%, Disk Usage: {disk_usage}%, sent at {now}"))

webhook.add_embed(embed)
response = webhook.execute()
#print("successfully sent webhook at ", now, "in #resource-reporter-bot")
#time.sleep(1800)
