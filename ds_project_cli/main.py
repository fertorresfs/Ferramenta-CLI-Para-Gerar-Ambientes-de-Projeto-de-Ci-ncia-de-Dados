import typer
import os
from pathlib import Path
import subprocess

app = typer.Typer()

@app.command()
def criar_projeto(nome_projeto: str,
                 python_version: str = "3.9", #versão padrão
                 instalar_pacotes: bool = True):
    """
    Cria um novo projeto de Ciência de Dados.
    """

    # Criar diretório do projeto
    projeto_path = Path(nome_projeto)
    projeto_path.mkdir(exist_ok=False) # Não sobrescrever se já existir


    # Criar subdiretórios
    (projeto_path / "data").mkdir()
    (projeto_path / "notebooks").mkdir()
    (projeto_path / "src").mkdir()
    (projeto_path / "models").mkdir()
    (projeto_path / "reports").mkdir()



    # Criar arquivos
    (projeto_path / "README.md").touch()
    (projeto_path / ".gitignore").write_text("# Arquivos para ignorar\n__pycache__/\n.env\n")
    (projeto_path / "requirements.txt").touch()


    # Criar ambiente virtual (opcional, mas recomendado)
    venv_path = projeto_path / ".venv"
    subprocess.run([f"python{python_version}", "-m", "venv", str(venv_path)], check=True)
    typer.echo(f"Ambiente virtual criado em {venv_path}")

    # Instalar pacotes (opcional)
    if instalar_pacotes:
        # Ativar o ambiente virtual (dependente do sistema operacional)

        if os.name == 'posix': # Linux/macOS
            activate_script = venv_path / "bin" / "activate"
            subprocess.run(["source", str(activate_script), "&&", "pip", "install", "-r", "requirements.txt"], shell=True, cwd=projeto_path, check=True)
        elif os.name == 'nt': # Windows
            activate_script = venv_path / "Scripts" / "activate"
            subprocess.run([str(activate_script), "&&", "pip", "install", "-r", "requirements.txt"], shell=True, cwd=projeto_path, check=True)


        typer.echo("Pacotes instalados.")

    typer.echo(f"Projeto '{nome_projeto}' criado com sucesso!")


if __name__ == "__main__":
    app()
