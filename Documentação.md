# Documentação do Sistema de Gestão de Contratos

## 1. Introdução

### 1.1 Visão Geral do Projeto
O Sistema de Gestão de Contratos é uma aplicação web desenvolvida para otimizar o processo de gerenciamento de contratos jurídicos, integrando tecnologias modernas de desenvolvimento web e recursos avançados de inteligência artificial para processamento de documentos

### 1.2 Objetivos do Sistema
- Facilitar o armazenamento e recuperação de contratos
- Automatizar a extração de informações de documentos PDF
- Implementar busca semântica em contratos
- Otimizar o preenchimento de formulários relacionados a contratos

### 1.3 Público-Alvo
- Profissionais jurídicos
- Gestores de contratos
- Administradores de sistemas

![projeto](/workspaces/virtualspace/assets/images/Screenshot_1.png)

### 2.2 Componentes Principais
- Frontend: HTMX + Tailwind CSS
- Backend: FastAPI
- Banco de Dados: PostgreSQL (via SQLAlchemy)
- Banco de Dados Vetorial: Milvus
- Processamento de IA: Sentence Transformers (BAAI/bge-large-en-v1.5)

### 2.3 Fluxo de Dados
1. O usuário interage com a interface web
2. Requisições são enviadas ao backend FastAPI via HTMX
3. O backend processa as requisições, interagindo com o PostgreSQL para dados estruturados
4. Para busca semântica, o backend utiliza o Milvus
5. Documentos PDF são processados utilizando PyPDF2 e modelos de IA

## 3. Tecnologias Utilizadas

### 3.1 Frontend
- HTMX: Para interatividade e atualizações dinâmicas
- Tailwind CSS: Para estilização e design responsivo


### 3.2 Backend
- FastAPI: Framework web para Python
- SQLAlchemy: ORM para interação com o banco de dados
- Pydantic: Para validação de dados


### 3.3 Banco de Dados
- PostgreSQL: Banco de dados relacional principal
- Milvus: Banco de dados vetorial para busca semântica


### 3.4 Inteligência Artificial
- Sentence Transformers (BAAI/bge-large-en-v1.5): Para geração de embeddings
- PyPDF2: Para extração de texto de PDFs


### 3.5 Autenticação e Autorização
- Keycloak: Para gerenciamento de usuários e controle de acesso


## 4. Configuração do Ambiente de Desenvolvimento

### 4.1 Requisitos de Sistema

- Python 3.9+
- Node.js 14+
- PostgreSQL 13+
- Docker (para Milvus)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gestao-contratos.git
cd gestao-contratos

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instale as dependências Python
pip install -r requirements.txt

# Instale as dependências Node.js
npm install

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# Inicie o banco de dados Milvus via Docker
docker-compose up -d milvus

# Inicie o servidor de desenvolvimento
uvicorn main:app --reload
```

## 5. Integração com IA

### 5.1 Processamento de PDFs

1. Extração de texto usando PyPDF2
2. Limpeza e pré-processamento do texto
3. Geração de embeddings usando Sentence Transformers


### 5.2 Armazenamento de Embeddings

- Utilização do Milvus para armazenar e indexar embeddings
- Exemplo de inserção no Milvus:


## 6. Segurança

### 6.1 Autenticação
- Utilização do Keycloak para gerenciamento de usuários e autenticação
- Implementação de JWT para autenticação stateless

### 6.2 Autorização
- Definição de roles e permissões no Keycloak
- Verificação de permissões em nível de API

### 6.3 Proteção de Dados
- Criptografia de dados sensíveis em repouso
- Utilização de HTTPS para todas as comunicações
- Implementação de rate limiting para prevenir abusos

##  Glossário
- **Embedding**: Representação vetorial de texto que captura significado semântico.
- **ORM**: Object-Relational Mapping, técnica para converter dados entre sistemas de tipos incompatíveis.
- **JWT**: JSON Web Token, um padrão aberto para criar tokens de acesso.
- **API**: Application Programming Interface, conjunto de definições e protocolos para integração de software.
- **CI/CD**: Continuous Integration/Continuous Deployment, práticas de desenvolvimento de software para entrega rápida e confiável.