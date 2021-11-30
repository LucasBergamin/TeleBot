import telebot
import sqlite
from datetime import datetime

bot = telebot.TeleBot("2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI")
sqlite = sqlite

tabela_usuario = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_chat INTEGER NOT NULL,
  apelido VARCHAR(100),
  idade INTEGER,
  cidade VARCHAR(100)
);
"""

conexao = sqlite.criando_conexao("usuarios.db")
sqlite.executando_query(conexao, tabela_usuario)

def id(mensagem):
    return mensagem.chat.id

def validar(mensagem):
    return True

def validarUsuario(mensagem):
    select_users = "SELECT * from users"
    users = sqlite.select_query(conexao, select_users)
    for user in users:
        if id(mensagem) in user:
            return True
    return False

@bot.message_handler(commands="cadastro")
def apelidoUsuario(mensagem):
    msg = bot.send_message(id(mensagem), "Para começar me diga como posso te chamar?")
    bot.register_next_step_handler(msg, idadeUsuario)

def idadeUsuario(mensagem):
    apelido = mensagem.text
    msg = bot.send_message(id(mensagem), "Me diga quantos anos você tem ?")
    atualizandoUsuario(mensagem, 'apelido', apelido)
    bot.register_next_step_handler(msg, cidadeUsuario)

def cidadeUsuario(mensagem):
    idade = mensagem.text
    msg = bot.send_message(id(mensagem), "E para finalizar me diga de qual cidade você é")
    atualizandoUsuario(mensagem, 'idade', idade)
    bot.register_next_step_handler(msg, criandoUsuario)

def criandoUsuario(mensagem):
    cidade = mensagem.text
    atualizandoUsuario(mensagem, 'cidade', cidade)

def atualizandoUsuario(mensagem, nome_coluna, valor):
    criando_usuario = f" UPDATE users SET {nome_coluna} = '{valor}' WHERE id_chat = ({id(mensagem)});"
    sqlite.executando_query(conexao, criando_usuario)

def horario():
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    if '19:00' > dt_string < '05:00':
        return "Tenha uma ótima Noite"
    elif '05:00' > dt_string < '11:00':
        return "Tenha um ótimo dia"
    else:
        return "Tenha uma ótima tarde"

@bot.message_handler(func=validar)
def responder(mensagem):
    if validarUsuario(mensagem):
        select_users = f"SELECT apelido FROM users WHERE id_chat = {id(mensagem)}"
        apelido = sqlite.select_query(conexao, select_users)
        bot.send_message(id(mensagem), f'Seja bem vindo novamente {apelido[0][0]}')
        bot.send_message(id(mensagem), horario())
    else:
        text = """ 
Olá, em minha base de daoos que essa é sua primeira vez conosco :)
Vamos criar seu cadastro?
    --> /cadastro
        """
        criando_usuario = f" INSERT INTO users (id_chat) VALUES ({id(mensagem)});"
        sqlite.executando_query(conexao, criando_usuario)
        bot.reply_to(mensagem, text)

bot.polling()
