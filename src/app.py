import streamlit as st
import json
import subprocess
import os

st.title("💰 Agente Financeiro")

# carregar dados
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "..", "data", "produtos.json")

with open(file_path, "r", encoding="utf-8") as f:
    produtos = json.load(f)

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    if st.button("Enviar"):

        prompt = f"""
        Você é um educador financeiro.
        Responda de forma simples.

        Produtos:
        {produtos}

        Pergunta: {pergunta}
        """

        with st.spinner("Gerando resposta..."):
            resposta = subprocess.run(
                ["ollama", "run", "mistral"],
                input=prompt.encode(),
                capture_output=True
            )

        st.write(resposta.stdout.decode())
