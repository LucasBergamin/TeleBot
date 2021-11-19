import telebot
import pyttsx3

CHAVE_API = "2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI"
bot = telebot.TeleBot(CHAVE_API)
engine = pyttsx3.init()

engine.setProperty("voice", "brazil")
engine.setProperty("rate", 190)
engine.setProperty("volume", 1.)
engine.runAndWait()

engine.save_to_file("Saiba que eu te amo mais que tudo nesse mundo meu amorzinho", 'audio/amor.mp3')
engine.runAndWait()

bot.send_audio(chat_id=2108547649, audio=open(f'audio/mensagem.mp3', 'rb'))
bot.send_message(2108547649, "Eu te amo demais meu amor")