import json
from unicodedata import name
from pprint import pprint
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

url="https://api.github.com/repos/devtron-labs/devtron/releases/latest"

response=requests.get(url)

output=json.loads(response.text)
release_name= output["name"]
tag_name= output["tag_name"]
body=output["body"]

dis_header = {
    'authorization': 'OTQ1ODYxNjMxMDUxNzIyNzYy.YhWUeQ.QN42ibXxgOYuRh4k_zqtF7pjlTw'
}

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/946099813873770607/mUkM4JtFleH6Xn5di3WBSzrxuFxk13WbhZ4f6l83nw4YirYSKvyvSE_jmt84dgZ_E0k1')

embed = DiscordEmbed(title=release_name, description=body, color='ffd966')

embed.set_author(name='Devtron Labs')

webhook.add_embed(embed)

response = webhook.execute()