# Computer Vision Analysis Application

A real-time camera application that uses OpenAI's Vision API to analyze images.

## Features
- Live camera feed display
- Real-time image analysis using OpenAI's Vision API
- Simple keyboard controls
- Console output of analysis results

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the application:
```bash
python vision_app.py
```

2. Controls:
- `s` - Capture and analyze the current frame
- `q` - Quit the application

## How It Works

1. The application opens your computer's camera feed
2. A window displays the live video stream
3. When you press 's', the current frame is:
   - Captured from the video feed
   - Sent to OpenAI's Vision API for analysis
   - Analysis results are displayed in the console
4. Press 'q' at any time to close the application

## Requirements
- Python 3.x
- OpenAI API key
- Webcam or camera device