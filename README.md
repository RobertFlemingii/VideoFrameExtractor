# Video to Frames Extractor

## Overview

This Python application allows users to extract frames from a video file and save them as individual image files. The application uses a graphical user interface (GUI) built with Tkinter for ease of use and OpenCV for video processing.

## Features

- **Select Video File**: Choose a video file in formats such as MP4, AVI, MOV, or MKV.
- **Select Output Folder**: Specify a folder where the extracted frames will be saved.
- **Frame Extraction**: Each frame is saved as a PNG file in the selected output folder.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages using pip:
   ```bash
   pip install opencv-python-headless
   ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Select Video and Output Folder**:

   - Click the "Select Video and Output Folder" button.
   - Choose the video file you want to process.
   - Select the folder where you want the frames to be saved.

3. **Processing**:
   - The application will extract each frame from the video and save it as a PNG file in the selected folder.
   - A message will appear in the console indicating the number of frames extracted and the output location.

## Troubleshooting

- **Error: Unable to open video file**:
  - Ensure the video file path is correct and the file is not corrupted.
- **Error: Output folder creation failed**:
  - Check permissions and ensure the folder path is valid.
