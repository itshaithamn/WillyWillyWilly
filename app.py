from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes [[2]]


@app.route('/data', methods=['POST'])  # Change the route to accept POST requests
def data():
    # Parse the incoming JSON data
    json_data = request.get_json()  # Use get_json() to retrieve JSON payload [[9]]

    if json_data is None:
        # If no JSON data is received, return an error response
        return jsonify({"error": "No JSON data received"}), 400

    # Print the received JSON data to the console
    print("Received JSON data:", json_data)

    # Return a success response with the received data
    return jsonify({"message": "JSON data received successfully", "data": json_data}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)