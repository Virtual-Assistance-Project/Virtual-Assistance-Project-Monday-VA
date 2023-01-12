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
        <li><a href="#der--isced">2.6.1. Educational Level Choices</a>;</li>
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
          <li><a href="#route--get-schedule">3.2.2. GET schedules/</a>;</li>
          <li><a href="#route--get-schedule_id">3.2.3. GET schedules/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-schedule">3.2.4. PATCH schedules/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-schedule">3.2.5. DELETE schedules/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--quotas">3.3. Daily Quotas</a>:</h3>
        <ul>
          <li><a href="#route--post-quotas">3.3.1. POST quotas/</a>;</li>
          <li><a href="#route--get-quotas">3.3.2. GET quotas/profile/</a>;</li>
          <li><a href="#route--patch-quotas">3.3.3. PATCH quotas/profile/</a>;</li>
          <li><a href="#route--delete-quotas">3.3.4. DELETE quotas/profile/</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--health">3.4. Health Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-schedule">3.4.1. POST infos/health/</a>;</li>
          <li><a href="#route--get-profile-health">3.4.2. GET infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-health">3.4.3. PATCH infos/health/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-health">3.4.4. DELETE infos/health/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--finance">3.5. Finance Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-finance">3.5.1. POST infos/finances/</a>;</li>
          <li><a href="#route--get-profile-finance">3.5.2. GET infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-finance">3.5.3. PATCH infos/finances/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-finance">3.5.4. DELETE infos/finances/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
      <li>
        <h3><a href="#route--academic">3.6. Academic Informations</a>:</h3>
        <ul>
          <li><a href="#route--post-academic">3.6.1. POST infos/academic/</a>;</li>
          <li><a href="#route--get-profile-academic">3.6.2. GET infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--patch-profile-academic">3.6.3. PATCH infos/academic/&ltuuid:pk&gt</a>;</li>
          <li><a href="#route--delete-academic">3.6.4. DELETE infos/academic/&ltuuid:pk&gt</a>;</li>
        </ul>
      </li>
    </ul>
</ul>

<br>

---

<br>
<h1 id="initialization"><b>1. Inicialização do projeto localmente</b></h1>
<br>

Primeiramente deve assegurar-se de que tem a [última versão do python](https://www.python.org/downloads/) instalada em sua máquina, além do [PostgreSQL](https://www.postgresql.org/) se optar por rodar as migrações da API para o database localmente.

Após estas instalações, cheque se o _`pip3`_, o _`python3`_ e o _`postgres`_ foram instalados corretamente:

```powershell
python3 --version   # Python 3.11.0

pip3 --version      # pip 22.3.1 from C:\Python311\[...]\pip

psql --version      # psql (PostgreSQL) 14.5
```

Atualize seu _`pip`_ para evitar possíveis erros durante as instalações de pacotes:

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

**_OPCIONAL_**: Se optou por rodar a aplicação utilizando um database local, certifique-se de ter criado um database para armazenar esta aplicação logando em seu superuser psql:

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

---

<br>
<h1 id="der"><b>2. DER: Diagrama de Entidades e relacionamentos</b></h1>
<br>

O _Diagrama de Entidades e Relacionamentos_ (**DER**) exemplifica em forma de um fluxograma a maneira que as entidades interagem dentro do banco de dados.

<br>

![Monday - Vitual Assistant API Entity Relationship Diagram](./ERD-Monday_VA.svg)

<br>

No caso da **Monday - Assistente Virtual**, temos 6 entidades se relacionando entre si através de uma 7ª chamada _`API_Managements`_, onde concentra todos os dados das demais.
O usuário tem a opção de planejar sua rotina manualmente através da entidade _`Schedules`_ ou, eventualmente, executar análises e oferecer automaticamente opções de rotina conforme as informações fornecidas pelas entidades de _`Infos`_ & _`Daily Quotas`_.

<br>

### Abaixo descreveremos mais detalhadamente a função de cada uma das entidades presentes no diagrama.

<br>

---

<br>
<h2 id="der--user"><b>2.1. Users</b> 👤</h2>
<br>

A entidade _`Users`_, assim como na maioria dos casos, tem como função o cadastro de novos usuários.

Ela contará com um CRUD completo, podendo-se Criar, Listar, Recuperar, Atualizar ou Deletar um usuário, sendo a deleção inicialmente um HARD delete.

Mais adiante, assim como para as outras entidades, detalharemos quais as chaves necessárias para a interação com esse CRUD, bem como seus endpoints e verbos HTTP.

<br>
<h2 id="der--schedules"><b>2.2. Schedules</b> 📒</h2>
<br>

A entidade _`Schedule`_ será a responsável por disponibilizar ao usuário uma forma de adicionar manualmente ao seu calendario novos agendamentos.

Diferentemente das entidades de **Cotas** e **Informações** a interação de _`Schedules`_ num ambito geral ocorrerá de forma totalmente dependente do que o usuário definir.

Esta, como demonstrado no diagrama, oferece a possibilidade de inserir um evento customizado e defini-lo como rotina (ou não).

<br>
<li id="der--type"><b>2.2.1. Type Choices</b> 🔁</li>
<br>

Ainda sobre _`Schedules`_, será fornecido um campo **`type`**, que definirá o tipo de _agendamento_ que desejamos realizar. Para tal, temos 6 tipos diferentes de agendamento, sendo eles:

- `Work`: Para agendamentos relacionados a vida profissional;
- `Sleep`: Para agendamentos relacionados a horários de sono ou de "momentos extras" relacionados a descanso;
- `Study`: Para agendamentos relacionados a sua vida acadêmica;
- `Hobby`: Para agendamentos relacionados a lazer, como encontros, viagens turísticas, jogos e afins;
- `Health`: Para agendamentos relacionados a saúde de modo geral, como visitas a clínicos, terapias, cirurgias e visitas a hospitais;
- `Commitment` (valor padrão): Para agendamentos genéricos que não se encaixam em nenhuma das categorias anteriores;

<br>
<h2 id="der--quotas"><b>2.3. Daily Quotas</b> 📊</h2>
<br>

As _`Daily Quotas`_ oferecerão a possibilidade do usuário definir cotas de atividades que deseja inserir em seu dia-a-dia em forma de porcentagem (um número entre 0 e 1). A API fornecerá opções de cotas para **horas de sono, trabalho, estudos, momentos de lazer e cuidados com a saúde**(como academia, caminhada e meditação por exemplo).

Vale ressaltar que nem todas as cotas serão calculadas da mesma forma. Algumas serão calculadas a partir do dia completo (24h), enquanto outras serão calculadas conforme o tempo restante de seu dia.

**POR EXEMPLO:** O _`horário de sono`_ é uma cota que será calculada a partir de 24h, bem como a soma de todos os agendamentos (_`Schedules`_), enquanto as demais cotas serão calculadas pelo restante do dia útil. Se definirmos a cota diária de sono como _`0.25`_ (25% de 24h, ou seja, 6h) e, além disso, definirmos um total de 4h de rotina, teremos um restante de dia útil igual a **`14 horas`** (24 - 6 - 4 = 10 horas). Essas 14h restantes serão a base da qual será calculada as outras cotas.

Sabendo disso e definindo um exemplo para todas as cotas, teremos um resultado semelhante a seguinte tabela:

<center>

---

|                             | `Cotas` | `Hora Base` | `Cálculo` | `Horas Diárias` | `Restante diário`  |
| :-------------------------: | :-----: | :---------: | :-------: | :-------------: | :----------------: |
|     **`Agendamentos`**      |    -    |     24h     |     -     |       4h        |         -          |
|    **`Horário de Sono`**    |  0.25   |     24h     | 24 x 0.25 |       6h        |         -          |
|      **`Horas Fixas`**      |    -    |     24h     |   4 + 6   |       10h       |     **_14h_**      |
| **`Horário Útil Restante`** |    -    |      -      |  24 - 10  |       14h       |         -          |
|       **`Trabalho`**        |   0.4   |     14h     | 14 x 0.4  |     5h36min     |      8h24min       |
|        **`Estudo`**         |  0.25   |     14h     | 14 x 0.25 |     3h30min     |      4h54min       |
|         **`Lazer`**         |  0.15   |     14h     | 14 x 0.15 |     2h06min     |      2h48min       |
|         **`Saúde`**         |   0.2   |     14h     | 14 \* 0,2 |     2h48min     | **Dia preenchido** |

---

</center>

Vale ressaltar que as cotas fornecidas por padrão esperam que o total de todas as cotas (exceto a cota de sono diário) sejam iguais a 1. Se esta cota não for igual a 1, será somado o valor total entre elas e considerado a soma igual a 100%.

**EXEMPLO:** Se a soma for 12 + 9 + 3 + 6, o total será 30 e suas cotas serão respectivamente 0.4, 0.3, 0.1 e 0.2, que somadas serão iguais a 1.

<br>
<h2 id="der--health"><b>2.4. Health Informations </b> 🩺</h2>
<br>

A entidade _`Health Informations`_ será responsável por armazenar informações relevantes do usuário relacionadas a saúde como peso, altura, IMC e peso ideal. Conforme o que for descrito pelo usuário, cálculos automáticos serão realizados e, se o usuário optar por uma rotina automatizada, esta será criada levando em consideração o que for aqui informado.

<br>
<h2 id="der--finance"><b>2.5. Finance Informations</b> 💵</h2>
<br>

A entidade _`Finance Informations`_ será responsável por armazenar informações relevantes do usuário relacionadas a sua vida profissional e financeira como ocupação primária, salário, pretensão salarial e aposentadoria. Conforme o que for descrito pelo usuário, cálculos automáticos serão realizados e, se o usuário optar por uma rotina automatizada, esta será criada levando em consideração os dados financeiros pessoais informados.

<br>
<h2 id="der--academic"><b>2.6. Academic Informations </b> 🎓</h2>
<br>

A entidade _`Finance Informations`_ será responsável por armazenar informações relevantes do usuário relacionadas a sua vida acadêmica como nível de educação, se você é graduado ou não e a sua graduação principal.

<br>
<li id="der--isced"><b>2.6.1. Educational Level Choices</b> 🔁</li>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dentro de <em>Academic Informations </em> teremos um campo chamado <strong><em>educational_level</em></strong> que oferecerá 10 possibilidades de preenchimento conforme as definições sobre <a href="https://datatopics.worldbank.org/education/wRsc/classification">Classificação Internacional Normalizada da Educação (CINE/ISCED)</a>:

<br>

---

<center>

|                        nome | função                                                                                                                                                                             | descrição                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Not informed`** (Padrão) | Não informado pelo usuário                                                                                                                                                         | ND                                                                                                                                                                                                                                                                                                                                                                                     |
|                **`ISCED0`** | Educação pré-primária                                                                                                                                                              | Destinado a crianças de até quatro anos, privilegia um enfoque holístico orientado a dar apoio inicial ao desenvolvimento cognitivo, físico, socio-emocional infantil, além de familiarizá-la com a instrução organizada fora do contexto familiar.                                                                                                                                    |
|                **`ISCED1`** | Educação primária, ou primeiro estágio da educação básica                                                                                                                          | Destinado a crianças de 5 a 11 anos, caracteriza-se por proporcionar destrezas básicas em leitura, escrita e matemática, além de formar uma base para a compreensão das áreas essenciais do conhecimento E o desenvolvimento pessoal e social dos estudantes.                                                                                                                          |
|                **`ISCED2`** | Educação Secundária Baixa, ou segundo estágio da educação básica                                                                                                                   | Normalmente destinado a adolescentes de 12 a 15 anos, caracteriza-se por aplicar um modelo mais orientado por disciplinas com a finalidade de introduzir conceitos teóricos sobre uma ampla gama de temas. No entanto, em alguns sistemas educativos oferecem desde esse nível programas vocacionais orientados a desenvolver destrezas pessoais para o acesso ao mercado de trabalho. |
|                **`ISCED3`** | Educação Secundária Alta                                                                                                                                                           | Destinado a adolescentes de 15 a 18 anos, caracteriza-se por consolidar a educação secundária com instrução mais diversificada, avançada e especialista, visando a preparação para Educação Superior, ou proporcionando destrezas para à formação profissional de nível médio.                                                                                                         |
|                **`ISCED4`** | Educação Pós-Secundária não superior, ou Pós-Secundária não terciária                                                                                                              | Proporciona aos estudantes dos programas de formação geral outra opção de certificação vocacional não terciária. Por outro lado, os graduados de programas vocacionais de Nível 3 podem optar por melhorar suas especializações, tendo mais oportunidade de acesso ao mercado de trabalho.                                                                                             |
|                **`ISCED5`** | Educação Terciária de Ciclo Curto, ou Primeiro estágio do ensino superior não conducente a uma qualificação avançada na área da investigação (bacharelato, licenciatura, mestrado) | Proporciona conhecimentos e habilidades profissionais, que atendem a ocupações específicas no mercado de trabalho.                                                                                                                                                                                                                                                                     |
|                **`ISCED6`** | Graduação em Educação Terciária, ou Formação superior avançada (pós-graduada), conducente a uma qualificação na área da investigação (doutoramento)                                | Proporciona conhecimentos e habilidades profissionais ou acadêmicas intermediárias (nível médio de complexidade do conteúdo acadêmico). Os programas são essencialmente teóricos, embora possam incluir componentes práticos por estarem embasados em pesquisas que refletem o desenvolvimento da área ou nas melhores práticas profissionais.                                         |
|                **`ISCED7`** | Mestrado, ou Especialização                                                                                                                                                        | Proporciona competências acadêmicas ou profissionais avançadas. Ainda que sejam essencialmente teóricos, podem incluir componentes práticos por estarem embasados em pesquisas que refletem os mais recentes avanços da área.                                                                                                                                                          |
|                **`ISCED8`** | Doutorado ou Pesquisa avançada                                                                                                                                                     | Conduzem o estudante a um título de pesquisa avançada cujas investigações são originais, tanto que costumam ser oferecidos exclusivamente por Instituições de Ensino Superior (IES) dedicadas à pesquisa.                                                                                                                                                                              |

</center>

---

###### Fonte: [Classificação Internacional Normalizada da Educação - WikiPedia](https://pt.wikipedia.org/wiki/Classifica%C3%A7%C3%A3o_Internacional_Normalizada_da_Educa%C3%A7%C3%A3o)

<br>

Conforme o que for descrito pelo usuário, cálculos automáticos serão realizados e, se o usuário optar por uma rotina automatizada, esta será criada levando em consideração os dados acadêmicos informados.

<br>
<h2 id="der--management"><b>2.7. API Management</b> ⚙</h2>
<br>

Por último, mas não menos importante, temos a entidade _`API_Managements`_, responsável por fornecer todas as informações do usuário armazenadas em um só local. Será através desta que toda a lógica de automatização e coleta de dados será estudada, gerando o calendário dos usuários, suas rotinas e compromissos de forma automatizada, ou caso prefira, manual.

> [...] Seção ainda em construção [...]

<br>

<h3>Agora que conhecemos todas as entidades e suas funções, seremos introduzidos as rotas da aplicação.</h3>

<br>

---

<br>
<h1 id="routes"><b>3. Rotas da Aplicação</b></h1>
<br>

Todas as rotas disponíveis na API estão sendo descritas abaixo e podem ser acessada através do comando:

```powershell
python .\manage.py runserver
```

Todas as rotas terão o mesmo padrão de resposta de erro, mudando apenas o código HTTP retornado em cada uma delas:

<br>

- **Corpo de resposta _400_ - Campos obrigatórios não declarados**:

```json
{
  "birthdate": ["This field is required."],
  "first_name": ["This field is required."],
  "last_name": ["This field is required."]
}
```

<br>
 
- **Corpo de resposta *401* - Email ou senha incorretos**:
```json
{
	"detail": "No active account found with the given credentials"
}
```

<br>
 
 
- **Corpo de resposta *401* - Authorization Headers Ausentes**:
```json
{
	"detail": "Authentication credentials were not provided."
}
```

<br>
  
- **Corpo de resposta *400* - Token Inválido**:
```json
{
	"detail": "Given token not valid for any token type",
	"code": "token_not_valid",
	"messages": [
		{
			"token_class": "AccessToken",
			"token_type": "access",
			"message": "Token is invalid or expired"
		}
	]
}
```

<br>
 
 
- **Corpo de resposta *403* - Ação não permitida para usuários não administradores**:
```json
{
	"detail": "You do not have permission to perform this action."
}
```

<br>
 
- **Corpo de resposta *404* - Resultado não encontrado**:
```json
{
	"detail": "Not found."
}
```

<br>

---

<br>
<h2 id="route--users"><b>3.1. Users</b></h2>
<br>

Esta rota fornece ao usuário da API um CRUD completo de cadastro, leitura, atualização e deleção de novas contas. Vale ressaltar que a deleção feita será um _`Hard Delete`_ onde todas as informações não serão persistidas no database.

Visando a segurança das informações do usuário da aplicação, a rota `User` é a única em toda a aplicação que compartilhará os dados dos usuários com admninistradores, sendo esses apenas dados básicos como nome de usuário, email e data de aniversário. Nenhum administrador da API terá acesso nem mesmo ao hash da senha dos usuários. Estes apenas poderão administrar atualizações e deleções de perfil conforme torne-se necessário.

<br>

---

<br>
<h3 id="route--post-users"><b>3.1.1. POST users/</b></h3>
<br>

Esta rota será responsável pelo cadastro de novos usuários na aplicação. É esperado um corpo de requisição e não é necessário um token de autorização.

#### **Corpo de requisição**:

```json
{
  "username": "Usuário",
  "email": "usuario@teste.com",
  "password": "1234Teste",
  "birthdate": "1990-01-01",
  "first_name": "Usuário",
  "last_name": "Teste"
}
```

#### **Corpo de resposta**:

```json
{
  "id": "1d19f739-8e13-4e08-b0c2-d5294db15ceb",
  "username": "Usuário",
  "email": "usuario@teste.com",
  "birthdate": "1990-01-01",
  "first_name": "Usuário",
  "last_name": "Teste"
}
```

<br>

---

<br>
<h3 id="route--get-users"><b>3.1.2. GET users/</b></h3>
<br>

Rota responsável pela listagem de todos os usuários. Apenas usuários administradores podem ter acesso a esta rota.

Se o token estiver correto e o usuário for identificado como um administrador, teremos uma resposta semelhante a esta:

#### **Corpo de resposta**:

```json
[
  {
    "id": "362ea31c-1856-4c86-a5c0-3330565df55d",
    "username": "admin",
    "email": "admin@admi.n",
    "birthdate": "1970-01-01",
    "first_name": "admin",
    "last_name": "admin"
  },
  {
    "id": "1d19f739-8e13-4e08-b0c2-d5294db15ceb",
    "username": "usuario",
    "email": "usuario@teste.com",
    "birthdate": "1990-01-01",
    "first_name": "Usuário",
    "last_name": "Teste"
  }
]
```

<br>

---

<br>
<h3 id="route--get-profile"><b>3.1.3. GET users/&ltuuid:pk&gt</b></h3>
<br>

Listagem de um único perfil de usuário. A rota apenas pode ser acessada pelo usuário dono da conta ou pelo administrador.

Se o token estiver correto, teremos uma resposta semelhante a esta:

#### **Corpo de resposta**:

```json
{
  "id": "1d19f739-8e13-4e08-b0c2-d5294db15ceb",
  "username": "Usuário",
  "email": "usuario@teste.com",
  "birthdate": "1990-01-01",
  "first_name": "Usuário",
  "last_name": "Teste"
}
```

<br>

---

<br>
<h3 id="route--patch-profile"><b>3.1.4. PATCH users/&ltuuid:pk&gt</b></h3>
<br>

Rota responsável pela atualização dos usuários. A rota recebe um corpo de requisição com todas as chaves declaradas na criação do usuário podendo ser editadas, total ou parcialmente. Apenas pode ser acessada pelo usuário dono da conta ou pelo administrador.

#### **Corpo de requisição**:

```json
{
  "username": "Usuário MODIFICADO"
}
```

Se o token estiver correto e os campos da requisição forem reconhecidos, teremos uma resposta semelhante a esta:

#### **Corpo de resposta**:

```json
{
  "id": "1d19f739-8e13-4e08-b0c2-d5294db15ceb",
  "username": "Usuário MODIFICADO",
  "email": "usuario@teste.com",
  "birthdate": "1990-01-01",
  "first_name": "Usuário",
  "last_name": "Teste"
}
```

<br>

---

<br>
<h3 id="route--delete-profile"><b>3.1.5. DELETE users/&ltuuid:pk&gt</b></h3>
<br>

Rota responsável pela deleção de um usuário. Será feito um `hard delete` no banco de dados, portando não persistirá os dados do usuário caso a requisição seja feita com sucesso.

Se o token estiver correto, um **_204 NO CONTENT_** será retornado pela rota.

<br>

---

<br>
<h2 id="route--schedules"><b>3.2. Schedules</b></h2>
<br>

Esta rota fornece ao usuário logado da API um CRUD completo de criação, leitura, atualização e deleção de novos agendamentos.

<br>

\_\_

<br>
<h3 id="route--post-schedules"><b>3.2.1. POST schedule/ </b></h3>
<br>

Esta rota será responsável pela criação de novos agendamentos pelo usuário logado. É esperado um corpo de requisição e necessário um token de autorização.

#### **Corpo de requisição**:

```json
{
  "title": "Estudar Next.js",
  "type": "STUDY",
  "begans_at": "13:00",
  "ends_at": "15:00",
  "routine_weekdays": "seg-sex",
  "description": "estudar Next em uma semana"
}
```

<br>

\_\_

<br>
<h3 id="route--get-schedule"><b>3.2.2. GET schedule/ </b></h3>
<br>

Essa rota será responsável pela listagem dos agendamentos cadastrados por um usuário. É esperado um token de autorização e somente o próprio usuário que criou conseguirá listar seus agendamentos

#### **Retorno esperado**:

```json
[
  {
    "id": "d3972966-7fd1-40d6-96c0-bd0a7ee10920",
    "title": "Estudar Next.js",
    "type": "STUDY",
    "begans_at": "13:00:00",
    "ends_at": "15:00:00",
    "routine_weekdays": "seg-sex",
    "description": "estudar Next em uma semana"
  },
  {
    "id": "c5e6ee8b-3c29-4dda-8e2d-de811f0be9a4",
    "title": "Estudar Django",
    "type": "STUDY",
    "begans_at": "15:20:00",
    "ends_at": "16:30:00",
    "routine_weekdays": "seg-sex",
    "description": "estudar django"
  }
]
```

<br>

\_\_

<br>
<h3 id="route--get-schedule_id"><b>3.2.3. GET schedule/&ltuuid:pk&gt</b></h3>
<br>

Essa rota será responsável pela listagem de um único agendamento. É esperado um token de autorização e somente o próprio usuário que criou conseguirá listar seu agendamento

#### **Retorno esperado**:

```json
{
  "id": "c5e6ee8b-3c29-4dda-8e2d-de811f0be9a4",
  "title": "Estudar Django",
  "type": "STUDY",
  "begans_at": "15:20:00",
  "ends_at": "16:30:00",
  "routine_weekdays": "seg-sex",
  "description": "estudar django"
}
```

<br>

\_\_

<br>
<h3 id="route--patch-schedule"><b>3.2.4. PATCH schedule/&ltuuid:pk&gt</b></h3>
<br>

Rota responsável pela atualização dos agendamentos. A rota recebe um corpo de requisição com todas as chaves declaradas na criação do agendamento podendo ser editadas, total ou parcialmente.

#### **Corpo de requisição**:

```json
{
  "ends_at": "17:10"
}
```

#### **Retorno esperado**:

```json
{
  "id": "c5e6ee8b-3c29-4dda-8e2d-de811f0be9a4",
  "title": "Estudar Django",
  "type": "STUDY",
  "begans_at": "15:20:00",
  "ends_at": "17:10:00",
  "routine_weekdays": "seg-sex",
  "description": "estudar django"
}
```

<br>

\_\_

<br>
<h3 id="route--delete-schedule"><b>3.2.5. DELETE schedule/&ltuuid:pk&gt</b></h3>
<br>

Rota responsável pela deleção de um agendamento.
Um 204 NO CONTENT será retornado pela rota

<br>

---

<br>
<h2 id="route--quotas"><b>3.3. Quotas</b></h2>
<br>

Esta rota fornece ao usuário logado da API um CRUD completo de criação, leitura, atualização e deleção de novos quotas.

<br>

\_\_

<br>
<h3 id="route--post-quotas"><b>3.3.1. POST quotas/</b></h3>
<br>

Essa rota será responsável em receber as horas geradas pelos agendamentos. É esperado um corpo de requisição e necessário um token de autorização.

#### **Corpo de requisição**:

```json
{
  "work": 8,
  "sleep": 8,
  "study": 2,
  "hobby": 1
}
```

#### **Retorno esperado**:

```json
{
  "id": "da9995a6-738f-40ea-b145-ad6906a6a58f",
  "work": 0.421,
  "sleep": 0.421,
  "study": 0.105,
  "hobby": 0.053,
  "health": 0.0
}
```

<br>

\_\_

<br>
<h3 id="route--get-quotas"><b>3.3.2. GET quotas/profile/</b></h3>
<br>

Essa rota retornará as quotas salvas pelo usuário.

#### **Retorno esperado**:

```json
{
  "id": "da9995a6-738f-40ea-b145-ad6906a6a58f",
  "work": 0.421,
  "sleep": 0.421,
  "study": 0.105,
  "hobby": 0.053,
  "health": 0.0
}
```

<br>
<h3 id="route--patch-quotas"><b>3.3.3. PATCH quotas/&ltuuid:pk&gt</b></h3>
<br>

<br>
<h3 id="route--delete-quotas"><b>3.3.4. DELETE quotas/&ltuuid:pk&gt</b></h3>
<br>

Rota responsável pela deleção de uma quota.
Um 204 NO CONTENT será retornado pela rota

<br>

---
