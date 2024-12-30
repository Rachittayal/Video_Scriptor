import cv2
import os
import subprocess
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

def extract_images(video_path, output_folder, interval=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Extracting images using FFmpeg...")
    command = [
        'ffmpeg', '-i', video_path, 
        '-vf', f'fps=1/{interval}',
        os.path.join(output_folder, 'frame_%04d.jpg')
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Images extracted and saved to {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting images: {e}")

def generate_captions(frames_folder, model, processor, tokenizer):
    captions = []
    for image_name in sorted(os.listdir(frames_folder)):
        if image_name.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(frames_folder, image_name)
            image = Image.open(image_path)
            inputs = processor(images=image, return_tensors="pt").to("cpu")
            outputs = model.generate(**inputs)
            caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
            captions.append(f"{image_name}: {caption}")
            print(f"Generated caption for {image_name}: {caption}")
    return captions

if __name__ == "__main__":
    # Define paths
    video_path = "data\Forge Upset Forging.mp4"  # Path to your video file
    frames_folder = "data/extracted_images/"  # Folder to save extracted images
    captions_file = "data/transcript.txt"  # File to save captions

    # Step 1: Extract Images
    extract_images(video_path, frames_folder, interval=5)

    # Step 2: Load Pre-trained Model
    model_name = "nlpconnect/vit-gpt2-image-captioning"
    model = VisionEncoderDecoderModel.from_pretrained(model_name)
    processor = ViTImageProcessor.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Step 3: Generate Captions
    captions = generate_captions(frames_folder, model, processor, tokenizer)

    # Step 4: Save Captions to File
    with open(captions_file, "w", encoding="utf-8") as file:
        file.write("\n".join(captions))
    print(f"Captions saved to {captions_file}")
