from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        input_array = data.get('data', [])

        # Personal details from the example
        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        # Initialize lists and variables
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alpha_chars_for_concat = []

        # Process the input array
        for item in input_array:
            if item.isalpha():
                alphabets.append(item.upper())
                alpha_chars_for_concat.append(item)
            else:
                try:
                    num = int(item)
                    if num % 2 == 0:
                        even_numbers.append(str(num))
                    else:
                        odd_numbers.append(str(num))
                    total_sum += num
                except ValueError:
                    special_characters.append(item)
        
        # Logic for the concatenated string
        reversed_alpha_str = "".join(alpha_chars_for_concat)[::-1]
        concat_string = "".join([
            char.upper() if i % 2 == 0 else char.lower()
            for i, char in enumerate(reversed_alpha_str)
        ])

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        return jsonify(response), 200

    except Exception as e:
        # Graceful error handling
        return jsonify({
            "is_success": False,
            "user_id": "john_doe_17091999", # Return user_id even on error
            "error_message": str(e)
        }), 400
