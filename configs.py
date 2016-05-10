def configure_app(app):
    import platform
    import os
    print("Loading base configs = ", app.config)
    app.config.from_object(Config)
    if os.getenv("MODE", "PROD") is "PROD":
        print("Loading production configs = ", app.config)
        app.config.from_object(ProductionConfig)
    else:
        if platform.system() is "Windows":
            print("Loading WindowsDev configs = ", app.config)
            app.config.from_object(WindowsDevConfigs)
        else:
            print("Loading Dev configs = ", app.config)
            app.config.from_object(DevConfig)
    print("Final Configs = ", app.config)

class Config(object):
    DEBUG=True
    SECRET_KEY="python and java"
    SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite"
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True


class DevConfig(Config):
    DATA_DIR="/tmp/data"


class WindowsDevConfigs(DevConfig):
    DATA_DIR="C:/temp/data"


class ProductionConfig(Config):
    DEBUG=False
    SECRET_KEY="there is no secrete key"
    DATA_DIR="/tmp/data"
