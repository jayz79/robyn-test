from robyn import Robyn, Request, Response
from urllib.parse import parse_qs

app = Robyn(__file__)


@app.get("/")
def home(request: Request) -> Response:
    """
    Display the home page of the web application.
    Args:
        request (Request): The HTTP request object.
    Returns:
        Response: The HTTP response object containing the home page HTML.
    """
    html = "<h1>Welcome to Capital Music!</h1>"
    response = Response(status_code=200, headers={"Content-Type": "text/html"}, description=html)
    return response


@app.get("/login")
def login_page(request: Request) -> Response:
    """
    Display the login page of the web application.
    Args:
        request (Request): The HTTP request object.
    Returns:
        Response: The HTTP response object containing the login page HTML.
    """
    html = "<h1>Login Page</h1><form action='/login' method='post'><input type='text' name='username' placeholder='Username'><br><input type='password' name='password' placeholder='Password'><br><input type='submit' value='Login'></form>"
    response = Response(status_code=200, headers={"Content-Type": "text/html"}, description=html)
    return response


@app.post("/login")
def do_login(request: Request) -> Response:
    """
    Handle the login functionality of the web application.
    Args:
        request (Request): The HTTP request object.
    Returns:
        Response: The HTTP response object based on the login outcome.
    """
    query_params = parse_qs(request.body, max_num_fields=2)

    username = query_params['username'][0]
    password = query_params['password'][0]

    if username == "admin" and password == "password":
        print("Access granted")
        # Handle access granted case here
    else:
        html = "<h1>Invalid username or password</h1>"
        return Response(status_code=200, headers={"Content-Type": "text/html"}, description=html)


@app.get("/dashboard")
def dashboard(request: Request) -> Response:
    """
    Display the dashboard page of the web application.
    Args:
        request (Request): The HTTP request object.
    Returns:
        Response: The HTTP response object containing the dashboard page HTML.
    """
    html = "<h1>Dashboard</h1><p>This could be a dashboard after login or something!</p>"
    response = Response(status_code=200, headers={"Content-Type": "text/html"}, description=html)
    return response


if __name__ == "__main__":
    app.start("127.0.0.1", 8080)
