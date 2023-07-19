# VideoMergePlus v1
VideoMergePlus is a powerful Python tool for effortless video processing. It allows you to convert GIFs to MP4s and concatenate video clips, enabling you to quickly create batches of advertisements or engaging social media content.

## Get creative with bulk video merging and advertisement creation using MoviePy.
### Clone the repository.
0. We recommend using conda and installing it via pip install conda then running conda create --name videomergeplus and then typing conda activate videomergeplus
1. Install the required libraries using pip install -r requirements.txt.
2. Put GIFs in a folder you make called gif, also make these folders too: done, output
3. Run the Python script using python video_merge_plus.py.
4. Ensure 'call.mp4' is present in the working directory to be added at the end of each video during concatenation.
5. Explore the possibilities and streamline your video editing with VideoMergePlus!

## Usage

1. Convert GIFs to MP4s:
   ```python
   input_folder = "./gif"
   output_folder = "./output"

   video_processor = VideoProcessor(input_folder, output_folder)
   video_processor.convert_gif_to_mp4()

## Concatenate GIF & Video Clips
You can change the resoltuion of the GIFs to your end video resolution. Check your files info for correct sizes to avoid the first clip being a different size than  the second. Everything else is automatic. 

```
ffmpeg_cmd = f"ffmpeg -i {input_file} -vf \"scale=1280:720\" -y {output_file}"
```

You can read more about all the supported codec here https://ffmpeg.org/ffmpeg-codecs.html

## File tree example
1. 📦admaker
2. ┣ 📂done
3.   ┣ 📂gif
4.   ┣ 📂output
5.   ┃ ┗ 📜.DS_Store
6. ┣ 📜.DS_Store
7. ┣ 📜app.py
8. ┣ 📜call.mp4
9. ┗ 📜requirements.txt

