import base64
import os
import json
import subprocess
import re
from openai import OpenAI

# Load API key securely from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OpenAI API Key. Set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

def encode_image(image_path):
    """Encodes an image to Base64 format."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Error: File {image_path} not found.")
        return None
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

def extract_bib_numbers(text):
    """Extracts bib numbers (digits) from the OpenAI response."""
    return re.findall(r'\b\d+\b', text)  # Finds sequences of digits

def analyze_image(image_path):
    """Sends an image to OpenAI for analysis and extracts bib numbers."""
    base64_image = encode_image(image_path)
    if not base64_image:
        return None  

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What are the runner bib numbers in this image?"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                    ],
                }
            ],
        )
        response_text = response.choices[0].message.content
        bib_numbers = extract_bib_numbers(response_text)  # Extract only numbers

        return bib_numbers  # Returns list of numbers
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def main(images_folder="images", output_file="results.json"):
    """Processes images and extracts runner bib numbers using OpenAI."""
    results = []  

    if not os.path.exists(images_folder):
        print(f"Error: Folder {images_folder} does not exist.")
        return

    for image_filename in os.listdir(images_folder):
        image_path = os.path.join(images_folder, image_filename)
        bib_numbers = analyze_image(image_path)
        
        if bib_numbers:
            results.append({"image_filename": image_filename, "bib_numbers": bib_numbers})

    with open(output_file, "w") as file:
        json.dump(results, file, indent=4)

    print(f"Results saved to {output_file}")

    # Run the JSON-to-CSV conversion script
subprocess.run(["python", "json_to_csv.py"])

if __name__ == "__main__":
    main()  # Run the script    