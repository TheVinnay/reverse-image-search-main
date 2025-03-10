# Reverse Image Search

## Overview
This project implements a reverse image search system using Python. It allows users to upload an image and find similar images from a dataset using feature extraction and similarity comparison techniques.

## Features
- Upload an image and search for similar images
- Uses feature extraction techniques like ORB, SIFT, or CNN-based embeddings
- Supports large-scale image datasets
- Efficient similarity comparison using KD-Tree, FLANN, or cosine similarity

## Technologies Used
- Python
- OpenCV
- Scikit-learn
- NumPy
- Flask (for web interface)

## Installation
```sh
# Clone the repository
git clone https://github.com/TheVinna/reverse-image-search.git
cd reverse-image-search

# Install dependencies
pip install -r requirements.txt
```

## Usage
```sh
python main.py --image path/to/query/image.jpg
```

To run the web interface:
```sh
python app.py
```

## Project Structure
```
reverse-image-search/
├── css/                  # Stylesheets for web interface
├── fonts/                # Font files for UI
├── images/               # Static images for web UI
├── js/                   # JavaScript files for frontend functionality
├── dataset/              # Image dataset
├── features/             # Extracted feature files
├── models/               # Pre-trained models (if any)
├── static/               # Web static files
├── templates/            # HTML templates for web UI
├── app.py                # Flask web application
├── main.py               # Command-line interface
├── A2 creations.py       # Additional script (describe purpose if needed)
├── import psutil.py      # Script for system monitoring (if applicable)
├── pip install psutil.py # Script to install psutil dependency
├── googlef8b4b65fa5f6e39e.html # Google verification file
├── index.html            # Homepage of the web interface
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
```

## Future Improvements
- Integrate deep learning models for better accuracy
- Improve search speed with more efficient indexing
- Expand dataset with diverse image categories

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the project!

## Contact
For any inquiries, contact [vinaytati64@gmail.com](mailto:vinaytati64@gmail.com).

