# AI_Interface
Local interface for AI

# AI Interface

This project implements a graphical interface in Python that interacts with an AI API to generate responses to user questions. The responses can be exported as text (.txt) or audio (.mp3).

## Features

1. **Generate Response**: By entering a question in the "Input" field and pressing the "Generate Response" button, the application retrieves an AI-generated response.
2. **New Question**: Clears the input and output fields to allow a new question.
3. **Export Text**: Saves the generated response to a `.txt` file.
4. **Export Audio**: Converts the response to audio using the configured voice and saves it as a `.mp3` file.

## Requirements

### Required Libraries

Install the following libraries using `pip`:

```bash
pip install edge-tts==6.1.14 google-generativeai==0.8.3
```

## Configuration
At the beginning of the code, adjust the following variables as needed:

1. **API_KEY**: Enter your Google Generative AI API key.
2. **AI_MODEL**: The AI model to be used (e.g., "gemini-1.5-pro-latest").
3. **VOICE**: The voice for text-to-speech conversion (e.g., "en-US-JennyNeural").
4. **USER_NAME**: Your name, which will appear in the interface.

## Usage
1. Run the `interface.py` script to open the interface.
2. Enter a question in the "Input" field.
3. Press "Generate Response" to get the AI response.
4. Use the buttons to perform additional actions:
   - **New Question**: Clears the fields.
   - **Export Text**: Exports the response to a `.txt` file.
   - **Export Audio**: Exports the response in `.mp3` format.

## Code Structure
- **generate_response**: Generates the AI response for the entered question.
- **new_question**: Clears the input and output fields.
- **export_text**: Saves the response to a `.txt` file with a timestamp.
- **export_audio_async**: Asynchronous function that converts the response to audio and saves it as a `.mp3` file.
- **export_audio**: Wrapper function to call the asynchronous `export_audio_async`.

## Notes
- Ensure you have an internet connection when generating the AI response, as the process depends on the Google API.
- Refer to the official documentation of the libraries used for more information on customizing AI models and voices.

## Libraries
- https://github.com/rany2/edge-tts
- https://github.com/google-gemini/generative-ai-python
