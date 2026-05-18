# Documentação do Projeto: Rastreador de Hidratação Web
Link da Aplicação: https://contagem-hidratacao-bf7y5wudbg2utclp5wubj3.streamlit.app/

**Versão:** 1.1.0
**Autor:** Miguel Lira Miranda
**Disciplina:** Bootcamp II


## Instruções para o Avaliador (Teste da API de Clima)

Para testar a funcionalidade de integração com o clima (OpenWeather) de forma imediata e sem a necessidade de criar uma nova conta, utilize a chave de testes abaixo:

* **Chave API OpenWeather:** `b0410757fca8b4cb515c200ed1d53497`

**Passo a passo para o teste:**
1. No menu lateral da aplicação, configure o seu peso.
2. No campo **Sua Cidade**, digite o nome de uma cidade (Dica: tente uma cidade quente como *Cuiabá* ou *Teresina* para ver a regra dos 30°C injetando +500ml de água automaticamente!).
3. Cole a chave de testes acima no campo **Chave API OpenWeather**.
4. Clique em **Salvar e Calcular Meta**.


## 1. Descrição do Problema
A manutenção de níveis adequados de hidratação é um desafio comum para indivíduos que mantêm rotinas intensas de estudo ou trabalho em ambientes digitais. A negligência no consumo de água pode resultar em complicações de saúde, redução da capacidade cognitiva, fadiga e cefaleia. O problema central reside na falta de monitoramento quantitativo e personalizado da ingestão hídrica diária.

## 2. Proposta de Solução
O projeto consiste em uma interface Web (GUI) construída com Streamlit desenvolvida em Python que permite o registro e monitoramento da ingestão de água. Diferente de calculadoras genéricas, esta aplicação implementa uma lógica de personalização baseada em dados do usuário:
* Cálculo de meta diária baseado no peso corporal.
* Diferenciação de volume necessário para praticantes de atividades físicas (50ml/kg) versus indivíduos sedentários (35ml/kg).
* Integração inteligente com API de clima para recalcular a meta em dias quentes.
* Persistência de dados em formato JSON para acompanhamento do progresso.

## 3. Público-Alvo
Estudantes, profissionais de tecnologia e demais indivíduos que buscam uma ferramenta técnica, rápida e moderna para gestão de hábitos saudáveis diretamente no navegador.

## 4. Tecnologias e Ferramentas
* **Linguagem:** Python 3.12
* **Interface Gráfica:** Streamlit
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

### Execução Local
Para iniciar o rastreador localmente, utilize o comando:
``` bash
py -m streamlit run src/hidratacao.py
```

## 7. Qualidade e Validação Tecnológica
### Testes Automatizados
Foram implementados testes para cobrir o fluxo principal, validação de entradas negativas e cálculos de meta dinâmica (incluindo testes de integração com mock da API externa). Para executar os testes:
``` bash
py -m pytest
```

### Análise Estática (Lint)
A padronização do código e a busca por vulnerabilidades estáticas podem ser realizadas via Ruff:

```Bash
py -m ruff check .
```

## 8. Dicas de Utilização e Reinicialização
### Como resetar os dados?
A aplicação utiliza o arquivo dados_agua.json para persistir as informações do perfil e o histórico de consumo. Caso deseje realizar uma nova personalização (mudar o peso ou nível de atividade) ou limpar o histórico:

Na barra lateral da própria aplicação web, clique no botão 🗑️ Zerar Histórico (Folha em Branco).

O sistema apagará o histórico automaticamente e reiniciará a tela de forma limpa, permitindo reconfigurar o perfil instantaneamente.