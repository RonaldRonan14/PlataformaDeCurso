
# Plataforma de Cursos

A Plataforma de Cursos é um sistema web desenvolvido em Python com Flask para gerenciamento de cursos, aulas e favoritos. O projeto segue uma arquitetura em camadas e possui funcionalidades de autenticação e controle de acesso.

## Estrutura do Projeto

O projeto está dividido nas seguintes camadas:

- **Configuração:** Define configurações gerais e conexão com o banco de dados.
- **Domínio:** Contém entidades que representam os modelos de dados (ex.: Curso, Aula, Usuario).
- **Serviços:** Centraliza a lógica de negócios e validações.
- **Repositórios:** Gerencia acesso ao banco de dados e operações CRUD.
- **Apresentação:** Gerencia as interações do usuário, incluindo controladores e templates.

### Estrutura de Pastas

```
plataformaDeCursos/
├── Config.py
├── requirements.txt
├── run.py
├── .vscode/
├── Domain/
│   ├── Entities/
│   ├── Services/
├── Infrastructure/
│   ├── Repositories/
├── Presentation/
│   ├── Controllers/
│   ├── Autorize/
│   ├── Views/
```

## Funcionalidades

1. **Gestão de Cursos**
   - Criar, editar, ativar/desativar e excluir cursos.
2. **Gestão de Aulas**
   - Associar aulas a cursos, com informações como duração e descrição.
3. **Favoritos**
   - Usuários podem marcar cursos como favoritos.
4. **Autenticação e Controle de Acesso**
   - Administradores podem acessar funcionalidades restritas.
5. **Pré-visualização de Recursos**
   - Upload e exibição de imagens como capa do curso.

## URLs Principais

- **Usuários:** `http://127.0.0.1:5000/`
- **Administradores:** `http://127.0.0.1:5000/login/admin`

### Administrador Padrão
- **CPF:** `00000000000`
- **Senha:** `FGAWAAQYtEdb`

## Configuração e Execução

1. **Requisitos:**
   - Python 3.12+
   - SQLite

2. **Instalação:**
   - Clone este repositório:
     ```bash
     git clone https://github.com/seuusuario/seurepositorio.git
     ```
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```

3. **Iniciar o Servidor:**
   ```bash
   python run.py
   ```

4. **Configuração do Banco de Dados:**
   - As tabelas são criadas automaticamente na inicialização do servidor.

## Tecnologias Utilizadas

- Python 3.12
- Flask
- SQLAlchemy
- SQLite
- Bootstrap
