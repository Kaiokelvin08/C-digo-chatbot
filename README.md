# 👋 Olá, eu sou Kaio Kelvin

💻 Desenvolvedor em formação focado em Backend, Inteligência Artificial e Engenharia de Software.  
🚀 Atualmente desenvolvendo projetos envolvendo APIs, automação, sistemas inteligentes e aplicações Full Stack.  
📚 Estudante de Ciência da Computação com interesse em arquitetura de software, IA generativa e desenvolvimento de soluções escaláveis.

---
Como Utilizar o Chatbot com Groq API — Passo a Passo

Esse código cria um chatbot em Python utilizando:

LangChain;
API da Groq;
modelo Llama 3.3 70B.
Por que a API Key é necessária?

A API Key funciona como uma “identidade” do seu sistema dentro da plataforma da Groq.

Ela é necessária porque o seu código precisa se conectar aos servidores da Groq para utilizar o modelo de inteligência artificial Llama 3.3.

Sem essa chave:

a plataforma não sabe quem está fazendo a requisição;
o acesso ao modelo é bloqueado;
o chatbot não consegue gerar respostas.
O que acontece quando você usa a API Key?

Quando o código executa esta linha:

os.environ['GROQ_API_KEY'] = 'sua_chave'

o Python envia essa chave junto com cada requisição para a Groq.

A Groq então:

verifica se a chave é válida;
identifica sua conta;
libera acesso ao modelo de IA;
processa sua pergunta;
devolve a resposta do chatbot.
1. Criar conta na Groq

Acesse o site oficial da Groq

Depois:

Clique em Sign Up
Crie sua conta
Faça login no painel
2. Gerar sua API Key

Após entrar no painel:

Vá em:
API Keys
Clique em:
Create API Key
Dê um nome para a chave

Exemplo:

chatbot-python
Copie a chave gerada

Ela será parecida com:

gsk_xxxxxxxxxxxxxxxxx

Após ter a chave api key, você terá que adiciona-la no espaço direcionado a ela "SUA_CHAVE_API" na linha 6.

⚠️ IMPORTANTE:
Nunca compartilhe sua chave API publicamente.

3. Instalar as bibliotecas

No terminal execute:

pip install -U langchain-groq langchain-core
4. Criar o arquivo Python

Crie um arquivo chamado:

chatbot.py

Cole o código dentro dele.

5. Adicionar sua chave API

Substitua esta linha:

os.environ['GROQ_API_KEY'] = 'SUA_CHAVE'

Pela sua chave real:

os.environ['GROQ_API_KEY'] = 'gsk_xxxxxxxxx'
6. Executar o chatbot

No terminal execute:

python chatbot.py
7. Resultado esperado

Quando iniciar:

🚀 Sistema Pronto! (Digite 'x' para sair)

Você poderá conversar normalmente:

Você: O que é Marte?

Astro-Guia: Marte é o quarto planeta do sistema solar...
8. Como encerrar

Digite:

x

O programa será encerrado.

9. Melhor prática de segurança

Evite deixar sua chave diretamente no código.

O ideal é usar um arquivo:

.env

Exemplo:

GROQ_API_KEY=gsk_xxxxxxxxx

Depois utilize:

from dotenv import load_dotenv
load_dotenv()

Isso protege sua chave caso publique o projeto no GitHub.
# 🚀 Sobre Meu GitHub

Este GitHub foi estruturado para funcionar como:
- portfólio técnico;
- ambiente de estudos;
- laboratório de engenharia de software;
- vitrine de projetos reais;
- demonstração prática da minha evolução como desenvolvedor.

Aqui você encontrará projetos envolvendo:
- Python;
- APIs REST;
- Chatbots com IA;
- Sistemas de gerenciamento;
- Banco de dados;
- Estruturação de software;
- Arquitetura backend;
- Versionamento profissional com Git/GitHub.

---

# 🎯 Objetivo Profissional

Meu objetivo é evoluir constantemente como engenheiro de software, desenvolvendo aplicações:
- organizadas;
- escaláveis;
- documentadas;
- bem estruturadas;
- próximas de ambientes reais de desenvolvimento.

Busco aplicar boas práticas como:
- Clean Code;
- versionamento semântico;
- documentação técnica;
- modularização;
- arquitetura de sistemas;
- padronização de commits;
- integração com APIs modernas.

---

# 🧠 Visão Geral dos Projetos

Os projetos deste GitHub foram desenvolvidos para demonstrar:
- capacidade de resolução de problemas;
- construção de aplicações completas;
- organização de código;
- integração com IA;
- desenvolvimento backend;
- estruturação profissional de repositórios.

---

# 🌌 Projeto Destaque — Astro-Guia IA

## 📌 Contexto do Projeto

O Astro-Guia surgiu como um estudo prático sobre:
- integração com modelos de linguagem (LLMs);
- consumo de APIs de IA;
- gerenciamento de contexto em chatbots;
- engenharia de prompts;
- criação de assistentes inteligentes.

O projeto simula um especialista em exploração espacial capaz de responder perguntas técnicas e educativas utilizando inteligência artificial.

---

# 🎯 Objetivo do Projeto

O principal objetivo foi construir um chatbot funcional utilizando:
- Python;
- LangChain;
- API Groq;
- modelo Llama 3.3 70B.

Além disso, o projeto teve foco em:
- aprendizado de arquitetura de chatbots;
- gerenciamento de histórico de conversa;
- tratamento de erros;
- organização profissional de código.

---

# 🏗️ Arquitetura da Solução

## 🔹 Fluxo de Funcionamento

```text
Usuário → Interface Terminal → LangChain → API Groq → Modelo Llama 3.3 → Resposta
