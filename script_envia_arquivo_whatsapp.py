from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import time

def enviar_arquivo_whatsapp(driver, nome_grupo, caminho_arquivo):
    # Pesquisar e selecionar o grupo
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "_3FRCZ copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(nome_grupo)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)

    # Aguardar o grupo carregar
    time.sleep(5)

    # Anexar o arquivo
    anexo_button = driver.find_element_by_xpath('//div[@title="Anexar"]')
    anexo_button.click()
    time.sleep(2)

    # Selecionar a opção "Documento"
    documento_button = driver.find_element_by_xpath('//input[@accept="*"]')
    documento_button.send_keys(caminho_arquivo)
    time.sleep(2)

    # Enviar o arquivo
    enviar_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    enviar_button.click()
    time.sleep(2)

def executar_envio_semanal():
    # Configurar o caminho do driver do Selenium (por exemplo, para o Chrome)
    driver_path = '/caminho/para/chromedriver'

    # Iniciar o driver do Selenium
    driver = webdriver.Chrome(driver_path)

    # Abrir o WhatsApp Web
    driver.get('https://web.whatsapp.com/')
    time.sleep(20)  # Esperar alguns segundos para fazer login manualmente

    # Dados do arquivo e grupo
    nome_grupo = 'Nome do Grupo'
    caminho_arquivo = '/caminho/do/arquivo.mp4'

    # Verificar o dia da semana atual
    dia_semana_atual = datetime.now().strftime('%A')

    # Definir o dia e horário de envio (por exemplo, todas as segundas às 9:00)
    dia_envio = 'Monday'
    horario_envio = '09:00'

    # Calcular a data e horário do próximo envio
    data_envio = datetime.strptime(dia_envio, '%A').date()
    while data_envio.strftime('%A') != dia_semana_atual:
        data_envio += timedelta(days=1)
    horario_envio_dt = datetime.strptime(horario_envio, '%H:%M').time()
    data_hora_envio = datetime.combine(data_envio, horario_envio_dt)

    # Calcular o tempo restante para o próximo envio
    tempo_restante = (data_hora_envio - datetime.now()).total_seconds()

    # Aguardar até o horário de envio
    time.sleep(tempo_restante)

    # Enviar o arquivo
    enviar_arquivo_whatsapp(driver, nome_grupo, caminho_arquivo)

    # Aguardar alguns segundos antes de fechar o navegador
    time.sleep(5)

    # Fechar o navegador
    driver.quit()

# Executar o envio semanal
executar_envio_semanal()