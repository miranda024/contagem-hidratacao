# Documentação do Projeto:  contagem de Hidratação CLI

**Versão:** 1.0.0
**Autor:** Miguel Lira Miranda
**Disciplina:** Bootcamp II

## 1. Descrição do Problema
A manutenção de níveis adequados de hidratação é um desafio comum para indivíduos que mantêm rotinas intensas de estudo ou trabalho em ambientes digitais. A negligência no consumo de água pode resultar em complicações de saúde, redução da capacidade cognitiva, fadiga e cefaleia. O problema central reside na falta de monitoramento quantitativo e personalizado da ingestão hídrica diária.

## 2. Proposta de Solução
O projeto consiste em uma ferramenta de linha de comando (CLI) desenvolvida em Python que permite o registro e monitoramento da ingestão de água. Diferente de calculadoras genéricas, esta aplicação implementa uma lógica de personalização baseada em dados do usuário:
* Cálculo de meta diária baseado no peso corporal.
* Diferenciação de volume necessário para praticantes de atividades físicas (50ml/kg) versus indivíduos sedentários (35ml/kg).
* Persistência de dados em formato JSON para acompanhamento do progresso.

## 3. Público-Alvo
Estudantes, profissionais de tecnologia e demais indivíduos que buscam uma ferramenta técnica, rápida e integrada ao terminal para gestão de hábitos saudáveis.

## 4. Tecnologias e Ferramentas
* **Linguagem:** Python 3.12
* **Gerenciamento de Dependências:** pip
* **Framework de Testes:** Pytest
* **Análise Estática (Linting):** Ruff
* **Integração Contínua (CI):** GitHub Actions

## 5. Estrutura do Projeto
A organização dos arquivos segue as boas práticas de separação de responsabilidades:
* `src/`: Contém o código-fonte da aplicação.
* `tests/`: Scripts de testes automatizados para validação de regras de negócio.
* `.github/workflows/`: Configuração da pipeline de integração contínua.
* `requirements.txt`: Declaração das dependências do projeto.
* `VERSION`: Registro do versionamento semântico.

## 6. Instruções de Instalação e Execução

### Pré-requisitos
* Python 3 instalado.

### Instalação
1. Clonar o repositório.
2. Navegar até o diretório do projeto.
3. Instalar as dependências necessárias:
```bash
   python -m pip install -r requirements.txt
```
### Execução
Para iniciar o rastreador, utilize o comando:
```bash
  python src/hidratacao.py
```
## 7. Qualidade e Validação Tecnológica

### Testes Automatizados
Foram implementados testes para cobrir o fluxo principal, validação de entradas negativas e cálculos de meta dinâmica. Para executar os testes:
```bash
   python -m pytest
```

### Análise Estática (Lint)
A padronização do código e a busca por vulnerabilidades estáticas podem ser realizadas via Ruff:
```bash
   python -m ruff check .
```
## 8. Dicas de Utilização e Reinicialização

### Como resetar os dados?
A aplicação utiliza o ficheiro `dados_agua.json` para persistir as informações do perfil e o histórico de consumo. Caso deseje realizar uma **nova personalização** (mudar o peso ou nível de atividade) ou limpar o histórico:

1. Feche a aplicação no terminal.
2. Apague o ficheiro `dados_agua.json` na pasta raiz do projeto.
3. Execute o programa novamente. O sistema detetará a ausência de dados e solicitará a criação de um novo perfil.
