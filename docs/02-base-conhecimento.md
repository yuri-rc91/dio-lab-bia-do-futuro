# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo                   | Formato | Utilização no Agente                                                                         |
| ------------------------- | ------- | -------------------------------------------------------------------------------------------- |
| `transacoes.csv`          | CSV     | Analisar padrão de gastos, identificar categorias e variações ao longo do tempo              |
| `perfil_usuario.json`     | JSON    | Armazenar informações como renda, objetivos financeiros e preferências                       |
| `metas_financeiras.json`  | JSON    | Definir e acompanhar metas como reserva de emergência ou quitação de dívidas                 |
| `regras_financeiras.json` | JSON    | Fornecer diretrizes básicas (ex: limites de gastos, boas práticas de organização financeira) |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram realizadas pequenas expansões nos dados mockados com o objetivo de melhorar a diversidade das opções financeiras.
As modificações incluem:
- Inclusão de novos ativos, como Fundos Imobiliários (FII) e ETF
- Ampliação das possibilidades de recomendação com base em diferentes perfis de risco
Essas alterações permitem que o agente ofereça sugestões mais completas e alinhadas aos objetivos do usuário.

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados a partir de arquivos locais no formato JSON (e opcionalmente CSV), utilizando Python.
O carregamento ocorre no início da execução, permitindo que as informações sejam utilizadas na geração de respostas pelo modelo.

Exemplo de implementação:

```python
import json
import subprocess

with open("produtos.json", "r") as f:
    produtos = json.load(f)

prompt = f"Explique de forma simples qual é o investimento mais seguro entre esses: {produtos}"

resposta = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt.encode(),
    capture_output=True
)

print(resposta.stdout.decode())
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são carregados a partir dos arquivos da pasta data e inseridos diretamente no prompt como contexto.
Essas informações são organizadas e incluídas antes da pergunta do usuário, permitindo que o modelo gere respostas mais relevantes.
Os dados são consultados dinamicamente a cada execução, sendo atualizados conforme as informações disponíveis.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Renda mensal: R$ 3.000
- Saldo disponível: R$ 1.200

Resumo financeiro:
- Total de receitas: R$ 3.000
- Total de despesas: R$ 2.500
- Saldo: R$ 500

Últimas transações:
- 01/03: Supermercado - R$ 450
- 05/03: Transporte - R$ 120
- 10/03: Lazer - R$ 200

Produtos disponíveis:
- Tesouro Selic (baixo risco, indicado para reserva de emergência)
- CDB Liquidez Diária (baixo risco, rendimento diário)
- Fundo Imobiliário (risco médio, renda mensal)
- ETF Ibovespa (risco médio, diversificação)
```
