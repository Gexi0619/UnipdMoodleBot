
from settings_win import folders, forums, login_info, paths, me

# Prepare for selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Prepare for others
import os
import difflib
import pyautogui
import time
import datetime
import sys
import io
current_dir = os.path.dirname(os.path.abspath(__file__))

# Prepare for send data to my self
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
output = io.StringIO()
sys.stdout = output

from selenium.webdriver.chrome.service import Service
s = Service(paths['chromedriver_path'])

# Creat a new chrome instance
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={paths['chrome_dir']}")
options.add_argument(f"--profile-directory={paths['chrome_profile']}")
options.add_argument('--lang=en')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
# options.add_argument('--headless') # Faster, but more unstable
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-infobars')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--start-maximized')
options.add_argument('user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
driver = webdriver.Chrome(service=s, options=options)


# Login to Moodle
driver.get('https://ssu.elearning.unipd.it/auth/shibboleth/index.php')
print('Moodle page is opening')
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_username_js")))
username = driver.find_element('name', 'j_username_js')
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "j_username_js")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "j_username_js")))
username_input.send_keys(login_info['username'])
password = driver.find_element('name', 'j_password')
password.send_keys(login_info['password'])
dominio = driver.find_element('id', login_info['usertype'])
dominio.click()
accedi = driver.find_element('id', 'login_button_js')
accedi.click()
try: # Check if login successful
    element = WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(text(),"{}")]'.format(login_info['my_name'])), login_info['my_name']))
    driver.execute_script("window.stop();")
    print('Login successful')
except Exception as e:
    print(e)

# Connect to whatsapp
driver.execute_script("window.open('https://web.whatsapp.com/')") # Open a new tab on an exist window
driver.switch_to.window(driver.window_handles[0]) 
#try:
    #me = WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(),'{me['name_whatsapp']}')]")))
    #print('connected to whatsapp web successful')
    #driver.switch_to.window(driver.window_handles[0]) 
#except:
    #print('cannnot connect to the whatsapp web')
    #driver.switch_to.window(driver.window_handles[0]) 

        
# Check all course folders
for folder in folders:

    print("-----", folder['folder_name'], "-----")

    # Enter the folder page of the course and list all files
    driver.get(folder['folder_url'])
    # driver.get_screenshot_as_file('moodlecoursepage.png') 
    files = driver.find_elements(By.CLASS_NAME, 'fp-filename')
    new_folder = [file.text for file in files]
    print("newfolder:", new_folder)

    # Get the old lists from the document
    with open(folder['folder_path'], 'r', encoding='utf-8') as f:
        old_folder = [line.strip() for line in f.readlines()]
    print("oldfolder:", old_folder)

    # Compare old and new lists
    folder_news = set(new_folder) - set(old_folder)
    print("folder update:", folder_news) 

    if folder_news:
        print('***Starting send msg to whatsapp group***')
        # Message wording
        now = datetime.datetime.now()
        time_str = now.strftime('%d %b %H:%M').replace(' 0', ' ')
        #folder_content = f"Moodlebot\nNuovo caricamento: {', '.join(folder_news)}\n{time_str}"
        #folder_content = f"Moodlebot{Keys.SHIFT}{Keys.ENTER}Nuovo caricamento:{Keys.SHIFT}{Keys.ENTER}{time_str}"
        folder_content = f"[MoodleBot] Nuovo caricamento: {', '.join(folder_news)}"

        # Send to Whatsapp group
        driver.switch_to.window(driver.window_handles[-1]) # Switch to the second tab
        print('Whatsapp page is opening')
        # driver.get_screenshot_as_file('whatsapppage.png')

        group = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(folder['group_name']))))
        print('Already find the group')
        # driver.get_screenshot_as_file('whatsappgroup.png')
        group.click()

        inputbox = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
        inputbox.send_keys(folder_content)
        inputbox.send_keys(Keys.ENTER)
        print('Already send the msg')

        # Check if the send is successful
        try:
            WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Pending']")))
        except:
            print('Failed to send the message, it may be a network problem')
        
        driver.switch_to.window(driver.window_handles[0]) # Switch back to the first tab

        # Write the full up-to-date list to the document
        files = driver.find_elements(By.CLASS_NAME, 'fp-filename')#redifined
        new_folder = [file.text for file in files]
        with open(folder['folder_path'], 'w') as f:
            for file in files:
                f.write(file.text + '\n')
        print('Write down update successful')

    else:
        print("No update")


# Check all course forums
for forum in forums:

    print("-----", forum['forum_name'], "-----")

    # Enter the forum page of the course and list all files
    driver.get(forum['forum_url'])
    dicussions = driver.find_elements(By.CLASS_NAME, "w-100.h-100.d-block")
    new_discussions = []
    for discussion in dicussions:
        new_discussion = discussion.get_attribute("title")
        new_discussions.append(new_discussion)
    print("newforum:", new_discussions)

    # Get the old lists from the document
    with open(forum['forum_path'], 'r', encoding='utf-8') as f:
        old_discussions = [line.strip() for line in f.readlines()]
    print("newforum:", old_discussions)

    # Compare old and new lists
    forum_news = set(new_discussions) - set(old_discussions)
    print("forum update:", forum_news) 

    if forum_news:
        print('***Starting send msg to whatsapp group***')
        # Message wording
        now = datetime.datetime.now()
        time_str = now.strftime('%d %b %H:%M').replace(' 0', ' ')
        #forum_content = f"Moodlebot\nNuova comunicazione: {', '.join(forum_news)}\n{time_str}"
        forum_content = f"[MoodleBot] Nuova comunicazione: {', '.join(forum_news)}"

        # Send to Whatsapp group
        driver.switch_to.window(driver.window_handles[-1]) # Switch to the second tab
        print('Whatsapp page is opening')
        # driver.get_screenshot_as_file('whatsapppage.png')

        group = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(folder['group_name']))))
        print('Already find the group')
        # driver.get_screenshot_as_file('whatsappgroup.png')
        group.click()

        inputbox = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
        inputbox.send_keys(forum_content)
        inputbox.send_keys(Keys.ENTER)
        print('Already send the msg')

        # Check if the send is successful
        try:
            WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Pending']")))
        except:
            print('Failed to send the message, it may be a network problem')

        driver.switch_to.window(driver.window_handles[0]) # Switch back to the first tab

        # Write the full up-to-date list to the document
        dicussions = driver.find_elements(By.CLASS_NAME, "w-100.h-100.d-block")#newdifined
        new_discussions = []
        for discussion in dicussions:
            new_discussion = discussion.get_attribute("title")
            new_discussions.append(new_discussion)
        with open(forum['forum_path'], 'w') as f:
            for new_discussion in new_discussions:
                f.write(new_discussion + '\n')
        print('Write down update successful')

    else:
        print("No update")
        
        
        
# Send run data to my self by email
# Get terminal output
sys.stdout = sys.__stdout__
output_str = output.getvalue()
#Write down data file
now = datetime.datetime.now()
dt_string = now.strftime("%Y%m%d%H%M")
datafile = 'data/data_' + dt_string + '.txt'
with open(datafile, 'w') as f:
    f.write(output_str)
# Write the email
msg = MIMEMultipart()
msg['Subject'] = '[MoodleBot] Data_' + dt_string
msg['From'] = me['sender_email']
msg['To'] = me['receiver_email']
with open(datafile, 'r') as f:
    body = f.read()
msg.attach(MIMEText(body))
# Send the email
try:
    with smtplib.SMTP(me['smtp_server'], me['smtp_port']) as smtp:
        smtp.starttls()
        smtp.login(me['smtp_username'], me['smtp_password'])
        smtp.sendmail(me['sender_email'], me['receiver_email'], msg.as_string())
    print('Email send successful')
except Exception as e:
    print(e)

# Message myself to report running status
driver.switch_to.window(driver.window_handles[-1]) # Switch back to the first tab
me = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(me['name_whatsapp']))))
me.click()
inputbox = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
inputbox.send_keys('Suc!')
inputbox.send_keys(Keys.ENTER)
try:
    WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Pending']")))
    print('Whatsapp msg send successful')
except:
    print('Failed to send the whatsapp msg')
time.sleep(30)

driver.quit()

