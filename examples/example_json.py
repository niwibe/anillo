from anillo.app import application
from anillo.middlewares.json import json_middleware
from anillo.http import Ok


def index(request):
    return Ok({"echo-response": request.data["echo"]}, mimetype="application/json")


app = application(json_middleware(index))


if __name__ == '__main__':
    from anillo import wsgi
    wsgi.run_simple(app, port=5000)
