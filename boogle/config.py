class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfiguration(Config):
    DEBUG = True


class TestingConfiguration(Config):
    TESTING = True


class ProductionConfiguration(Config):
    pass



app_config = dict(
    dev=DevelopmentConfiguration,
    production=ProductionConfiguration,
    test=TestingConfiguration
)
