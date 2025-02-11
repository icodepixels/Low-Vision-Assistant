from flask import Flask, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    try:
        # Get image URL from request
        data = request.get_json()
        if not data or 'image_url' not in data:
            return jsonify({'error': 'No image URL provided'}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data['image_url'],
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        return jsonify({
            'description': response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)