<html>
    <body>
        <form id="login-form" name="login-form" action="/login" method="POST">
            Username: <input id="username" class="form-control" name="username" type="text" placeholder="Username"/>
            Password: <input id="password" class="form-control" name="password" type="password" placeholder="Password"/>
            <input id="token" name="token" type="hidden" value="{{ token }}"/>
            <input value="Login" type="submit"/>
        </form>
    </body>
</html>
