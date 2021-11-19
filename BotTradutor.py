from textblob import TextBlob
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

def traduzir(mensagem):
    mensagemTraduzida = TextBlob(mensagem.text).translate(to='en')
    engine.save_to_file(mensagemTraduzida, 'audio/mensagem.mp3')
    engine.runAndWait()
    return mensagemTraduzida

@bot.message_handler(func=validar)
def responder(mensagem):
    print(f"{mensagem.chat.first_name} {mensagem.chat.last_name} {mensagem.chat.id} {mensagem.text}")
    bot.reply_to(mensagem, f"""Olá {mensagem.chat.first_name} {mensagem.chat.last_name} seja bem vindo ao Bot tradutor :).

tudo que for escrito em português será traduzido para inglês e você receberá um áudio demonstrando o modo de falar""")
    try:
        mensagemTraduzida = traduzir(mensagem)
        bot.send_message(id(mensagem), "O modo de se falar a palavra em inglês")
        bot.send_audio(chat_id=id(mensagem), audio=open(f'audio/mensagem.mp3', 'rb'))
        bot.send_message(id(mensagem), f"A mensagem escrita em português: '{mensagem.text}' em inglês '{str(mensagemTraduzida)}'")
    except:
        bot.send_message(id(mensagem), "Por favor digite a palavra de modo correto")


bot.polling()