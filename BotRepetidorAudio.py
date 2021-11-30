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

def id(mensagem):
    return mensagem.chat.id

def salvarAudio(mensagem):
    engine.save_to_file(f"{mensagem.text}", f"audio/audio.mp3")
    engine.runAndWait()

@bot.message_handler(func=validar)
def responder(mensagem):
    bot.reply_to(mensagem, f"Olá {mensagem.chat.first_name} {mensagem.chat.last_name} esse bot foi programado para tudo que você mandar escrito ele te responder em formato de audio")
    salvarAudio(mensagem)
    bot.send_audio(chat_id=id(mensagem), audio=open(f'audio/audio.mp3', 'rb'))

bot.polling()
