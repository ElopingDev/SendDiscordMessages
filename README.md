# Discord API Learning Project

## Overview

This is a simple project designed to help understand how to interact with APIs, specifically the Discord API. The script retrieves user information from a Discord channel and sends a message with the user's details and the current user agent.

## Features

- Retrieve information about a user from a Discord channel.
- Fetch the user agent from a web request.
- Send a message to a specified Discord channel containing the user's informations.

## How It Works

1. **Input Channel ID**: The script prompts for a Discord channel ID.
2. **Retrieve User ID**: Uses the `get_other_user_id` function to get the user ID of the other participant in a DM channel.
3. **Fetch User Information**: Uses the `get_infos` function to retrieve and format information about the user.
4. **Send Message**: Posts a message to the specified channel with the user's details and user agent.

## Setup

1. **Install Dependencies**: Ensure you have `requests` installed.
   ```bash
   pip install requests
   ```
2. **Update Tokens**: Replace "xxx" with your actual client_auth_token and bot_auth_token.

3. **Run the Script**: Execute the script using Python.  

## Credits

- Discord API: [Discord Developer Portal](https://discord.com/developers/docs/intro)
- User ID Calculation: Special thanks to ChatGPT for assisting with the snowflake timestamp formula.
