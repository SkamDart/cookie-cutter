from project import (
    create_app,
    settings
)


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=settings.HTTP_PORT)
