from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

def comandos_disponiveis():
    return (
        "📋 Comandos disponíveis:\n"
        "/start - Iniciar a interação com o bot.\n"
        "/ajuda - Ver esta lista de comandos.\n"
        "/noticias - Últimas notícias sobre a FURIA.\n"
        "/resultados - Resultados dos jogos da FURIA.\n"
        "/loja - Novidades da loja FURIA.\n"
        "/clipes - Ver os últimos clipes da FURIA."

    )

# Função que vai ser chamada quando o usuário enviar o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou o bot oficial da FURIA! Como posso ajudar você?\n\n" + comandos_disponiveis()
    )

# Função para exibir os comandos disponíveis
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(comandos_disponiveis()
    )

# Função para as últimas notícias sobre a FURIA
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Última notícia sobre a FURIA: 📰\n"
        "FURIA conquista vitória histórica no campeonato internacional de CS! 🎮🔥\n"
        "Confira mais em: https://www.furia.gg\n"
        + sugestao_comandos()
    )

# Função para mostrar os resultados dos jogos
async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Últimos resultados dos jogos da FURIA:\n"
        "FURIA vs Team Liquid: Vitória 2-0 🎮🏆\n"
        "FURIA vs Astralis: Derrota 1-2 ⚔️\n\n"
        "Próximo jogo:\n"
        "FURIA vs Natus Vincere: 12/05 às 16:00"
        + sugestao_comandos()
    )

# Função para mostrar novidades da loja
async def loja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Confira as novidades da loja FURIA:\n"
        "1. Camiseta oficial FURIA x Adidas 🦁👕 - Disponível agora!\n"
        "2. Boné exclusivo FURIA 🎩 - Só na nossa loja!\n\n"
        "Acesse a loja em: https://loja.furia.gg"
        + sugestao_comandos()
    )

async def clipes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Últimos clipes da FURIA no YouTube:\n\n"
        "🎬 Estamos na próxima fase! - MELHORES MOMENTOS x M80 #ESLProLeague 21: https://www.youtube.com/watch?v=0NluG5rZlWo\n"
        + sugestao_comandos()
    )

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(comandos_disponiveis())

def sugestao_comandos():
    return "\n\n👉 Para mais comandos, digite /comandos"
    
def main():
    # Substitua 'YOUR_TOKEN' pelo token que você obteve do BotFather
    application = Application.builder().token("7792477230:AAGREdOhSFPsYCfUrpx-5e7-SUFs_gem-YE").build()

    # Cria um manipulador de comando para o comando /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))  # Adicionando o comando /ajuda
    application.add_handler(CommandHandler("noticias", noticias))  # Adicionando o comando /noticias
    application.add_handler(CommandHandler("resultados", resultados))  # Adicionando o comando /resultados
    application.add_handler(CommandHandler("loja", loja))  # Adicionando o comando /loja
    application.add_handler(CommandHandler("clipes", clipes))
    application.add_handler(CommandHandler("menu", start))
    application.add_handler(CommandHandler("comandos", comandos))

    # Inicia o bot e começa a escutar por novas mensagens
    application.run_polling()

# Esta linha garante que o código só será executado se este arquivo for executado diretamente
if __name__ == '__main__':
    main()
