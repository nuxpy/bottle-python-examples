<html>
    <head>
        <title>Mi sitio web con Bottle</title>
    </head>
    <body>
        <h1>Hola mundo</h1>
        <p>Estamos en el sitio de {{ valor }}</p>
        <form id="contacto" method="POST" action="envia_contacto">
            <input type="text" name="mi_contacto" placeholder="Mi contacto"/>
            <input type="submit"/>
        </form>
    </body>
</html>
