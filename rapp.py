import streamlit as st
from moviepy.editor import VideoFileClip
import whisper_timestamped as whisper
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def speech_to_text_with_timestamps(audio_path, language="en"):
    audio = whisper.load_audio(audio_path)
    model = whisper.load_model("medium", device="cpu")
    result = whisper.transcribe(model, audio, language=language)
    return result

def create_text_from_transcription(transcription_data):
    # Example of handling different formats
    print(transcription_data)

    if isinstance(transcription_data, dict):
        # Check if transcription_data has a 'transcript' key
        if "transcript" in transcription_data:
            return " ".join([item["word"] for item in transcription_data["transcript"]])

        # Check if transcription_data has a 'text' key and 'segments' key
        elif "text" in transcription_data and "segments" in transcription_data:
            # Extract words from the segments
            return " ".join([word["text"] for segment in transcription_data["segments"] for word in segment["words"]])

    elif isinstance(transcription_data, list):
        return " ".join([item for item in transcription_data])

    else:
        return "Error: Unexpected transcription data format"

def sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

st.title("Video to Sentiment Analysis App")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    audio_path = "extracted_audio.wav"
    extract_audio(video_path, audio_path)
    st.success("Audio extracted from video.")

    transcription_result = speech_to_text_with_timestamps(audio_path)
    st.success("Transcription completed.")

    transcription_text = create_text_from_transcription(transcription_result)
    st.text_area("Transcription Text", transcription_text, height=200)

    sentiment_scores = sentiment_analysis(transcription_text)
    st.write("Sentiment Analysis Scores", sentiment_scores)
