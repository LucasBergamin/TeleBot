from selenium import webdriver
from selenium.webdriver.common.by import By
import telebot

CHAVE_API = "2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI"
bot = telebot.TeleBot(CHAVE_API)

def id(mensagem):
    return mensagem.chat.id

@bot.message_handler(commands="atual")
def previsaoAtual(mensagem):
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.get("https://www.climadobrasil.com.br/estado-de-sao-paulo/campinas")
    atual = browser.find_element(By.XPATH, '//*[@id="headerCity"]/div/section/section[1]/p/span').text
    browser.quit()
    bot.send_message(id(mensagem), f"No momento está fazendo: {atual} C")

@bot.message_handler(commands="amanha")
def previsaoAmanha(mensagem):
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.get("https://www.climadobrasil.com.br/estado-de-sao-paulo/campinas")
    maxima = browser.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/div[1]/div[2]/div[2]/div[2]/span[1]/span').text
    minima = browser.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/div[1]/div[2]/div[2]/div[2]/span[2]/span').text
    browser.quit()
    bot.send_message(id(mensagem), f"Amanhã irá fazer máxima de: {maxima} C e mínima de {minima} C")

@bot.message_handler(commands="semana")
def previsaoSemana(mensagem):
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.get("https://www.climadobrasil.com.br/estado-de-sao-paulo/campinas")
    for i in range(1, 8):
        dia = browser.find_element(By.XPATH, f'/html/body/div[2]/main/div[4]/div/section[4]/section/div/article/div[1]/div[2]/div[{i}]/div[1]/p[3]').text
        maxima = browser.find_element(By.XPATH, f'/html/body/div[2]/main/div[4]/div/section[4]/section/div/article/div[1]/div[2]/div[{i}]/div[2]/span[1]/span').text
        minima = browser.find_element(By.XPATH, f'/html/body/div[2]/main/div[4]/div/section[4]/section/div/article/div[1]/div[2]/div[{i}]/div[2]/span[2]/span').text
        bot.send_message(id(mensagem), f"No dia {dia} irá fazer uma máxima de {maxima} C e uma miníma de {minima} C")
    browser.quit()

def validar(mensaegem):
    return True

@bot.message_handler(func=validar)
def mandarMensagem(mensagem):
    texto = f""" Olá {mensagem.chat.first_name} {mensagem.chat.last_name} seja bem vindo ao Bot da Previsão do tempo :)
Aparte /atual para saber a temperatura atual
Aparte /amanha para saber a temperatura de amanhã
Aparte /semana para saber a temperatura da semana toda. 
    """
    bot.reply_to(mensagem, texto)

bot.polling()
