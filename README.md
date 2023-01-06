# **API Monday - Assistente Virtual**

A proposta deste projeto é a de criar um meio de interação entre um banco de dados e uma aplicação frontend baseada em uma assistente virtual.

## **Sumário**

<ul>
  <li>
    <h3><a href="#initialization"><b>Inicialização do projeto localmente</b></a>;</h3>
  </li>
  <li>
    <h3><a href="#der"><b>DER: Diagrama de Entidades e relacionamentos</b></a>:</h3>
    <ul>
      <li><a href="#der--user">Users</a>;</li>
      <li><a href="#der--schedules">Schedules</a>;</li>
      <li><a href="#der--quotas">Daily Quotas</a>;</li>
      <li><a href="#der--type">Type Choices</a>;</li>
      <li><a href="#der--type">Educational Level Choices</a>;</li>
      <li><a href="#der--type">Health Informations</a>;</li>
      <li><a href="#der--type">Finance Informations</a>;</li>
      <li><a href="#der--type">Academic Informations</a>;</li>
      <li><a href="#der--management">API Management</a>;</li>
    </ul>
  </li>
  <li>
    <h3><a href="#routes"><b>Rotas da aplicação</b></a>:</h3>
    <ul>
      <li>
        <h3><a href="#route--users">Users</a>:</h3>
        <ul>
          <li><a href="#route--post-user">POST users/</a>;</li>
          <li><a href="#route--get-user">GET users/</a>;</li>
          <li><a href="#route--get-profile">GET users/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile">GET users/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-profile">DELETE users/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">Schedules</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">POST schedules/</a>;</li>
          <li><a href="#route--get-profile-schedule">GET schedules/</a>;</li>
          <li><a href="#route--patch-profile-schedule">PATCH schedules/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">DELETE schedules/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">Daily Quotas</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">POST users/quotas/</a>;</li>
          <li><a href="#route--get-profile-schedule">GET users/quotas/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">PATCH users/quotas/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">DELETE users/quotas/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">Health Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">POST infos/health/</a>;</li>
          <li><a href="#route--get-profile-schedule">GET infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">PATCH infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">DELETE infos/health/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">Finance Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">POST infos/finances/</a>;</li>
          <li><a href="#route--get-profile-schedule">GET infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">PATCH infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">DELETE infos/finances/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">Academic Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">POST infos/academic/</a>;</li>
          <li><a href="#route--get-profile-schedule">GET infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">PATCH infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">DELETE infos/academic/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
    </ul>
</ul>

<br>

___

<br>
<h2 id="initialization"><b>Inicialização do projeto localmente</b></h2>
<br>

Primeiramente deve assegurar-se de que tem a [última versão do python](https://www.python.org/downloads/) instalada em sua máquina, além do [PostgreSQL](https://www.postgresql.org/) se optar por rodar as migrações da API para o database localmente. 

Após estas instalações, cheque se o *pip3*, o *python3* e o *postgres* foram instalados corretamente:

```powershell
python3 --version   # Python 3.11.0

pip3 --version      # pip 22.3.1 from C:\Python311\[...]\pip

psql --version      # psql (PostgreSQL) 14.5
```

Atualize seu *pip* para evitar possíveis erros durante as instalações de pacotes:

```powershell
# Windows
python.exe -m pip install --upgrade pip

# Linux
sudo -H pip3 install --upgrade pip

# MacOS
pip3 install --upgrade pip
```

Como toda aplicação desenvolvida em Python, será necessário iniciar um ambiente virtual para concentrar todas as instalações de extensões dentro do diretório do projeto. Para isso, vamos criar esse ambiente virtual através do seguinte comando:

```powershell
python -m venv venv
```

Agora, ative seu ambiente virtual:

```powershell
# Linux & MacOS
.\venv\bin\activate

# Windows
.\venv\Scripts\activate
```

Vamos instalar as dependências necessárias para o bom funcionamento da API de modo geral. Para isso, já dentro do ambiente virtual, utilize o comando abaixo para instalar estas dependências:

```powershell
pip install -r .\requirements.txt
```

***OPCIONAL***: Se optou por rodar a aplicação utilizando um database local, certifique-se de ter criado um database para armazenar esta aplicação logando em seu superuser psql:

```bash
C:\Meu_Projeto\Monday-VA> psql 
Password for user nome_do_usuario:  # digite sua senha aqui
psql (14.5)
Type "help" for help.

nome_do_usuario=>CREATE DATABASE "nome_do_database";
# Insira o nome do database dentro das "aspas"
```

Com todos estes passos encaminhados, você agora precisa executar as migrations, para que todas estas presentes nos apps da API possam constar no database:

```powershell
python .\manage.py migrate
```

Como último passo, rode o servidor local:
```bash
python .\manage.py runserver

# Se tudo estiver ok, você verá algo semelhante a isso aparecer em seu terminal:
Performing system checks...

System check identified no issues (0 silenced).
January 05, 2023 - 22:20:06
Django version 4.1.5, using settings '_core_.settings'
Starting development server at http://127.0.0.1:8000/ 
Quit the server with CTRL-BREAK.
```

### Pronto! Temos nosso servidor 100% funcional rodando localmente! Agora vamos abordar um pouquinho melhor sobre as relações entre as entidades.

<br>

___

<br>
<h2 id="der"><b>DER: Diagrama de Entidades e relacionamentos</b></h2>
<br>

O *Diagrama de Entidades e Relacionamentos* (**DER**) exemplifica em forma de um fluxograma a maneira que as entidades interagem dentro do banco de dados.

<br>

![Monday - Vitual Assistant API Entity Relationship Diagram](./ERD-Monday_VA.svg)

<br>

No caso da **Monday - Assistente Virtual**, temos 6 entidades se relacionando entre si através de uma 7ª chamada *API_Managements*, onde concentra todos os dados das demais. 
O usuário tem a opção de planejar sua rotina manualmente através da entidade *Schedules* ou, eventualmente, executar análises e oferecer automaticamente opções de rotina conforme as informações fornecidas pelas entidades de *Infos* & *Daily Quotas*.