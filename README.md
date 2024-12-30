# Video Analysis and PPT Generation

This project is designed to analyze videos, extract images and audio, generate captions for the images using a pre-trained model, and create a PowerPoint presentation based on the generated captions and images.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Features
- Extract images from a video at specified intervals.
- Generate captions for the extracted images using a transformer model.
- Create a PowerPoint presentation with the generated captions and images.
- Download the generated PPTX file to a specified location.

## Requirements
To run this project, you need to have the following Python packages installed:

- `openai-whisper`
- `opencv-python`
- `python-pptx`
- `ffmpeg-python`
- `transformers`
- `pillow`

You can install these packages using the `requirements.txt` file provided in the project:
pip install -r requirements.txt


## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that FFmpeg is installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

## Usage
1. Place your video file in the `data` directory. Update the `video_path` variable in `video_analysis.py` to point to your video file.

2. Run the `video_analysis.py` script to extract images and generate captions:
   ```bash
   python video_analysis.py
   ```

3. After running the above script, the captions will be saved in `data/transcript.txt`.

4. Run the `ppt_gen.py` script to create a PowerPoint presentation:
   ```bash
   python ppt_gen.py
   ```

5. The generated PPTX file will be saved in the `output` directory and will also be copied to the specified download folder.

## File Descriptions
- `video_analysis.py`: Script to extract images and generate captions from a video.
- `ppt_gen.py`: Script to create a PowerPoint presentation from the generated captions and images.
- `requirements.txt`: List of required Python packages for the project.
- `data/transcript.txt`: File where the generated captions are saved.
- `data/extracted_images/`: Directory where the extracted images from the video are stored.
- `output/`: Directory where the generated PowerPoint presentation is saved.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

