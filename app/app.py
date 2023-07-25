import os
from flask import Flask
from apis import api

app = Flask(__name__)
app.url_map.strict_slashes = False # remove appended / to routes
api.init_app(app)

if __name__ == "__main__":
  port = os.environ['API_PORT']
  host = "localhost"
  app.run(debug=True, host="0.0.0.0", port=port)
