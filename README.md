# Telegram File Downloader Bot
This is a Telegram bot that allows you to download files sent in a Telegram group to a specified folder on your computer. It uses the Telethon library for Python and the Telegram API.

## Getting Started
### Prerequisites
- Python 3
- Telethon library (can be installed with pip)
- Telegram API ID and API Hash (can be obtained from https://core.telegram.org/api/obtaining_api_id)

### Installing
- Clone this repository
- Install the required libraries by running pip install -r requirements.txt
- Fill in your Telegram API ID and API Hash in the api_id and api_hash variables in the code
- Fill in your chat id of your group on the download variable in the code

### Usage
- Send the path of the folder where you want to download the files to the group
- Send a file to the group and it will automatically be downloaded to the specified folder on your system.

Here you have an example:

![image](https://user-images.githubusercontent.com/100825478/174212854-8bb3ef0a-3fe6-4e51-acae-d5e9284af8d8.png)

You can ask the bot if it's on, using the "alive?" command:

![image](https://user-images.githubusercontent.com/100825478/174213191-814d65dd-04d6-46ff-8873-a0be67d036e2.png)
