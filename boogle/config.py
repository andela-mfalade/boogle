class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfiguration(Config):
    DEBUG = True


class TestingConfiguration(Config):
    TESTING = True


class ProductionConfiguration(config):
    pass



app_config = dict(
    dev=DevelopmentConfiguration,
    testing=TestingConfiguration,
    production=ProductionConfiguration
)
