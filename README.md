## Simple Data Processing Flask API
This is a simple REST API built with Python and Flask that processes an array of data. It sorts the items into even numbers, odd numbers, and alphabets, and returns a structured JSON response.

## How to Use
To use the API, you need to send a POST request to the /bfhl endpoint with a JSON payload.

Endpoint: `/bfhl`

Method: `POST`

Headers: `Content-Type: application/json`

### Request Body
The request body must be a JSON object containing a single key, "data", which holds an array of strings.

Example Request Payload:

```json

{
    "data": ["a", "1", "334", "4", "R", "$"]
}
```

### Responses
✅ Success Response (Status 200)
If the request is successful, the API will return a JSON object with the processed data.

Example Success Response:

```json

{
    "is_success": true,
    "user_id": "john_doe_17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123",
    "odd_numbers": ["1"],
    "even_numbers": ["334", "4"],
    "alphabets": ["A", "R"],
    "special_characters": ["$"],
    "sum": "339",
    "concat_string": "Ra"
}
```

❌ Error Response (Status 400)
If the request payload is missing the "data" key or is malformed, the API will return an error.

Example Error Response:

```json

{
    "is_success": false,
    "user_id": "john_doe_17091999",
    "error_message": "JSON payload is missing or the 'data' key is not found."
}
```
## Testing with cURL
You can easily test the live endpoint using a command-line tool like cURL. Replace https://your-api-url.com with the actual URL provided by your hosting provider (like Vercel).

```bash

curl -X POST https://your-api-url.com/bfhl \
-H "Content-Type: application/json" \
-d '{
    "data": ["a", "1", "334", "4", "R", "$"]
}'

```
