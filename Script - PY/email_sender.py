import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Configuración de correo electrónico
SMTP_SERVER = 'smtp.gmail.com'  # Cambia esto si usas un servidor SMTP diferente
SMTP_PORT = 587  # Cambia esto si usas un puerto diferente
EMAIL_FROM = ''
EMAIL_TO = ''
EMAIL_SUBJECT = 'Error en la página web'

# Credenciales del correo electrónico
EMAIL_USERNAME = '' #USuario de correo
EMAIL_PASSWORD = '' #Key

# URL de la página web a verificar
URL = 'https://proofof-concept.azurewebsites.net/'

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def print_with_timestamp(message):
    now = get_timestamp()
    print(f'{now} - {message}')

def send_email():
    timestamp = get_timestamp()
    email_body = f'Hola\nPara informar que la plataforma {URL} no está DISPONIBLE.\nFecha y hora del error del servidor: {timestamp}'
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = EMAIL_SUBJECT
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print_with_timestamp('Correo enviado exitosamente.')
    except Exception as e:
        print_with_timestamp(f'Error al enviar el correo: {e}')

def check_website():
    try:
        response = requests.get(URL)
        if response.status_code != 200:
            print_with_timestamp(f'Status code: {response.status_code}. Enviando correo...')
            send_email()
        else:
            print_with_timestamp('La página web está funcionando correctamente.')
    except requests.exceptions.RequestException as e:
        print_with_timestamp(f'Error al hacer la solicitud: {e}. Enviando correo...')
        send_email()

if __name__ == '__main__':
    check_website()
