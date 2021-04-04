# Ellimecha Bot

Discord Bot para manejar y consultar eventos. Este bot contiene los siguientes comandos:

* Añadir un evento (solo administradores y Rol 'Pomponera':

 ```$elliadd "01-04-2021 22:00" "La culpa es de Laikhas"```

* Ver eventos del día:

```$ellilist```

* Ayuda:

```$ellihelp```

* Canal de Recordatorios (solo administradores y Rol 'Pomponera'):

```$elliautoreminder```

Además, este bot cada 24 horas permite lanzar un mensaje de recordatorio con un @everyone.

Para arrancar este bot necesitaras un token de discord. Para ello consulta la siguiente [documentación](https://www.writebots.com/discord-bot-token/).

Una vez obtenido el token, se debe de crear una variable de entorno llamada ```DISCORD_TOKEN```; para posteriormente llamar al bot.

## Ejecutar el bot e instalar dependencias

Para poder ejecutar el bot para desarrollar para el puede usarse ```pipenv``` y utilizar el fichero pipenv para ejecutarlo.

```pipenv install #instala las dependencias```

```pipenv run runbot # ejecuta el bot```

```pipenv run tests # ejecuta los tests unitarios```

## Crear un contenedor con Docker

Se ha añadido la posibilidad de ejecutar este bot en un contenedor; de tal forma que pueda desplegarse en un servidor de forma sencilla; para ello se ejecutarán los siguientes comandos.

Primero se construye la imagen:

```docker build . --tag ellibot:version```

y se creará un nuevo contenedor:

```docker container run --env DISCORD_TOKEN=<discordtoken> --restart unless-stopped ellibot:version```
