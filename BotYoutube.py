import telebot
from pytube import YouTube

bot = telebot.TeleBot("2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI")


@bot.message_handler(commands=['musica'])
def musica(mensagem):
    msg = bot.send_message(id(mensagem), "Por favor mande um link válido para que possamos fazer o dowload")
    bot.register_next_step_handler(msg, dowloadMusica)


@bot.message_handler(commands=['video'])
def video(mensagem):
    msg = bot.send_message(id(mensagem), "Por favor mande um link válido para que possamos fazer o dowload")
    bot.register_next_step_handler(msg, dowloandVideo)


def dowloandVideo(mensagem):
    try:
        yt = YouTube(f'{mensagem.text}')
        yt.streams.first().download(filename=f"{yt.title}.mp4", output_path='audio')
        bot.send_message(id(mensagem), f"Por favor aguarde um mínuto enquanto fazemos o dowload do seu vídeo {yt.title}")
        bot.send_video(chat_id=id(mensagem), data=open(f'audio/{yt.title}.mp4', 'rb'), timeout=400)
    except:
        bot.send_message(id(mensagem), "Por favor informe uma URL válida")


def dowloadMusica(mensagem):
    try:
        yt = YouTube(f'{mensagem.text}')
        yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.mp3", output_path='audio')
        bot.send_message(id(mensagem), f"Por favor aguarde um mínuto enquanto fazemos o dowload da sua música {yt.title}")
        bot.send_photo(id(mensagem), yt.thumbnail_url)
        bot.send_audio(chat_id=id(mensagem), audio=open(f'audio/{yt.title}.mp3', 'rb'), timeout=400)
    except:
        bot.send_message(id(mensagem), "Por favor informe uma URL válida")


def validar(mensagem):
    return True


def id(mensagem):
    return mensagem.chat.id


@bot.message_handler(func=validar)
def mensagem(mensagem):
            texto=f"""Olá {mensagem.chat.first_name} {mensagem.chat.last_name} seja bem vindo a o Bot do youtube :)
        
Você pode baixar um vídeo ou apenas uma música
Para baixar apenas o vídeo digite 
--> /video
Ou para baixar apenas a música digite 
--> /musica
"""
        bot.reply_to(mensagem, texto)


bot.polling()
