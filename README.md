# 🚀 AI-Image-Processing-BibVision

**AI-Image-Processing-BibVision** is a Python-based AI-powered image processing tool that extracts runner bib numbers from images using OpenAI's API. It automatically processes images, extracts bib numbers, and saves the results in JSON and CSV formats.

## 📌 Table of Contents
- [🔍 Overview](#-overview)
- [✨ Features](#-features)
- [⚙️ Installation](#-installation)
- [▶️ Usage](#-usage)
- [📂 File Structure](#-file-structure)
- [🔑 API Key Setup](#-api-key-setup)
- [🛠️ Customization](#-customization)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 🔍 Overview
This project utilizes OpenAI's GPT-4o model to analyze images containing runner bib numbers. The extracted numbers are stored in `results.json` and automatically converted into `results.csv` for further analysis.

## ✨ Features
✅ **Image Processing:** Reads and processes images to extract bib numbers.  
✅ **AI-Based Recognition:** Uses OpenAI's API for accurate text extraction.  
✅ **Automated Conversion:** Automatically converts JSON results into CSV.  
✅ **Customizable Processing:** Allows manual JSON-to-CSV conversion if preferred.  

## ⚙️ Installation
1️⃣ **Clone the Repository:**  
   ```bash
   git clone https://github.com/yaspreure/AI-Image-Processing-BibVision.git
   cd AI-Image-Processing-BibVision
   ```
2️⃣ **Set Up a Virtual Environment (Optional but Recommended):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3️⃣ **Install Required Dependencies:**  
   ```bash
   pip install openai pandas
   ```
4️⃣ **Set Up OpenAI API Key:**  
   You need to **purchase an API key** from OpenAI and set it as an environment variable:  
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
   On Windows (Command Prompt):  
   ```cmd
   set OPENAI_API_KEY=your_api_key_here
   ```

## ▶️ Usage
### **1️⃣ Process Images and Extract Bib Numbers**
📂 **Place your images inside the `images/` folder.**  
▶️ **Run the main script:**  
   ```bash
   python image_processing.py
   ```
📄 **Extracted results will be saved in `results.json` and automatically converted to `results.csv`.**  

### **2️⃣ Convert JSON to CSV Manually**
If you prefer to convert JSON to CSV manually, **modify `image_processing.py` as follows**:  
❌ **Remove these two lines:**  
   ```python
   import subprocess
   subprocess.run(["python", "json_to_csv.py"])
   ```
✅ **Then, run the conversion script manually:**  
   ```bash
   python json_to_csv.py
   ```

## 📂 File Structure
```
AI-Image-Processing-BibVision/
│── images/                 # Folder containing input images (JPG format)
│── results.json            # Output file containing extracted bib numbers
│── results.csv             # CSV version of results.json
│── image_processing.py     # Main script to process images and extract numbers
│── json_to_csv.py          # Script to convert JSON results to CSV
│── README.md               # Project documentation
```

## 🔑 API Key Setup
You **must purchase an API key** from OpenAI and set it as an environment variable before running the scripts.

## 🛠️ Customization
- **Modify the OpenAI prompt** in `image_processing.py` to improve accuracy:
  ```python
  {"type": "text", "text": "What are the runner bib numbers in this image?"}
  ```
- **Change the output format** in `json_to_csv.py` by modifying `pandas.DataFrame.to_csv()` options.

## 🤝 Contributing
Contributions are welcome! Feel free to **open issues** or **submit pull requests**.

## 📜 License
This project is licensed under the **MIT License**.

---
