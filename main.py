
import requests
from getInfos import get_infos
from getID import get_other_user_id


channel_id = input(f"Enter channel ID.\n")
owner_id = "xxx"
client_auth_token = "xxx"
bot_auth_token = "xxx"
url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

user_id_from_channel = get_other_user_id(client_auth_token, channel_id, owner_id)
user_result = get_infos(bot_auth_token, user_id_from_channel)

response = requests.get('https://www.google.com')
user_agent = response.request.headers['User-Agent']

finalMessage = f"{user_result}\nUser Agent : {user_agent}"

payload ={
    "content" : {finalMessage}
}

headers ={
    f"Authorization":f"{client_auth_token}"

}


rq = requests.post(url, payload, headers=headers)

print(rq)