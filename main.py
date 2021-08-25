from flask import Flask, request, render_template
from predict import predict
import features, commands

import mimetypes
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.json')

app = Flask(__name__)


@app.route("/manifest.json")
@app.route("/sw.js")
@app.route("/logo.png")
def my_static():
	return app.send_static_file(request.path[1:])

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/chat")
def chat():
	return render_template("chat.html")

@app.route("/share")
def share():
	return render_template("share.html")

@app.route("/features")
def features_list():
	return render_template("features/index.html")

@app.route("/features/<feature>")
def feature(feature:str):
	return render_template(f"features/{feature}.html", features=features)

@app.route("/response", methods=["POST"])
def get_response():
	data = request.form
	response = predict(data.get("message"))
	if response is not None:
		if r"{features}" in response:
			response = response.replace(r"{features}", "<br/>".join(features.feature_list))
		if r"{joke}" in response:
			response = response.replace(r"{joke}", commands.get_joke())
		if r"{meme}" in response:
			response = response.replace(r"{meme}", commands.get_meme())
	return response if response else ""


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=2000, debug=True)