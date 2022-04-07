from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO,send, emit
import json
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['EVENTS_PAUSED'] = False
socketio = SocketIO(app)

event_template = """
        <div class="col-md-12">
          <div class="card flex-md-row mb-2 box-shadow">
            <div class="card-body align-items-start">
              <strong class="d-inline-block mb-2 text-uppercase">{}</strong>
              <h3 class="mb-0">
                <a class="text-dark" href="#">{}</a>
              </h3>
              <div class="mb-1 mt-2 text-white badge badge-secondary">{}</div>
              <p class="card-text mt-2">{}</p>
              <a class="btn btn-outline-primary" data-toggle="collapse" href="#{}" role="button" aria-expanded="false" aria-controls="collapseExample">Event Details</a>
              <div class="collapse" id="{}">
                <div class="card card-body mt-3 bg-dark text-white">
                  <pre style="white-space: pre-wrap" class="text-white">{}<pre>
                </div>
              </div>
            </div>
          </div>
        </div>
"""

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/events",methods=["POST"])
def events():
    data = request.get_json()
    id = uuid.uuid4().hex
    event = {"priority":data["event"]["priority"],"rule":data["event"]["rule"],
      "message":event_template.format(
        data["event"]["priority"],data["event"]["rule"],
        data["event"]["time"],data["event"]["output"],
        id,id,json.dumps(data,indent=4)
      )
    }
    if not app.config["EVENTS_PAUSED"]:
        socketio.emit('newEvent', event)
    return jsonify({"message":"ok"})

@socketio.on('pauseUpdates')
def toggle_update(data):
    if data == "1":
        app.config["EVENTS_PAUSED"] = True
    else:
        app.config["EVENTS_PAUSED"] = False

if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0',debug=True)
