# Excel Separator Pro 📊

Uma ferramenta administrativa moderna e eficiente para automação da separação de planilhas Excel baseada em representantes. O projeto oferece uma interface web intuitiva (estilo Dashboard) para processar grandes volumes de dados, mantendo a formatação original e permitindo downloads individuais ou em massa.

## 🚀 Funcionalidades

- **Dashboard Moderno**: Interface responsiva com design premium, glassmorphism e modo noturno.
- **Processamento em Tempo Real**: Console de logs integrado para acompanhar o status da extração.
- **Flexibilidade Total**: Suporta qualquer nome de arquivo de entrada (`.xlsx` ou `.xlsm`).
- **Fidelidade de Estilo**: Preserva larguras de colunas, fontes, cores e filtros da planilha original.
- **Downloads Inteligentes**: Gere arquivos individuais por representante ou baixe tudo compactado em um único `.zip`.
- **Backend Robusto**: Processamento em memória para máxima velocidade e segurança.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: [Python 3.9+](https://www.python.org/)
- **Framework Web**: [Flask](https://flask.palletsprojects.com/)
- **Manipulação de Excel**: [Openpyxl](https://openpyxl.readthedocs.io/)
- **Servidor de Produção**: [Gunicorn](https://gunicorn.org/)
- **Frontend**: HTML5, Vanilla CSS (Modern CSS Variables), Vanilla JavaScript.
- **Containerização**: [Docker](https://www.docker.com/)

## 💻 Como Executar

### Pré-requisitos
- Python 3.9 ou superior instalado.
- Pip (gerenciador de pacotes do Python).

### Instalação e Execução Local
1. Clone o repositório:
   ```bash
   git clone https://github.com/pethersonjr7/app-separacao-arquivos-adm.git
   cd app-separacao-arquivos-adm
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:
   ```bash
   python app.py
   ```

4. Acesse em seu navegador:
   `http://localhost:3000`

### Usando Docker 🐳
Se preferir rodar em um container isolado:

1. Construa a imagem:
   ```bash
   docker build -t excel-separator .
   ```

2. Inicie o container:
   ```bash
   docker run -p 3000:3000 excel-separator
   ```

## 📁 Estrutura do Projeto

- `app.py`: Servidor Flask principal e rotas de API.
- `processor.py`: Motor de lógica para separação e estilização das planilhas.
- `code.py`: Script original (legado) preservado com proteções de execução.
- `templates/`: Arquivos HTML da interface.
- `static/css/`: Estilização premium do dashboard.
- `Dockerfile`: Configuração para deploy via Docker.

---
Desenvolvido para otimização de fluxos administrativos. 🚀
