# VideoMergePlus v1
VideoMergePlus: Convert GIFs to MP4s, concatenate clips, and create bulk ads automatically or content for social media.

VideoMergePlus is a powerful Python tool for effortless video processing. It allows you to convert GIFs to MP4s and concatenate video clips, enabling you to quickly create batches of advertisements or engaging social media content.

## Get creative with bulk video merging and advertisement creation using MoviePy.
### Clone the repository.
1. Install the required libraries using pip install -r requirements.txt.
2. Put GIFs in the gif folder
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

```
video_files_in_output = [os.path.join('./output', f) for f in os.listdir('./output') if f.endswith('.mp4')]
```

```
done_folder = './done'
video_processor.concatenate_clips(video_files_in_output, method='compose')
```
