 # 📝 To-Do List em Django

Projeto de uma aplicação **To-Do List** desenvolvida com **Django**, onde o usuário pode **criar, visualizar, editar e excluir tarefas**. O objetivo do projeto é praticar os conceitos fundamentais do framework Django, como **models, views, templates e forms**

---

## 🚀 Funcionalidades

- ✅ Criar tarefas
- ✏️ Editar tarefas existentes
- 🗑️ Excluir tarefas
- 📋 Listar tarefas cadastradas

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12.3
- Django 6.0.6
- SQLite (banco de dados padrão do Django)
- HTML / CSS (templates)

---

## 📂 Estrutura do Projeto

```bash

project-to-do-list/
├── core/                      # Configurações principais do projeto Django
│   ├── asgi.py                # Configuração ASGI
│   ├── settings.py            # Configurações da aplicação
│   ├── urls.py                # Rotas globais do projeto
│   └── wsgi.py                # Configuração WSGI
│
├── tarefas/                   # Aplicação responsável pelo gerenciamento de tarefas
│   ├── migrations/            # Histórico de migrações do banco de dados
│   ├── static/
│   │   └── css/
│   │       └── style.css      # Estilos da aplicação
│   ├── templates/
│   │   ├── 404.html           # Página personalizada de erro
│   │   └── tarefas/
│   │       ├── base.html      # Template base
│   │       └── home.html      # Página principal
│   ├── admin.py               # Configurações do painel administrativo
│   ├── apps.py                # Configuração da aplicação
│   ├── forms.py               # Formulários Django
│   ├── models.py              # Modelos do banco de dados
│   ├── tests.py               # Testes automatizados
│   ├── urls.py                # Rotas da aplicação
│   └── views.py               # Lógica das views
│
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py                  # Utilitário de gerenciamento Django
└── README.md                  # Documentação do projeto

```

## ⚙️ Como rodar o projeto localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências

```bash
pip install django
```

### 4️⃣ Aplicar as migrações

```bash
python manage.py migrate
```

### 5️⃣ Rodar o servidor

```bash
python manage.py runserver
```

