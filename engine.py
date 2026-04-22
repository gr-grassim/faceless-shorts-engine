import os
import pandas as pd
import textwrap
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def create_text_overlay(text, video_size, font_path):
    """
    Generates a transparent PNG overlay with dynamically centered and wrapped text.
    Includes a semi-transparent bounding box to ensure text readability against dynamic backgrounds.
    """
    img = Image.new('RGBA', video_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 60)
    except IOError:
        print("Warning: Custom font not found. Falling back to default system font.")
        font = ImageFont.load_default()

    # Apply text wrapping for 9:16 vertical aspect ratio
    wrapped_text = textwrap.fill(text, width=25)
    
    # Calculate bounding box for absolute centering
    bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (video_size[0] - w) / 2
    y = (video_size[1] - h) / 2

    # Render contrast box (RGBA: Black with 180 opacity)
    padding = 40
    draw.rectangle([x - padding, y - padding, x + w + padding, y + h + padding], fill=(0, 0, 0, 180))
    
    # Render text
    draw.text((x, y), wrapped_text, font=font, fill="white", align="center")
    
    overlay_path = "temp_overlay.png"
    img.save(overlay_path)
    return overlay_path

def generate_video(content_id, text):
    """
    Orchestrates the video rendering pipeline.
    Composites the dynamically generated text overlay onto the base background video.
    """
    print(f"Processing Video #{content_id}...")
    
    # Initialize background video and normalize duration
    bg_clip = VideoFileClip("assets/background.mp4").subclip(0, 5)
    
    # Generate and initialize the text overlay layer
    overlay_path = create_text_overlay(text, bg_clip.size, "assets/font.ttf")
    text_clip = ImageClip(overlay_path).set_duration(bg_clip.duration)
    
    # Execute composite render
    final_video = CompositeVideoClip([bg_clip, text_clip])
    
    # Export output pipeline
    output_filename = f"outputs/short_{content_id}.mp4"
    final_video.write_videofile(output_filename, fps=24, codec="libx264", audio=False, verbose=False, logger=None)
    
    # Post-render cleanup
    os.remove(overlay_path)
    print(f"Pipeline Success: Saved to {output_filename}\n")

if __name__ == "__main__":
    print("Initializing Faceless Shorts Engine Pipeline...")
    
    # Ingest structured data
    df = pd.read_csv("data/content.csv")
    
    # Execute batch generation
    for index, row in df.iterrows():
        generate_video(row['id'], row['text'])
