import requests
from flask import Flask, jsonify, request
import config

app = Flask(__name__)


@app.route("/items")
def repeat_items():
    """
    Repeats the response from the local data API.

    Returns:
        Response: A JSON response containing the repeated data, or an error response.
    """
    try:
        count = request.args.get("count")  # Get count parameter (may be None)
        if count is not None:
            count = int(count)
            if count <= 0:
                return jsonify({"error": "Count must be a positive integer."}), 400

        # Construct the URL for the local data API
        api_url = f"http://localhost:{config.DATA_SERVER_PORT}/items"
        if count is not None:
            api_url += f"?count={count}"

        # Make the request to the local data API
        api_response = requests.get(api_url)
        api_response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Return the response from the local API as is
        return jsonify(api_response.json()), api_response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the data API: {e}")
        return jsonify({"error": "Error communicating with the data API."}), 500
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid count parameter."}), 400


def serve():
    app.run(debug=False, host="0.0.0.0", port=config.DATA_REPEATER_PORT1)


if __name__ == "__main__":
    serve()
