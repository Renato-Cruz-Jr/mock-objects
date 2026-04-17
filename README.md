# Custom Stack & Number Sorter

Este projeto contém a implementação de uma classe de pilha (`CustomStack`) com capacidade limitada e uma classe `NumberAscOrder` que utiliza a pilha para ordenar uma coleção de números.

O projeto foi desenvolvido seguindo as práticas de TDD (Test-Driven Development), com 100% de cobertura de testes garantida pelo `pytest-cov` e uso de `pytest-mock` para isolamento de componentes.

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento localmente.

### 1. Clone o Repositório (se aplicável)

```sh
git clone https://github.com/Renato-Cruz-Jr/mock-objects.git
cd mock-objects
```

### 2. Crie e Ative o Ambiente Virtual

Um ambiente virtual é crucial para isolar as dependências do projeto.

**No Windows (PowerShell/CMD):**
```sh
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1
```

**No macOS e Linux (bash/zsh):**
```sh
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate
```

Após a ativação, você verá `(venv)` no início do seu prompt de comando.

### 3. Instale as Dependências

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias:

```sh
pip install -r requirements.txt
```

## Execução dos Testes

O projeto utiliza `pytest` para a execução dos testes.

### 1. Rodar todos os Testes

Para executar a suíte de testes completa e garantir que tudo está funcionando corretamente:

```sh
pytest
```

### 2. Rodar Testes com Relatório de Cobertura

Para executar os testes e gerar um relatório de cobertura de código no terminal, garantindo que 100% do código está sendo testado:

```sh
python -m pytest test --cov=src
```

Você deverá ver uma saída indicando 100% de cobertura para os módulos em `src/`.
