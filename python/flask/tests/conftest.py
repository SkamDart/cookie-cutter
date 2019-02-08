from project import (
    create_app,
    settings
)


@pytest.fixtures(scope='session')
def app():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='session')
def client(app):
    yield app.test_client()
