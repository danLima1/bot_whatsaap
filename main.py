import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule
from datetime import datetime, timedelta
import pytz
import random
import os

# Configuração do WebDriver (certifique-se de ter o chromedriver instalado e no PATH)
driver = webdriver.Chrome()


def login_whatsapp():
    driver.get("https://web.whatsapp.com")
    print("Por favor, escaneie o QR Code para logar no WhatsApp Web.")
    while True:
        try:
            # Espera até que o elemento de busca esteja presente, indicando login bem-sucedido
            driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            break
        except:
            time.sleep(5)
    print("Login realizado com sucesso.")


def find_group(group_name):
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        print(f"Grupo '{group_name}' encontrado.")
    except Exception as e:
        print(f"Erro ao encontrar o grupo '{group_name}': {e}")


def send_message(message):
    try:
        pyperclip.copy(message)
        message_box = driver.find_element(By.XPATH,
                                          '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
        message_box.click()
        message_box.send_keys(Keys.CONTROL, "v")  # Cola o texto da área de transferência
        message_box.send_keys(Keys.ENTER)
        print("Mensagem enviada com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")


def send_photo(photo_path):
    try:
        # Clica no ícone de anexo
        attach_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
        attach_button.click()

        # Seleciona a opção de foto/vídeo
        photo_video_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
        photo_video_button.send_keys(photo_path)

        time.sleep(3)  # Tempo para o upload da foto

        # Envia a foto
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send-light"]')
        send_button.click()
        print("Foto enviada com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar a foto: {e}")


def send_promotional_message():
    group_name = "test"
    message = """➡ Você vai se CADASTRAR nessa plataforma de graça e vai
fazer o DEPÓSITO de qualquer valor acima de R$32,00.

➡ Vai ME MANDAR NO PRIVADO o print do COMPROVANTE.

E eu vou escolher aleatoriamente a pessoa que vai levar o
iPhone 😍

👉🏻 Link para se CADASTRAR na plataforma e fazer o depósito:
[CADASTRE-SE AQUI](https://go.aff.donald.bet/spnpc6hv)

👉🏻 Para mandar o COMPROVANTE é nesse número no privado

É SOMENTE ISSO PARA PARTICIPAR"""

    photo_path = "C:/Users/dn/Pictures/sorteio.jpeg"  # Caminho para a foto a ser enviada

    print(f"Enviando mensagem promocional para o grupo '{group_name}' às {time.strftime('%H:%M:%S')}")

    # Acessa o grupo
    find_group(group_name)

    # Envia a mensagem
    send_message(message)

    # Envia a foto
    send_photo(photo_path)


def send_hourly_message():
    group_name = "test"
    tz_brazil = pytz.timezone('America/Sao_Paulo')
    now = datetime.now(tz_brazil)
    current_time = now.strftime('%H:%M')

    # Gera uma lista de 11 minutos aleatórios entre 0 e 59
    random_minutes = sorted(random.sample(range(60), 11))

    times = [now.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=m) for m in random_minutes]
    times_str = '\n'.join([f"✅🕘{t.strftime('%H:%M')}" for t in times])

    message = f"""⏰ ATENÇÃO SESSÃO DAS {current_time}! HORÁRIO DE BRASÍLIA!

Funciona em quais jogos?
🐯TIGRE 🐂TOURO 🐇COELHO 🐲DRAGÃO

{times_str}

Plataforma com a Falha
➡️ https://go.aff.donald.bet/spnpc6hv

Horários enviados com base nos Históricos da Plataforma 📈
➖➖➖➖➖➖➖➖➖➖➖

🚨 PRÓXIMA SESSÃO ➡️ {(now + timedelta(hours=1)).strftime('%H:%M')} ⏰"""

    print(f"Enviando mensagem de horário para o grupo '{group_name}' às {time.strftime('%H:%M:%S')}")

    # Acessa o grupo
    find_group(group_name)

    # Envia a mensagem
    send_message(message)


# Login no WhatsApp Web
login_whatsapp()

# Agendamento das mensagens
schedule.every().day.at("09:01").do(send_promotional_message)
schedule.every().day.at("00:54").do(send_promotional_message)
schedule.every().hour.at(":20").do(send_hourly_message)  # Mensagem a cada hora

print("Agendamentos configurados. O bot está em execução...")

# Loop para manter o script rodando e verificar os horários
while True:
    schedule.run_pending()
    time.sleep(1)  # Verifica a cada minuto