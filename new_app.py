from flask import Flask
import platform
import os
import configs

app = Flask(__name__)
configs.configure_app(app)

if __name__ == "__main__":
    print("Starting applicattion !!")
    print(os.listdir(app.config.get("DATA_DIR")))
    app.run()
    pass
