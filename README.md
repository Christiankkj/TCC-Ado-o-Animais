# Sistema de Denúncia e Adoção de Animais

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Sistema web para registro de denúncias de animais em situação de rua e divulgação de pontos de adoção.**

Projeto desenvolvido como Trabalho de Conclusão de Curso (TCC), com foco na utilização da tecnologia como ferramenta de apoio à proteção animal no município de Euclides da Cunha, Bahia.

---

## Sobre o projeto

O abandono de animais é um problema que afeta diversas comunidades. A falta de informações centralizadas dificulta a identificação de animais em situação de rua e o acesso a oportunidades de adoção.

Diante desse cenário, o projeto propõe uma plataforma web na qual usuários podem registrar denúncias, informar a localização de animais e cadastrar pontos de adoção.

A aplicação utiliza mapas interativos para facilitar a visualização e localização das informações cadastradas.

## Objetivos

- Facilitar o registro de denúncias de animais em situação de rua.
- Permitir a identificação geográfica dos locais denunciados.
- Divulgar pontos de adoção.
- Centralizar informações sobre animais e locais de acolhimento.
- Incentivar a participação da comunidade na proteção animal.

## Funcionalidades implementadas

- Cadastro de usuários dos tipos pessoa e empresa.
- Autenticação e encerramento de sessão.
- Criptografia de senhas por meio de hash.
- Validação de formulários.
- Registro de denúncias de animais.
- Classificação por tipo: gato, cachorro ou ambos.
- Registro da quantidade de animais.
- Armazenamento de coordenadas geográficas.
- Cadastro de pontos de adoção.
- Associação dos registros aos usuários responsáveis.
- Consulta de denúncias e pontos de adoção na aplicação.
- Página inicial e página de apresentação do projeto.

## Tecnologias utilizadas

### Back-end

- Python
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- PyMySQL

### Front-end

- HTML5
- CSS3
- JavaScript
- Leaflet
- OpenStreetMap

### Banco de dados

- MySQL

### Ferramentas

- Git
- GitHub
- Visual Studio Code

---

## Como executar o projeto

Atualmente, a aplicação foi estruturada para execução local, utilizando Python, Flask e MySQL.

### 1. Pré-requisitos

Antes de começar, instale:

- [Python](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/) (opcional)

### 2. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Christiankkj/TCC-Ado-o-Animais.git
```

Entre na pasta do projeto:

```bash
cd TCC-Ado-o-Animais
```

### 3. Criar ambiente virtual

No Windows, execute:

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
venv\Scripts\activate
```

### 4. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

### 5. Configurar o banco de dados

Abra o MySQL e crie o banco:

```sql
CREATE DATABASE animaisabandono;
```

O repositório contém o arquivo `banco.sql`, responsável por definir as tabelas utilizadas pelo sistema.

Antes de importá-lo, confira a correspondência entre os nomes das tabelas do script e os utilizados no código. Em particular, a tabela `ponto_adoacao` deve ser ajustada para `ponto_adocao`.

Depois de corrigir o script, execute:

```bash
mysql -u root -p animaisabandono < banco.sql
```

Informe a senha do MySQL quando solicitado.

### 6. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Configure a conexão com o banco de dados:

```env
DATABASE_URL=mysql+pymysql://root:SUA_SENHA@localhost:3306/animaisabandono
```

Substitua `SUA_SENHA` pela senha configurada no MySQL.

Não compartilhe esse arquivo nem envie suas credenciais ao GitHub.

### 7. Executar a aplicação

Com o banco configurado e o ambiente virtual ativado, execute:

```bash
python app.py
```

Acesse a aplicação pelo navegador:

```text
http://127.0.0.1:5000
```

---

## Estrutura do projeto

```text
TCC-Ado-o-Animais/
│
├── static/
│   ├── css/
│   ├── js/
│   └── imagens/
│
├── templates/
│   ├── auth/
│   ├── home.html
│   └── sobre.html
│
├── app.py
├── auth.py
├── database.py
├── forms.py
├── models.py
├── banco.sql
├── requirements.txt
├── .env
└── .gitignore
```

A estrutura interna de `static/` e `templates/` pode variar conforme as atualizações do projeto.

## Banco de dados

O sistema utiliza o MySQL para armazenar informações relacionadas aos usuários, denúncias e pontos de adoção.

Principais entidades:

**Usuários**
- Identificador.
- Tipo de usuário.
- Nome.
- E-mail.
- Senha armazenada como hash.

**Denúncias**
- Identificador.
- Tipo de animal.
- Quantidade.
- Coordenadas.
- Usuário responsável.
- Data de criação.

**Pontos de adoção**
- Identificador.
- Nome do local.
- Tipo de animal.
- Quantidade disponível.
- Contato do responsável.
- Coordenadas.
- Usuário responsável.

## Execução e hospedagem

| Característica | Situação |
|---|---|
| Execução local | Sim |
| Banco de dados | MySQL |
| Aplicação web | Flask |
| Acesso pela internet | Não há hospedagem pública documentada |
| Servidor de produção | Não configurado |
| Uso em produção | Ainda não recomendado |

O projeto utiliza um servidor de desenvolvimento Flask e depende de um banco de dados MySQL configurado no ambiente.

## Status do projeto

**Protótipo acadêmico em desenvolvimento.**

O projeto possui funcionalidades de autenticação, registro de denúncias e cadastro de pontos de adoção, mas ainda necessita de correções de integração, validação e aprimoramentos antes de ser considerado uma aplicação completa.

## Próximas melhorias

- Corrigir e padronizar a estrutura do banco de dados.
- Aprimorar o gerenciamento de sessões e configurações de segurança.
- Finalizar a integração das funcionalidades com o mapa.
- Implementar testes das principais funcionalidades.
- Melhorar a validação e o tratamento de erros.
- Preparar a aplicação para hospedagem em um servidor de produção.

---

## Objetivo social

Utilizar a tecnologia para facilitar a identificação de animais em situação de rua, incentivar a adoção responsável e contribuir para a conscientização da comunidade sobre o abandono animal.
