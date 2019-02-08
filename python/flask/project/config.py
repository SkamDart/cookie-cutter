import os


env = os.environ.get('ENV', 'prod')

class BaseConfig:
    DEBUG = False
    ENV = env
    SHOULD_ALERT = False


class DevConfig(BaseConfig):
    pass

class ProdConfig(BaseConfig):
    SHOULD_ALERT = True


class SandboxConfig(BaseConfig):
    SHOULD_ALERT = True


class StageConfig(BaseConfig):
    SHOULD_ALERT = True


class TestConfig(BaseConfig):
    pass


configs = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'sandbox': SandboxConfig,
    'stage': StageConfig,
    'test': TestConfig
}


settings = configs[env]


def configure_app(app, environment=None):
    """Creates flask app."""
    config_name = environment if environment else os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(configs[config_name])
    app.jinja_env.cache = {}

    app.logger.setLevel(app.config['LOGGING_LEVEL'])
    handler = logging.StreamHandler()
    handler.setFormatter(app.config['LOGGING_FORMAT'])
    app.logger.addHandler(handler)
