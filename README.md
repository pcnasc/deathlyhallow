# Invisibility Cloak with Computer Vision

This project is a Python implementation of Harry Potter's **"Invisibility Cloak"**, inspired by Tiff in Tech's code. The original version can be found on her GitHub. The program leverages **OpenCV** to create a masking effect, replacing the cloak’s color with a captured background, thus effectively simulating invisibility.

## How It Works
1. Captures a static background when you step out of the frame.  
2. Detects a specific cloak color (e.g., red, blue, etc.) using **HSV color thresholds**.  
3. Masks the detected color and seamlessly blends the captured background in its place, making the cloak appear invisible in real time.  

## Requirements
- Python 3.x  
- OpenCV (`pip install opencv-python`)  
- NumPy (`pip install numpy`)  

## How to Use
1. Clone this repository:  
   ```bash  
   git clone https://github.com/pcnasc/invisible-cloak.git  

2.	Install a couple of dependencies:
    ```bash
    pip install -r requirements.txt  

## Features
	•	Dynamic masking of cloak color.
	•	Customizable HSV thresholds for different colors.
	•	Real-time processing using OpenCV.

## Acknowledgements

This project was inspired by the youtube tutorial by Tiff in Tech. Check out her content for more Python and tech projects.

## License

[MIT LICENSE]


## Future Features 

	•	Implementation of a live background to enhance the realism of the Concealment Wizardry.
