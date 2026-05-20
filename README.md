# Aplicação Full-Stack de Gerenciamento de Usuários

Aplicação full-stack que demonstra os princípios de **Arquitetura Limpa (Clean Architecture)** e **SOLID**, construída com FastAPI no backend e Vue 3 no frontend.

---

## Arquitetura

O projeto segue uma abordagem de **Arquitetura Limpa modular**, separando as responsabilidades em camadas bem definidas:

```
Domínio → Aplicação → Infraestrutura → Apresentação
```

Cada módulo (ex.: `auth`, `user`) é autocontido, com suas próprias entidades de domínio, casos de uso, interfaces de repositório, implementações de infraestrutura e camada de apresentação (rotas da API / componentes de UI).

### Princípios de Design Aplicados

- **Single Responsibility Principle** — Cada classe e módulo possui uma única responsabilidade bem definida
- **Open/Closed Principle** — O comportamento é estendido por meio de novos casos de uso sem modificar os existentes
- **Liskov Substitution Principle** — As interfaces de repositório são substituíveis entre implementações SQL e em memória
- **Interface Segregation Principle** — As portas de domínio definem contratos específicos e enxutos
- **Dependency Inversion Principle** — A camada de aplicação depende de abstrações de repositório, não de implementações concretas

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.10, FastAPI 0.136, SQLAlchemy 2.0 |
| Banco de Dados | SQLite (dev), Alembic (migrações) |
| Autenticação | JWT via `python-jose`, esquema Bearer token |
| Validação | Pydantic v2, Pydantic Settings |
| Servidor | Uvicorn |
| Frontend | Vue 3, Vite 8 |
| Componentes de UI | PrimeVue 4, PrimeIcons |
| Estilização | Tailwind CSS 4 |
| Cliente HTTP | Axios |
| Roteamento | Vue Router 4 |
| Validação (FE) | Zod |

---

## Estrutura do Projeto

```
solid_pattern_clean_code/
├── back/                         # Backend FastAPI
│   ├── alembic/                  # Migrações do banco de dados
│   ├── app/
│   │   ├── core/                 # Config, DB, CORS, middleware, segurança
│   │   ├── modules/
│   │   │   ├── auth/             # Módulo de autenticação
│   │   │   │   ├── application/  # DTOs, casos de uso (login, registro)
│   │   │   │   ├── domain/       # Interface do repositório
│   │   │   │   ├── infrastructure/ # Implementação SQLAlchemy
│   │   │   │   └── presentation/ # Rotas da API
│   │   │   └── user/             # Módulo de gerenciamento de usuários
│   │   │       ├── application/  # DTOs, service, casos de uso (CRUD)
│   │   │       ├── domain/       # Entidades, interface do repositório, portas
│   │   │       ├── infrastructure/ # Implementação SQLAlchemy, mapper
│   │   │       └── presentation/ # Rotas da API
│   │   └── shared/               # Modelos base compartilhados
│   └── alembic.ini
└── front/                        # Frontend Vue 3
    └── src/
        ├── modules/
        │   ├── auth/             # Páginas de login e registro, store, services
        │   └── user/             # Páginas de listagem, criação e edição, store, services
        ├── router/               # Configuração do Vue Router
        └── shared/               # Cliente HTTP, componentes base, composables
```

---

## Endpoints da API

### Autenticação

| Método | Endpoint | Autenticação | Descrição |
|--------|----------|:---:|-------------|
| `POST` | `/auth/register` | Não | Registrar uma nova conta |
| `POST` | `/auth/login` | Não | Autenticar e receber um token JWT |

### Usuários

| Método | Endpoint | Autenticação | Descrição |
|--------|----------|:---:|-------------|
| `POST` | `/users` | Não | Criar um usuário |
| `GET` | `/users?page=1&size=10` | Sim | Listar usuários com paginação |
| `GET` | `/users/{id}` | Sim | Buscar usuário por ID |
| `PUT` | `/users/{id}` | Sim | Atualizar um usuário |
| `DELETE` | `/users/{id}` | Sim | Remover um usuário |

A documentação interativa da API está disponível em `http://localhost:8000/docs` (Swagger UI) e `http://localhost:8000/redoc` após iniciar o backend.

---

## Como Executar

### Pré-requisitos

- Python 3.10+
- Node.js 18+

### Backend

```bash
# Acesse o diretório do backend
cd back

# Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install fastapi uvicorn sqlalchemy alembic pydantic pydantic-settings python-jose

# Execute as migrações do banco de dados
alembic upgrade head

# Inicie o servidor de desenvolvimento
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`.

### Frontend

```bash
# Acesse o diretório do frontend
cd front

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

A aplicação estará disponível em `http://localhost:5173`.

---

## Fluxo de Autenticação

1. Crie uma conta em `/register` ou via `POST /auth/register`
2. Faça login em `/login` ou via `POST /auth/login` para receber um token JWT Bearer
3. O token é armazenado no `localStorage` e anexado automaticamente a todas as requisições protegidas por um interceptor do Axios
4. Rotas protegidas no frontend redirecionam usuários não autenticados para a página de login

---

## Configuração de Ambiente

O backend carrega as variáveis de ambiente do arquivo `.env.<ENV>` (padrão: `.env.dev`). Altere a variável `ENV` para trocar de perfil:

```env
# .env.dev
DATABASE_URL=sqlite:///./dev.db
```

Defina `ENV=prod` e forneça um arquivo `.env.prod` para configurar a URL do banco de dados em produção.

---

## Build para Produção

### Frontend

```bash
cd front
npm run build
```

O build de produção é gerado na pasta `front/dist/`.
