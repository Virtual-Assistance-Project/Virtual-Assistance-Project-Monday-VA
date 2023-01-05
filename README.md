# **API Monday - Assistente Virtual**

A proposta deste projeto é a de criar um meio de interação entre um banco de dados e uma aplicação frontend baseada em uma assistente virtual.

## **Sumário**

<ul>
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
        </ul>
      </li>
    </ul>
</ul>

