# 🤖 Bia do Futuro — Agente Financeiro Educador

Projeto desenvolvido como solução para o lab da [DIO](https://www.dio.me/) **"Agente Financeiro Inteligente com IA Generativa"**.

---

## 💡 Sobre o Projeto

A **Bia** é um agente financeiro com IA que atua como **educadora financeira pessoal**. Em vez de apenas responder perguntas, ela analisa a situação do usuário, identifica problemas e orienta com ações práticas e linguagem acessível.

O foco está em **clareza e confiabilidade**: o agente evita respostas fora de contexto ou incorretas, garantindo que o usuário receba orientações úteis e seguras.

---

## ⚙️ Tecnologias

| Camada | Tecnologia |
|---|---|
| LLM | [Mistral](https://mistral.ai/) via [Ollama](https://ollama.com/) |
| Interface | [Streamlit](https://streamlit.io/) |
| Base de dados | Dados mockados (`data/`) |

---

## 🗂️ Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
├── 📁 data/                      # Dados mockados do cliente
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   └── produtos_financeiros.json
├── 📁 docs/                      # Documentação do agente
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   └── 03-prompts.md
├── 📁 src/
│   └── app.py                    # Aplicação Streamlit
└── README.md
```

---

## 🚀 Como Executar

**Pré-requisitos:** [Ollama](https://ollama.com/) e Python instalados.

```bash
# 1. Baixe o modelo
ollama pull mistral

# 2. Instale as dependências
pip install streamlit

# 3. Execute a aplicação
streamlit run src/app.py
```

---

## 📄 Documentação

A pasta `docs/` contém a documentação completa do agente:

- **01 — Documentação do Agente:** caso de uso, persona e arquitetura
- **02 — Base de Conhecimento:** estratégia de uso dos dados
- **03 — Prompts:** system prompt e exemplos de interação

