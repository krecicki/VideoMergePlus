# Cody Krecicki's Choice Internet Brands 🚀
# Creator of Awesome Python Project 🐍
# https://github.com/krecicki
# https://twitter.com/krecicki

import os
import subprocess
import random
import string
from moviepy.editor import VideoFileClip, concatenate_videoclips


class VideoProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.call_clip_path = 'call.mp4'

    def convert_gif_to_mp4(self):
        os.makedirs(self.output_folder, exist_ok=True)

        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(".gif"):
                input_file = os.path.join(self.input_folder, filename)
                output_file = os.path.join(self.output_folder, os.path.splitext(filename)[0] + ".mp4")
                ffmpeg_cmd = f"ffmpeg -i {input_file} -vf \"scale=1280:720\" -y {output_file}"

                try:
                    subprocess.run(ffmpeg_cmd, shell=True, check=True)
                    print(f"Converted {input_file} to {output_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to convert {input_file}: {e}")

    def concatenate_clips(self, video_clip_paths, method="compose"):
        os.makedirs(self.output_folder, exist_ok=True)
        done_folder = './done'  # New folder for the final concatenated videos
        os.makedirs(done_folder, exist_ok=True)  # Create the 'done' folder if it doesn't exist

        if not os.path.isfile(self.call_clip_path):
            raise FileNotFoundError("The 'call.mp4' file is missing.")
        call_clip = VideoFileClip(self.call_clip_path)

        for clip_path in video_clip_paths:
            clip = VideoFileClip(clip_path)

            if clip.duration > 0:
                final_clip = concatenate_videoclips([clip, call_clip], method=method)
            else:
                final_clip = clip

            random_filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            output_path = os.path.join(done_folder, f"{random_filename}.mp4")  # Save in 'done' folder

            final_clip.write_videofile(output_path, codec='libx264')

            clip.close()
            final_clip.close()

        call_clip.close()


if __name__ == "__main__":
    input_folder = "./gif"
    output_folder = "./output"

    video_processor = VideoProcessor(input_folder, output_folder)

    # Convert GIFs to MP4s
    video_processor.convert_gif_to_mp4()

    # Get the list of video files in the "./output" folder
    video_files_in_output = [os.path.join('./output', f) for f in os.listdir('./output') if f.endswith('.mp4')]

    # Concatenate videos with the 'compose' method and save them in "./done" folder
    done_folder = './done'
    video_processor.concatenate_clips(video_files_in_output, method='compose')
