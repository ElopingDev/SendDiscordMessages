import requests


def get_other_user_id(auth_token, dm_channel_id, your_user_id):
    """
    Retrieves the user ID of the OTHER participant in a DM channel.

    :param auth_token: The authentication token for your account.
    :param dm_channel_id: The ID of the DM channel.
    :param your_user_id: Your own user ID.
    :return: The user ID of the other participant in the DM channel.
    Description Auto-Generated.
    """
    url = f"https://discord.com/api/v9/channels/{dm_channel_id}"

    headers = {
        "Authorization": f"{auth_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        channel_data = response.json()
        user_ids = channel_data.get('recipients', [])

        # compare ur id with recipients id to make sure it doesn't pick out your id
        for user in user_ids:
            if user['id'] != your_user_id:
                return user['id']

        return "Unable to find the other user ID."
    else:
        error_message = response.json().get('message', 'No error message provided')
        error_code = response.json().get('code', 'No error code provided')
        return f"Failed to retrieve channel details: {response.status_code}\nError code: {error_code}\nError message: {error_message}"



