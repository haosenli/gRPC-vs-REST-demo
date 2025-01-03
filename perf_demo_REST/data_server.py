from flask import Flask, jsonify, request
import data_provider
import config

app = Flask(__name__)


@app.route("/items")
def get_items_rest():
    """
    Retrieves a list of items based on the 'count' query parameter.

    Returns:
        Response: A JSON response containing the retrieved items.
                  Returns a 400 error if 'count' is invalid.
    """
    try:
        count = int(request.args.get("count"))  # Get 'count' from query parameters
        if count <= 0:
            return jsonify({"error": "Count must be a positive integer."}), 400
    except (
        ValueError,
        TypeError,
    ):  # Handle cases where 'count' is not an integer or is missing
        return (
            jsonify(
                {
                    "error": "Invalid or missing 'count' parameter. Please provide a positive integer."
                }
            ),
            400,
        )

    response = data_provider.get_items(count)  # Pass count to data_provider
    print("Returning data from data server")
    return jsonify({"data": response})


def serve():
    app.run(debug=False, host="0.0.0.0", port=config.DATA_SERVER_PORT)


if __name__ == "__main__":
    serve()
