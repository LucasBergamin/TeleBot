import telebot

CHAVE_API = "2098648256:AAEFf1rs0sxMCAaGCbrADSDWpmEdnsL2QsI"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo a pizza para a sua casa')

@bot.message_handler(commands=["hambuguer"])
def hambuguer(mensagem):
    bot.send_message(mensagem.chat.id, 'X-TUDAO A CAMINHO')

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, 'Não tem salada aqui não')

@bot.message_handler(commands=["opcao1"])
def opacao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /pizza Pizza
    /hambuguer Hambuguer
    /salada Salada
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opacao2(mensagem):
    bot.send_message(mensagem.chat.id, 'AQUI É PERFEITO')

@bot.message_handler(commands=["opcao3"])
def opacao3(mensagem):
    print(mensagem)
    bot.reply_to(mensagem, f"Valeu!! :) {mensagem.chat.first_name} {mensagem.chat.last_name}")
    bot.send_message(mensagem.chat.id, 'Bergamin mando outro abraço')

def validar(mensagem):
    return True

@bot.message_handler(func=validar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 reclar de um pedido
    /opcao3 mandar um abraço pro bergamin
Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)

bot.polling()

