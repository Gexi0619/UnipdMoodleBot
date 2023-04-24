# Si prega di compilare le informazioni di seguito

# Le informazioni personali per l'accesso a Moodle di Unipd
login_info = {
    'username': 'cognome.nome',
    'password': 'il tuo moodle password',
    'usertype': 'radio2', # Se accedi come @studenti.unipd.it, compila 'radio2'; se accedi come @unipd.it, compila 'radio1"
    'my_name': 'COGNOME NOME' # Secondo il formato
}

# Alcuni paths devono essere specificati
paths = {
    'chromedriver_path': '/usr/lib/chromium-browser/chromedriver', # Un'esempio per Raspberry Pi
    'chrome_dir': '/home/il tuo user name/.config/chromium', # Un'esempio per Raspberry Pi
    # 'chrome_dir': 'C:/Users/your user name/AppData/Local/Google/Chrome/User Data/', # Un'esempio per Windows
    'chrome_profile': 'Default' # Nome predefinito
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

# Le informazioni sulla cartella per tutte le lezioni
folders = [
    {'folder_name': 'primolezione_folder', # Assegna liberamente un nome alla cartella della lezione
     'folder_url': 'https://ssu.elearning.unipd.it/mod/folder/view.php?id=123456', # Compila l'indirizzo web della pagina della cartella della lezione utilizzando il browser
     'folder_path': '/path/primolezione/folder.txt',
     'group_name':'nome del gruppo del primolezione'}, # Il nome complecato del gruppo whatsapp per questa lezione
    {'folder_name': 'secondolezione_folder', # Crea un nuovo documento di testo per la pagina della cartella del corso e scrivi il percorso qui
     'folder_url': 'https://ssu.elearning.unipd.it/mod/folder/view.php?id=789012', # Compila le informazioni seguenti seguendo il formato sopra indicato
     'folder_path': '/path/secondolezione/folder.txt',
     'group_name':'nome del gruppo del secondolezione'}
]

# Le informazioni sul foro per tutte le lezioni
forums = [
    {'forum_name': 'primolezione_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=123456',
     'forum_path': '/path/primolezione/forum.txt',
     'group_name': 'nome del gruppo del primolezione'},
    {'forum_name': 'secondolezione_forum',
     'forum_url': 'https://ssu.elearning.unipd.it/mod/forum/view.php?id=789012',
     'forum_path': '/path/primolezione/forum.txt',
     'group_name': 'nome del gruppo del secondolezione'}
]