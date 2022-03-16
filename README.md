# Sistema de Gerenciamento de Clínica PET

### Funcionalidades

- #### Cadastros
    - Cadastro de Cliente (CRUD)
      ![Cadastro de Cliente](docs/lista-clientes.png)
      &nbsp;
    - Cadastro de Pet (Inserção e Visualização)
      ![Cadastro de Pet](docs/cadastro-pets.png)
      &nbsp;
    - Cadastro de Funcionário (Inserção e Visualização)
      ![Cadastro de Funcionário](docs/cadastro-funcionario.png)
      &nbsp;

- #### Agendamento de Consulta para Pet
  ![Agendamento de Consulta para Pet](docs/cadastro-consulta.png)

- #### Documentos
    - Exportar Dados de Consulta de um Pet para PDF
    - Envio das informações de Consulta de um Pet por E-mail

![Dados da Consulta de Pet](docs/dados-consulta.png)
&nbsp;

- #### Autenticação
    - Login
    - Logout

- #### Autorização - Níveis de Acesso às funcionalidades de acordo com o Cargo do Usuário
    - Financeiro
        - Apenas usuários com este Cargo podem Cadastrar e Visualizar Funcionários
        - Apenas usuários com este Cargo podem Editar e Excluir dados de Clientes
    - Veterinário
        - Apenas usuários com este Cargo podem Cadastrar Consultas para Pets
    - Atendimento
        - Acessa todas as outras funcionalidades

--- 

### Tecnologias

- Back-end
    - Django
    - MySQL (Desenvolvimento)
    - PostgreSQL (Produção)
- Front-end
    - HTML
    - CSS
    - Bootstrap
    - jQuery Mask Plugin
    - Django AdminLTE 2
- Versionamento
    - Git
- Cloud
    - Heroku

---

### Live Demo (Clique na imagem)

[![Live Demo](https://upload.wikimedia.org/wikipedia/commons/8/89/Logo_di_Heroku.png?20160717173025)](https://django-pet.herokuapp.com/app/login/)

###### Obs.: Como utilizo um servidor gratuito, pode demorar um pouco até o site abrir.

#### Usuários para teste

- Veterinário
    - Login: teste_veterinario
    - Senha: Mud@r123
- Financeiro
    - Login: teste_financeiro
    - Senha: Mud@r123