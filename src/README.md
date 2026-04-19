# Passo a passo para execução

1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Criar e ativar ambiente virtual
python -m venv .venv
Ativar no Windows:
.venv\Scripts\activate

3. Instalar dependências
pip install -r requirements.txt

4. Instalar e rodar o Ollama
Baixe e instale o Ollama:
https://ollama.com/download
Depois, no terminal:
ollama run mistral

5. Executar a aplicação
streamlit run src/app.py

6. Acessar no navegador
A aplicação abrirá automaticamente em:
http://localhost:8501


## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```
