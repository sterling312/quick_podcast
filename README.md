# Quick Podcast

A simple tool to generate podcasts with multiple speakers from text files using Suno AI's Bark text-to-speech model.

## Description

Quick Podcast converts text into a podcast-like audio file with two alternating speakers. It uses Suno AI's Bark model to generate realistic voice audio from text.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quick_podcast.git
   cd quick_podcast
   ```

2. Install the required dependencies:
   ```bash
   pip install suno-bark scipy pydub
   ```

   Note: Installing Bark may take some time as it downloads large model files.

## Usage

1. Create a text file with your podcast script. Format it with alternating speakers.
   Example format:
   ```
   Dr. Smith:
   Welcome to "Innovations in Combustion," the podcast where we explore the latest breakthroughs in engine research and technology. I'm Dr. Smith, and today I'm joined by my esteemed colleague, Dr. Nguyen. We're discussing an exciting study on Reactivity Controlled Compression Ignition, or RCCI, combustion in dual-fuel engines. How are you today, Dr. Nguyen?

   Dr. Nguyen:
   I'm doing well, Dr. Smith—excited to delve into RCCI. This approach is fascinating because it not only offers enhanced fuel efficiency but also has the potential to significantly reduce harmful emissions. The paper we're reviewing today provides a comprehensive experimental analysis of RCCI. Have you noticed how the authors detailed the interplay between the high-reactivity and low-reactivity fuels?
   ```

2. Run the script:
   ```bash
   python quick_podcast.py input_text.txt output_podcast.wav
   ```

3. The script will generate an audio file with alternating speakers and a short pause between each segment.

## Notes

- The first time you run the script, it will download the Bark model files (approximately 5GB).
- Generation can be resource-intensive and may take some time depending on your hardware.
- The script uses specific voice profiles (speaker 9 and speaker 2) from Bark's available voices.

## License

See the LICENSE file for details.
