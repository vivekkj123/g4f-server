from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

# Initialize the g4f settings as needed
g4f.debug.logging = True
g4f.check_version = False
print(g4f.version)

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        # Retrieve data from the request
        data = request.get_json()

        # Extract messages from the JSON data
        messages = data.get('messages', [])
        # Use the messages to generate a response
        # response = g4f.ChatCompletion.create(
        #   model="gpt-3.5-turbo",
        #    messages=messages,
        #    stream=True,
        # )
        response = g4f.ChatCompletion.create(
	model=g4f.models.gpt_4,
	messages=messages,
	)
        response_messages = response

        return jsonify({"response": response_messages})

if __name__ == '__main__':
    app.run(debug=True)

