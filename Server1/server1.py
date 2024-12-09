from flask import Flask, request, jsonify


import  util

app = Flask(__name__)
@app.route("/Classify_image", methods = ['GET', 'POST'])
def Classify_image():
    image_data = request.form('image_data')
    response = jsonify(util.Classify_image(image_data))
    response.header.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    print("load Server")
    util.load_saved_artifacts()
    app.run(port = 5000)
