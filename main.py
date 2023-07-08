# import create_app
from app import create_app


app = create_app()


if __name__ == "__main__":
    app.run(None, 5000, True)