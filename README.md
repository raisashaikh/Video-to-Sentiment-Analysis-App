# Video-to-Sentiment-Analysis-App
This project allows users to upload a video file, extract its audio, transcribe the speech to text with timestamps, and perform sentiment analysis on the transcribed text. The app is built using Streamlit and leverages several libraries for video processing, speech-to-text transcription, and sentiment analysis.

# Features
Upload a video file (.mp4 format).
Extract audio from the uploaded video.
Transcribe speech from the extracted audio using Whisper with timestamps.
Perform sentiment analysis on the transcribed text using NLTK's VADER sentiment analyzer.
Display transcription text and sentiment analysis scores.
Installation
# Clone the repository:
 git clone https://github.com/raisashaikh/Video-to-Sentiment-Analysis-App.git
# Create a virtual environment and activate it (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install the required dependencies:
pip install -r requirements.txt
# Requirements
Python 3.8 or higher
Streamlit
moviepy
whisper-timestamped
nltk
Make sure you have ffmpeg installed for moviepy to work correctly.

# Usage
Run the Streamlit app:
streamlit run app.py
# Upload a video file:
Open the app in your browser (usually at http://localhost:8501).
Upload a video file in .mp4 format.
View results:
After uploading, the app will extract the audio from the video.
It will then transcribe the audio to text with timestamps.
Finally, it will perform sentiment analysis on the transcribed text and display the results.
# File Structure
app.py: The main Streamlit app script.
requirements.txt: A list of all dependencies required for the project.
# Dependencies
streamlit: For building the web app interface.\\
moviepy: For video processing.\\
whisper-timestamped: For speech-to-text transcription with timestamps.\\
nltk: For natural language processing and sentiment analysis.
