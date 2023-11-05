from pytube.cli import on_progress
import customtkinter as ctk
from pytube import YouTube
import os 

# main window settings
window = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
window.title("Youtube Mp3 Downloader")

# window size settings
window.geometry("500x550+650+200")
window.minsize(500,550)

# creating responsive frame
content_frame = ctk.CTkFrame(window)
content_frame.pack(fill=ctk.BOTH, expand=True, pady="5p",padx="5p")

# youtube logo label
youtube_label = ctk.CTkLabel(content_frame, text="YouTube", text_color="red",font=("Roboto",50,"bold"), fg_color=("#ebe6e6","black"), corner_radius=10)
youtube_label.pack(pady=(40,0))

# label & entry widgets for video url
url_label = ctk.CTkLabel(content_frame, text="Enter Youtube Url:", font=("Roboto",15))
url_entry = ctk.CTkEntry(content_frame, width=300, height=40, placeholder_text="Paste Link Here")
url_label.pack(pady=(40,5))
url_entry.pack()

# file_formats combo box
file_formats = [".mp3",".flac",".mp4","wav","wma"]
file_format_combobox = ctk.CTkComboBox(content_frame, values=file_formats)
file_format_combobox.pack(pady=(10,5))
file_format_combobox.set(".mp3") # Default value

# function to download video
def download_video():
    url = url_entry.get()
    file_format = file_format_combobox.get()
    
    # show progress when clicked to the button
    progress_label.pack(pady=(10,5))
    progress_bar.pack(pady=(10,5))
    status_label.pack(pady=(10,5))
    
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        
        # downloading the audio 
        audio_stream = yt.streams.filter(only_audio=True).first()
        out_file = audio_stream.download(output_path="downloads",filename_prefix="Mp3 Downloader by Omer - ")
        
        # saving the audio
        base, ext = os.path.splitext(out_file) 
        new_file = base + file_format
        os.rename(out_file, new_file)
        
        status_label.configure(text="Done!")
        
        
    # handling errors
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color ="white", fg_color ="red")

# download button
download_button = ctk.CTkButton(content_frame, text=f"Download",command=download_video, height=30)
download_button.pack(pady=(10,40))

# function for progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    progress_label.configure(text= str(int(percentage_completed))+"%")
    progress_label.update()
    progress_bar.set(float(percentage_completed / 100))

# progress bar
progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=290)
progress_bar.set(0.0)

# status label
status_label = ctk.CTkLabel(content_frame, text="Loading...")


# run
window.mainloop()
