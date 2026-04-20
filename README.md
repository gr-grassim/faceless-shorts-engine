# Faceless Shorts Automation Engine

An automated, pure Python pipeline designed for the hands-off generation and orchestration of vertical short-form video content. 

This project bypasses manual video editing software by utilizing a programmatic approach to content creation. It ingests structured data, dynamically calculates and renders text overlays, and composites high-definition multi-layer video outputs entirely via code.

## System Architecture

* **Data Ingestion:** Utilizes `pandas` to read and iterate through structured datasets (CSV/JSON), allowing for scalable batch processing of content.
* **Dynamic Rendering:** Implements `Pillow` (PIL) to mathematically calculate text bounding boxes, enabling dynamic text-wrapping and automated centering based on a 9:16 vertical aspect ratio.
* **Automated Compositing:** Leverages `MoviePy` to stitch together background media, translucent contrast layers, and rendered text graphics into a final `.mp4` output without human intervention.
* **Dependency Isolation:** Built utilizing strict virtual environments to ensure clash-free scaling with future Machine Learning or AI orchestration libraries.

## Project Structure

```text
faceless-shorts-engine/
├── assets/
│   ├── background.mp4      # Base video footage (9:16)
│   └── font.ttf            # Custom TrueType font file
├── data/
│   └── content.csv         # Structured input data
├── outputs/                # Rendered .mp4 outputs
├── engine.py               # Core compositing and rendering logic
└── requirements.txt        # Environment dependencies
    '''

## Setup & Installation
1. Clone the repository:
    '''bash
    git clone [https://github.com/gr-grassim/faceless-shorts-engine.git](https://github.com/gr-grassim/faceless-shorts-engine.git)
    cd faceless-shorts-engine

2. Initialize the Virtual Environment:
    '''Bash
    python -m venv venv

3. Activate the Environment:
    Windows: .\venv\Scripts\activate
    Mac/Linux: source venv/bin/activate

4. Install Dependencies:
    '''Bash
    pip install -r requirements.txt

## Usage
1. Ensure a valid vertical video is located at assets/background.mp4.
2. Ensure a valid TrueType font is located at assets/font.ttf.
3. Update the data/content.csv file with your desired text (wrap text containing commas in double quotes "").
4. Execute the rendering pipeline:
    '''Bash
    python engine.py

5. Check the outputs/ directory for your automatically generated short-form videos.

## 👨‍💻 Author
Grassim Jaiswal

Python Full-Stack Developer

LinkedIn Profile **https://linkedin.com/in/gr-grassim/**

GitHub Profile **https://github.com/gr-grassim/**
