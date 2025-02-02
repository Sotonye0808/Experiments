# Final Year Project Experiments

This repository contains programs used in conducting experiments in relation to my final year project. The experiments are designed to test various hypotheses, gather data for analysis and determine performance metrics.

## Structure

The modules are named according to what role they perform.
'process.py' is used for processing signatures to clean up images of signatures captured by phone cameras

The 'evaluation_modules' holds various modules for determining the performance of the system.
- 'ssim.py' determines the Structural Similarity Index (SSIM), measuring the perceptual similarity between the original and reproduced signature images.
- 'line_smoothness.py' determines the Line Smoothness Score, measuring how consistent and fluid the reproduced signature strokes are, avoiding jagged or shaky lines.
- 'gcode_error.py' determines G-Code Execution Error, measuring how precisely the robot follows the G-code instructions.

## Usage tips

- You can create a 'testing_images' directory to hold images you wish to use for experimentation or analysis.
- Libraries to install using pip include 'opencv_python', 'numpy', 'svgwrite' and 'scikit-image' ('os' and 'python-dotenv', if not already pre-installed with your python version)

## Contact

For any questions or issues, please contact [Sotonye Dagogo](mailto:sotydagz@gmail.com).
