# README for ELISPOT_quantifier

## Overview
The `ELISPOT_quantifier` is a Python-based tool designed for immunological research, specifically for quantifying spots in ELISPOT (Enzyme-Linked ImmunoSpot) assays. ELISPOT is a widely used technique in immunology to detect and analyze cellular responses, primarily by quantifying the number of cells secreting a specific cytokine or other biomolecules. This tool leverages image processing techniques to automate the quantification of spots in ELISPOT assay images, thereby enhancing accuracy and efficiency in research.

## Features
- **Adjustable Image Processing**: Enhances image quality through brightness and sharpness adjustments.
- **Spot Quantification**: Automatically detects and quantifies spots based on adjustable parameters like threshold level, spot size, etc.
- **Region of Interest (ROI) Detection**: Identifies and marks ROIs containing spots for easy visualization.
- **Dynamic Spot Size Range**: Automatically determines a dynamic range for spot sizes based on the image dimensions.
- **Interactive UI**: Built with Streamlit for a user-friendly, interactive web application.

## Installation
To use `ELISPOT_quantifier`, the following Python libraries are required:
- Streamlit
- OpenCV (cv2)
- NumPy
- scikit-image
- Pandas
- PIL (Python Imaging Library)

Install these dependencies using pip:
```
pip install streamlit opencv-python numpy scikit-image pandas Pillow
```

## Usage
1. **Start the Streamlit App**: Run the script in a Python environment where all dependencies are installed. Streamlit will host a local web server and provide a URL to access the app.
2. **Upload Images**: Use the file uploader to select ELISPOT assay images (supports `png`, `jpg` formats).
3. **Adjust Parameters**: Interactively adjust parameters like threshold level, spot size, brightness, and sharpness.
4. **View Results**: The app displays the original, adjusted, thresholded, and ROI-marked images alongside quantitative data of detected spots in a table format.

## Example of Running the App
```
streamlit run ELISPOT_quantifier.py
```

## Contributing
Contributions to improve `ELISPOT_quantifier` are welcome. Please follow the standard fork-pull request workflow.

## License
This project is licensed under the MIT License

## Contact:
* This application is designe and developed by Ali Rahjouei.
* email: ali.rahjouei@gamil.com
---

*Note: This README assumes a certain level of familiarity with ELISPOT assays and basic image processing techniques in Python. Adjust the content as needed based on the target audience and application complexity.*
