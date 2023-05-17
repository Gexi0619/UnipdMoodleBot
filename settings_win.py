# Le informazioni personali per l'accesso a Moodle di Unipd
login_info = {
    'username': 'gexi.sun',
    'password': 'XIgesun2304',
    'usertype': 'radio2', # Se accedi come @studenti.unipd.it, compila 'radio2'; se accedi come @unipd.it, compila 'radio1"
    'my_name': 'GEXI SOLE' # Secondo il formato
}

# 
paths = {
    'chromedriver_path': 'D:\chromedriver', #
    # 'chromedriver_path': '/usr/lib/chromium-browser/chromedriver', # Un'esempio per Raspberry Pi
    'chrome_dir': 'C:\Users\sunge\AppData\Local\Google\Chrome\User Data Copy',
    # 'chrome_dir': '/home/sgx/.config/chromium', # Un'esempio per Raspberry Pi
    'chrome_profile': 'Default'
}

# Le tue informazioni personali
me = {
    'name_whatsapp': 'il nickname', # Il nickname di whatsapp che hai impostato per l'account whatsapp con cui vuoi ricevere le notifiche come moodlebot
    'sender_email' : 'nome@mail.io', # L'indirizzo email a cui vuoi inviare i log
    'receiver_email' : 'nome@mail.io', # L'indirizzo email a cui vuoi ricevere i log (può essere la stessa di sender_email)
    'smtp_server' : 'smtp.gmail.com', # Controlla le istruzioni ufficiali per la casella di posta che stai utilizzando
    'smtp_port' : '587', # Controlla le istruzioni ufficiali per la casella di posta che stai utilizzando
    'smtp_username': 'nome@mail.io', # Controlla le istruzioni ufficiali per la casella di posta che stai utilizzando
    'smtp_password' : 'eyttrzbanzjoxqpx' # Controlla le istruzioni ufficiali per la casella di posta che stai utilizzando
}


# 所有课程的folder信息
folders = [
    {'folder_name': 'storiadellartemodernaavanzato2223_folder',
     'folder_url': 'https://ssu.elearning.unipd.it/mod/folder/view.php?id=335724',
     'folder_path': './storiadellartemodernaavanzato2223/folder.txt',
     'group_name':'IzyDhdopzOD9GXTOx2BITa'},
    {'name': 'iconografiaeiconologia2223_folder',
     'folder_url': 'https://ssu.elearning.unipd.it/mod/folder/view.php?id=336914',
     'folder_path': './iconografiaeiconologia2223/folder.txt',
     'group_name':'IzyDhdopzOD9GXTOx2BITa'},
     {'name': 'storiadellacriticadarte_folder',
     'folder_url': 'https://ssu.elearning.unipd.it/mod/folder/view.php?id=335397',
     'folder_path': './storiadellacriticadarte2223/folder.txt',
     'group_name':'IzyDhdopzOD9GXTOx2BITa'}
]

# 所有课程的forum信息
forums = [
    {'forum_name': 'storiadellartemodernaavanzato2223_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=335714',
     'forum_path': './storiadellartemodernaavanzato2223/forum.txt',
     'group_name': 'IzyDhdopzOD9GXTOx2BITa'},
    {'forum_name': 'iconografiaeiconologia2223_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=336904',
     'forum_path': './iconografiaeiconologia2223/forum.txt',
     'group_name': 'IzyDhdopzOD9GXTOx2BITa'},
     {'forum_name': 'storiadellacriticadarte2223_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=335387',
     'forum_path': './storiadellacriticadarte2223/forum.txt',
     'group_name': 'IzyDhdopzOD9GXTOx2BITa'},
     {'forum_name': 'storiadellacittaedelterritorio2223_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=332404',
     'forum_path': './storiadellacittaedelterritorio2223/forum.txt',
     'group_name': 'IzyDhdopzOD9GXTOx2BITa'},
]
