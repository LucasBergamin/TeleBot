import telebot
import pyttsx3

CHAVE_API = "2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI"
bot = telebot.TeleBot(CHAVE_API)
engine = pyttsx3.init()

engine.setProperty("voice", "brazil")
engine.setProperty("rate", 190)
engine.setProperty("volume", 1.)
engine.runAndWait()

def validar(mensagem):
    return True

def repitirAudio(mensagem):
    audio = engine.say(mensagem.text)
    engine.runAndWait()
    return audio

def id(mensagem):
    return mensagem.chat.id

@bot.message_handler(commands=['start'])
def start(mensagem):
    bot.send_message(id(mensagem), "Mandando audio")
    bot.send_audio(chat_id=id(mensagem), audio=open('audio/ola.mp3', 'rb'))
    engine.runAndWait()

@bot.message_handler(func=validar)
def responder(mensagem):
    bot.reply_to(mensagem, 'Olá, Digite /start para começar')

bot.polling()
