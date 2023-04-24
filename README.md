# Unipd Moodle Bot

When the professor uploads files in the folder of the Moodle course page, or when the professor sends a notification in the forum of the Moodle course page, the bot will send a notification message to the corresponding WhatsApp course group or individual.

## Prerequisites

### VPS Server or Raspberry Pi or old computer

For continuous running of the program, it is recommended to run it on a VPS or Raspberry Pi or a old computer that can be accessed at all times.

To log in to WhatsApp Web, users need to scan a QR code. Therefore, a VPS with VNC functionality is required to facilitate this process.

### Separate WhatsApp account

To ensure that the WhatsApp account associated with your bot stays logged in to WhatsApp Web for an extended period, it is recommended to create a separate WhatsApp account exclusively for the bot to send notifications. This is because the bot needs to maintain the login status continuously, and it may be inconvenient to use the same WhatsApp account for both the bot and your personal use.

## Setup

### Dependencies

Before using this project, please ensure that you have installed the following dependencies:

- Python 3.x
- Selenium
- Chrome

### Configure chromedriver

#### Windows

Open the URL '[chrome://settings/help](chrome://settings/help)' in your Chrome browser to check your Chrome version number. 

Visit the website 'https://chromedriver.storage.googleapis.com/index.html' to download the appropriate driver that matches your Chrome version. 

Note the local path where the downloaded driver is saved.

#### Linux

Using the following command to install chromedriver:

```
sudo apt-get install chromium-chromedriver
```

Default installation path for chromedriver on Linux should be at '/usr/lib/chromium-browser/chromedriver'

### Login to WhatsApp

Manually open the [WhatsApp Web](https://web.whatsapp.com/) and use your prepared WhatsApp account to scan the QR code for login verification. Ensure that your WhatsApp account has been added to the group you are connecting to.

### Fill in all the information in the settings.py file


## Usage

Use the following command to run Unipd Moodle Bot:

```
python main.py
```

### Crontab

To run the bot continuously on a server, you can use crontab. 

Use the following command to open the crontab editor:

```
crontab -e
```

Add the following command to it:

```
DISPLAY=0.0
XAUTHORITY=/home/your user name/.Xauthority
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
0,30 6-20 * * * export DISPLAY=:0 && export XAUTHORITY=/home/your user name/.Xauthority && /usr/bin/python /path to UnipdMoodleBot/main.py >> /path to UnipdMoodleBot/error.log 2>&1
```

By setting up a crontab, your Unipd Moodle Bot will run every half hour between 6:00 AM and 9:00 PM. The visual output of the run will be displayed directly on VNC, while any error code generated will be logged to the 'error.log' file located in the project directory.

## Todo

### Information types of Moodle

- [x] folder
- [x] forum
- [ ] orario degli esami
- [ ] ...

### Connected platform

- [x] WhatsApp
- [x] Email
- [ ] Telegram
- [ ] Discord

### Others

- [ ] argparse
