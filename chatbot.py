import os
# Importação direta - agora deve funcionar sem o erro de 'LanguageModelInput'
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Configure sua chave aqui
os.environ['GROQ_API_KEY'] = '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'

# Inicializando o modelo Llama 3.3 70B
model = ChatGroq(model="llama-3.3-70b-versatile")

# Definindo a Persona
persona = "Você é um Especialista em Exploração Espacial, entusiasmado e técnico."
historico = [SystemMessage(content=persona)]

print("🚀 Sistema Pronto! (Digite 'x' para sair)")

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == 'x':
        print("Astro-Guia: Encerrando sistemas. Até logo!")
        break

    # Adiciona a pergunta do usuário ao histórico
    historico.append(HumanMessage(content=pergunta))

    # Gera a resposta
    try:
        resposta = model.invoke(historico)
        print(f"Astro-Guia: {resposta.content}")

        # Salva a resposta no histórico para manter o contexto
        historico.append(resposta)
    except Exception as e:
        print(f"Erro na API: {e}")
