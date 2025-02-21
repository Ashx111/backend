from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID  = "ashirvad_singh_29122004" # Replace with your actual user_id, e.g., "john_doe_17091999"
EMAIL_ID  = "22bai71191@cuchd.in" # Replace with your actual college email ID, e.g., "john@xyz.com"
COLLEGE_ROLL_NUMBER = "22BAI71191"  # Replace with your actual college roll number, e.g., "ABCD123"

def process_data(data_list):
    """
    Processes the input data list to separate numbers and alphabets,
    and find the highest alphabet.
    """
    numbers = []
    alphabets = []
    highest_alphabet = []

    if not isinstance(data_list, list):
        return False, numbers, alphabets, highest_alphabet, "Invalid input data format. 'data' must be a list."

    if not data_list:
        return True, numbers, alphabets, highest_alphabet, None

    valid_alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for item in data_list:
        if isinstance(item, str):
            if item.isdigit():
                numbers.append(item)
            elif len(item) == 1 and item in valid_alphabets:
                alphabets.append(item)

    if alphabets:
        highest_alpha = max(alphabets, key=str.upper) # Find highest alphabet case-insensitive
        highest_alphabet = [highest_alpha]

    return True, numbers, alphabets, highest_alphabet, None


@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl_endpoint():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data or 'data' not in data:
                return jsonify({"is_success": False, "error": "Missing 'data' in request body"}), 400

            input_data_list = data.get('data')
            is_success, numbers, alphabets, highest_alphabet, error_message = process_data(input_data_list)

            if not is_success:
                return jsonify({"is_success": False, "error": error_message}), 400

            response_data = {
                "is_success": is_success,
                "user_id": USER_ID,
                "email": EMAIL_ID,
                "roll_number": COLLEGE_ROLL_NUMBER,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return jsonify(response_data), 200

        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)}), 500  # Internal Server Error

    elif request.method == 'GET':
        response_data_get = {
            "operation_code": 1
        }
        return jsonify(response_data_get), 200

    else:
        return jsonify({"is_success": False, "error": "Method not allowed"}), 405 # Method Not Allowed


if __name__ == '__main__':
    app.run(debug=False, port=8000) # Set debug=False for production and choose a port if needed