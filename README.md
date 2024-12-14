# Ferramenta-CLI-Para-Gerar-Ambientes-de-Projeto-de-Ci-ncia-de-Dados

## Estrutura do projeto:
```bash
ds_project_cli/
├── __init__.py  (pode ficar vazio)
└── main.py
```
## Como usar:

Instalar o Typer: ```bash pip install typer ```

Salvar o código acima como main.py.

Executar: ```bash python main.py criar_projeto [nome_do_projeto] [--python-version VERSÃO] [--instalar-pacotes] ```

## Exemplos:
```bash
python main.py criar_projeto meu_projeto (cria o projeto "meu_projeto" com Python 3.9 e sem instalar pacotes)

python main.py criar_projeto meu_projeto --python-version 3.8 --instalar-pacotes (cria o projeto "meu_projeto" com Python 3.8 e instala os pacotes do requirements.txt)
```
## Explicação do código:

* Typer: Usamos o Typer para criar a CLI. Ele facilita a definição de comandos e argumentos.
* Pathlib: Usamos Pathlib para manipular caminhos de arquivos e diretórios de forma mais robusta e legível.
* Subprocess: Usamos o módulo subprocess para executar comandos shell, como criar o ambiente virtual e instalar pacotes.
* Tratamento de erros básico: incluído com exist_ok=False e check=True nos comandos mkdir e subprocess.run, respectivamente.

## Próximos passos:

* Adicionar mais opções à CLI: como adicionar um template de notebook, configurar um arquivo .env, etc.
* Melhorar o tratamento de erros: adicionar mensagens de erro mais informativas e tratamento de exceções.
* Criar um pacote instalável: para facilitar a distribuição e o uso da ferramenta.
* Testes: adicionar testes unitários para garantir a qualidade do código.
