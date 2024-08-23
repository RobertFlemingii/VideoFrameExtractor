import tkinter as tk
from tkinter import filedialog
import cv2
import os

def select_video_file():
    video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
    if video_path:
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            split_video_to_frames(video_path, output_folder)

def split_video_to_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.png")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

# Set up the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Video to Frames")

    btn_select_video = tk.Button(root, text="Select Video and Output Folder", command=select_video_file)
    btn_select_video.pack(pady=20)

    root.mainloop()
