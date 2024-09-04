from datetime import datetime

import requests


def get_infos(auth_token, user_id):
    """
    Retrieves the Discord username and discriminator of a user given their user ID.

    :param auth_token: The authentication token for the Discord bot.
    :param user_id: The user ID of the person whose username is to be retrieved.
    :return: The full username (username#discriminator) if successful, else an error message.
    Description Auto-Generated.
    """
    url = f"https://discord.com/api/v9/users/{user_id}"

    headers = {
        "Authorization": f"Bot {auth_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        username = user_data['username']
        global_name = user_data['global_name']
        target_id = user_data['id']
        avatar_hash = user_data['avatar']
        discriminator = user_data['discriminator']


        # Decode the user ID to get the creation date
        # Discord snowflake ID format: timestamp (milliseconds) + worker ID + process ID + increment
        # Timestamp is in the highest 42 bits of the ID
        # Not made by me thanks to ChatGPT for the formula
        snowflake_timestamp = (int(user_id) >> 22) + 1420070400000  # Discord epoch
        creation_date = datetime.utcfromtimestamp(snowflake_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

        return (f"Username: {username}#{discriminator}\n"
                f"Display Name: {global_name}\n"
                f"User ID: {target_id}\n"
                f"Account Creation Date: {creation_date}\n"
                f"Avatar: https://cdn.discordapp.com/avatars/{target_id}/{avatar_hash}\n")
    else:
        return f"Failed to retrieve user details: {response.status_code}\nResponse content: {response.text}"
