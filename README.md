# **API Monday - Assistente Virtual**

A proposta deste projeto é a de criar um meio de interação entre um banco de dados e uma aplicação frontend baseada em uma assistente virtual.

## **Sumário**

<ul>
  <li>
    <h3><a href="#initialization"><b>1. Inicialização do projeto localmente</b></a>;</h3>
  </li>
  <li>
    <h3><a href="#der"><b>2. DER: Diagrama de Entidades e relacionamentos</b></a>:</h3>
    <ul>
      <li><a href="#der--user">2.1. Users</a>;</li>
      <li><a href="#der--schedules">2.2. Schedules</a>;</li>
      <ul>
        <li><a href="#der--type">2.2.1. Type Choices</a>;</li>
      </ul>
      <li><a href="#der--quotas">2.3. Daily Quotas</a>;</li>
      <li><a href="#der--health">2.4. Health Informations</a>;</li>
      <li><a href="#der--finance">2.5. Finance Informations</a>;</li>
      <li><a href="#der--academic">2.6. Academic Informations</a>;</li>
      <ul>
        <li><a href="#der--educational-level">2.6.1. Educational Level Choices</a>;</li>
      </ul>
      <li><a href="#der--management">2.7. API Management</a>;</li>
    </ul>
  </li>
  <li>
    <h3><a href="#routes"><b>3. Rotas da aplicação</b></a>:</h3>
    <ul>
      <li>
        <h3><a href="#route--users">3.1. Users</a>:</h3>
        <ul>
          <li><a href="#route--post-user">3.1.1. POST users/</a>;</li>
          <li><a href="#route--get-user">3.1.2. GET users/</a>;</li>
          <li><a href="#route--get-profile">3.1.3. GET users/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile">3.1.4. PATCH users/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-profile">3.1.5. DELETE users/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">3.2. Schedules</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.2.1 POST schedules/</a>;</li>
          <li><a href="#route--get-profile-schedule">3.2.2. GET schedules/</a>;</li>
          <li><a href="#route--patch-profile-schedule">3.2.3. PATCH schedules/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.2.4. DELETE schedules/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">3.3. Daily Quotas</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.3.1. POST users/quotas/</a>;</li>
          <li><a href="#route--get-profile-schedule">3.3.2. GET users/quotas/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">3.3.3. PATCH users/quotas/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.3.4. DELETE users/quotas/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">3.4. Health Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.4.1. POST infos/health/</a>;</li>
          <li><a href="#route--get-profile-schedule">3.4.2. GET infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">3.4.3. PATCH infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.4.4. DELETE infos/health/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">3.5. Finance Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.5.1. POST infos/finances/</a>;</li>
          <li><a href="#route--get-profile-schedule">3.5.2. GET infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">3.5.3. PATCH infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.5.4. DELETE infos/finances/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--schedule">3.6. Academic Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.6.1. POST infos/academic/</a>;</li>
          <li><a href="#route--get-profile-schedule">3.6.2. GET infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-schedule">3.6.3. PATCH infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.6.4. DELETE infos/academic/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
    </ul>
</ul>

<br>

___

<br>
<h2 id="initialization"><b>1. Inicialização do projeto localmente</b></h2>
<br>

Primeiramente deve assegurar-se de que tem a [última versão do python](https://www.python.org/downloads/) instalada em sua máquina, além do [PostgreSQL](https://www.postgresql.org/) se optar por rodar as migrações da API para o database localmente. 

Após estas instalações, cheque se o *`pip3`*, o *`python3`* e o *`postgres`* foram instalados corretamente:

```powershell
python3 --version   # Python 3.11.0

pip3 --version      # pip 22.3.1 from C:\Python311\[...]\pip

psql --version      # psql (PostgreSQL) 14.5
```

Atualize seu *`pip`* para evitar possíveis erros durante as instalações de pacotes:

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
<h2 id="der"><b>2. DER: Diagrama de Entidades e relacionamentos</b></h2>
<br>

O *Diagrama de Entidades e Relacionamentos* (**DER**) exemplifica em forma de um fluxograma a maneira que as entidades interagem dentro do banco de dados.

<br>

![Monday - Vitual Assistant API Entity Relationship Diagram](./ERD-Monday_VA.svg)

<br>

No caso da **Monday - Assistente Virtual**, temos 6 entidades se relacionando entre si através de uma 7ª chamada *`API_Managements`*, onde concentra todos os dados das demais. 
O usuário tem a opção de planejar sua rotina manualmente através da entidade *`Schedules`* ou, eventualmente, executar análises e oferecer automaticamente opções de rotina conforme as informações fornecidas pelas entidades de *`Infos`* & *`Daily Quotas`*.

<br>

### Abaixo descreveremos mais detalhadamente a função de cada uma das entidades presentes no diagrama.

<br>

___

<br>
<h2 id="der--user"><b>2.1. Users</b> 👤</h2>
<br>

A entidade *`Users`*, assim como na maioria dos casos, tem como função o cadastro de novos usuários.

Ela contará com um CRUD completo, podendo-se Criar, Listar, Recuperar, Atualizar ou Deletar um usuário, sendo a deleção inicialmente um HARD delete.

Mais adiante, assim como para as outras entidades, detalharemos quais as chaves necessárias para a interação com esse CRUD, bem como seus endpoints e verbos HTTP.

<br>
<h2 id="der--schedules"><b>2.2. Schedules</b> 📒</h2>
<br>

A entidade *`Schedule`* será a responsável por disponibilizar ao usuário uma forma de adicionar manualmente ao seu calendario novos agendamentos.

Diferentemente das entidades de **Cotas** e **Informações** a interação de *`Schedules`* num ambito geral ocorrerá de forma totalmente dependente do que o usuário definir.

Esta, como demonstrado no diagrama, oferece a possibilidade de inserir um evento customizado e defini-lo como rotina (ou não).

<br>
<h3 id="der--schedules"><b>2.2.1. Type Choices</b> 🔁</h3>
<br>

Ainda sobre *`Schedules`*, será fornecido um campo **`type`**, que definirá o tipo de *agendamento* que desejamos realizar. Para tal, temos 6 tipos diferentes de agendamento, sendo eles:

- `Work`: Para agendamentos relacionados a vida profissional;
- `Sleep`: Para agendamentos relacionados a horários de sono ou de "momentos extras" relacionados a descanso;
- `Study`: Para agendamentos relacionados a sua vida acadêmica;
- `Hobby`: Para agendamentos relacionados a lazer, como encontros, viagens turísticas, jogos e afins;
- `Health`: Para agendamentos relacionados a saúde de modo geral, como visitas a clínicos, terapias, cirurgias e visitas a hospitais;
- `Commitment` (valor padrão): Para agendamentos genéricos que não se encaixam em nenhuma das categorias anteriores;

<br>
<h2 id="der--quotas"><b>2.3. Daily Quotas</b> 📊</h2>
<br>

As *`Daily Quotas`* oferecerão a possibilidade do usuário definir cotas de atividades que deseja inserir em seu dia-a-dia em forma de porcentagem (um número entre 0 e 1). A API fornecerá opções de cotas para **horas de sono, trabalho, estudos, momentos de lazer e cuidados com a saúde**(como academia, caminhada e meditação por exemplo).

Vale ressaltar que nem todas as cotas serão calculadas da mesma forma. Algumas serão calculadas a partir do dia completo (24h), enquanto outras serão calculadas conforme o tempo restante de seu dia.

**POR EXEMPLO:** O *`horário de sono`* é uma cota que será calculada a partir de 24h, bem como a soma de todos os agendamentos (*`Schedules`*), enquanto as demais cotas serão calculadas pelo restante do dia útil. Se definirmos a cota diária de sono como *`0.25`* (25% de 24h, ou seja, 6h) e, além disso, definirmos um total de 4h de rotina, teremos um restante de dia útil igual a **`14 horas`** (24 - 6 - 4 = 10 horas). Essas 14h restantes serão a base da qual será calculada as outras cotas.

Sabendo disso e definindo um exemplo para todas as cotas, teremos um resultado semelhante a seguinte tabela:

<center>

___
|  | `Cotas` | `Hora Base` | `Cálculo` | `Horas Diárias` | `Restante diário` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **`Agendamentos`** | - | 24h | - | 4h | - |
| **`Horário de Sono`** | 0.25 | 24h | 24 x 0.25 | 6h | - |
| **`Horas Fixas`** | - | 24h | 4 + 6 | 10h | ***14h*** |
| **`Horário Útil Restante`** | - | - | 24 - 10 | 14h | - |
| **`Trabalho`** | 0.4 | 14h | 14 x 0.4 | 5h36min | 8h24min |
| **`Estudo`** | 0.25 | 14h | 14 x 0.25 | 3h30min | 4h54min |
| **`Lazer`** | 0.15 | 14h | 14 x 0.15 | 2h06min | 2h48min |
| **`Saúde`** | 0.2 | 14h | 14 * 0,2 | 2h48min | **Dia preenchido** |
___

</center>

Vale ressaltar que as cotas fornecidas por padrão esperam que o total de todas as cotas (exceto a cota de sono diário) sejam iguais a 1. Se esta cota não for igual a 1, será somado o valor total entre elas e considerado a soma igual a 100%.

**EXEMPLO:** Se a soma for 12 + 9 + 3 + 6, o total será 30 e suas cotas serão respectivamente 0.4, 0.3, 0.1 e 0.2, que somadas serão iguais a 1.

<br>
<h2 id="der--health"><b>2.4. Health Informations </b> 🩺</h2>
<br>

A entidade *`Health Informations`* será responsável por armazenar informações relevantes do usuário relacionadas a saúde como peso, altura, IMC e peso ideal. Conforme o que for descrito pelo usuário, cálculos automáticos serão realizados e, se o usuário optar por uma rotina automatizada, esta será criada levando em consideração o que for aqui informado.

<br>
<h2 id="der--finance"><b>2.5. Finance Informations </b> 💵</h2>
<br>

A entidade *`Finance Informations`* será responsável por armazenar informações relevantes do usuário relacionadas a sua vida profissional e financeira como ocupação primária, salário, pretensão salarial e aposentadoria. Conforme o que for descrito pelo usuário, cálculos automáticos serão realizados e, se o usuário optar por uma rotina automatizada, esta será criada levando em consideração os dados financeiros pessoais informados.
