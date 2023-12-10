import streamlit as st
from pytube import YouTube

def download_best_quality_video(url):
    try:
        # Get YouTube video
        yt = YouTube(url)

        # Get the best quality stream
        best_quality_stream = yt.streams.get_highest_resolution()

        if best_quality_stream:
            # Download the video
            best_quality_stream.download(output_path='downloads', filename=f"{yt.title}.mp4")

            st.success(f"Best quality video downloaded successfully.")
        else:
            st.warning("No video quality found for the video. Try another video.")

    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit app
st.title("YouTube Video Downloader")

# Input for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:")

# Download button
if st.button("Download Video"):
    if video_url:
        download_best_quality_video(video_url)
    else:
        st.warning("Please enter a valid YouTube video URL.")
