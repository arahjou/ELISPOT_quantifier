import streamlit as st
import cv2
import numpy as np
from skimage import measure, filters
import pandas as pd
from PIL import Image, ImageEnhance

# Function to adjust brightness and sharpness
def adjust_image(image, brightness_factor, sharpness_factor):
    pil_img = Image.fromarray(image)
    enhancer = ImageEnhance.Brightness(pil_img)
    image_bright = enhancer.enhance(brightness_factor)
    enhancer = ImageEnhance.Sharpness(image_bright)
    image_sharp = enhancer.enhance(sharpness_factor)
    return np.array(image_sharp)

# Function to quantify spots and return ROI coordinates
def quantify_spots(image, threshold_level, min_size, max_size):
    # Adjust thresholding approach
    threshold_value = filters.threshold_otsu(image)
    binary_image = image < threshold_value * threshold_level  # Adjust for black spots on light background
    labeled_image = measure.label(binary_image)
    properties = measure.regionprops(labeled_image, intensity_image=image)

    spot_info = []
    rois = []
    for prop in properties:
        area = prop.area
        if min_size <= area <= max_size:
            spot_info.append({
                'centroid': prop.centroid,
                'area': area,
                'mean_intensity': prop.mean_intensity,
                'max_intensity': prop.max_intensity
            })
            rois.append(prop.bbox)

    return spot_info, binary_image, rois

# Function to draw ROIs on the image
def draw_rois(image, rois):
    for roi in rois:
        minr, minc, maxr, maxc = roi
        image = cv2.rectangle(image, (minc, minr), (maxc, maxr), (255, 0, 0), 2)
    return image

# Function to determine dynamic range for spot sizes
def dynamic_size_range(image):
    height, width = image.shape
    max_limit = height * width // 50  # Example formula, adjust as needed
    return max_limit

# Streamlit app title
st.title('Image Spot Quantification Tool')

# File uploader
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['png', 'jpg'])

# Process each uploaded file
for uploaded_file in uploaded_files:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    # Dynamic range adjustment for spot size
    dynamic_max_size = dynamic_size_range(image)
    
    # Adjustable parameters
    threshold_level = st.slider('Threshold Level', 0.1, 1.0, 0.8)
    min_size = st.number_input('Minimum Spot Size', 1, dynamic_max_size, 10)
    max_size = st.number_input('Maximum Spot Size', 1, dynamic_max_size, 500)
    brightness_factor = st.slider('Brightness Factor', 0.5, 2.0, 1.0)
    sharpness_factor = st.slider('Sharpness Factor', 0.5, 2.0, 1.0)

    # Adjust brightness and sharpness
    adjusted_image = adjust_image(image, brightness_factor, sharpness_factor)

    # Quantify spots and get ROIs
    spots, thresholded_img, rois = quantify_spots(adjusted_image, threshold_level, min_size, max_size)

    # Draw ROIs on the adjusted image
    roi_image = draw_rois(np.copy(adjusted_image), rois)

    # Convert spot information to a DataFrame
    spots_df = pd.DataFrame(spots)

    # Display results
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(f"Original Image - {uploaded_file.name}")
        st.image(image, caption='Original Grayscale Image', use_column_width=True)
    with col2:
        st.write(f"Adjusted Image - {uploaded_file.name}")
        st.image(adjusted_image, caption='Brightness/Sharpness Adjusted Image', use_column_width=True)
    with col3:
        st.write(f"Thresholded Image - {uploaded_file.name}")
        st.image(thresholded_img, caption='Thresholded Image', use_column_width=True)
    with col4:
        st.write(f"ROI Image - {uploaded_file.name}")
        st.image(roi_image, caption='Image with ROIs', use_column_width=True)

    st.write(f"Total spots detected in {uploaded_file.name}: {len(spots)}")

    # Display the spot data in a table
    st.table(spots_df)
