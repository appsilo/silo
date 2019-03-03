from Silo.App import App
from routes import routes

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, App(routes, __file__), use_debugger=True, use_reloader=True)
