# FaceCrop 📸

FaceCrop is a simple command-line tool that automates the cropping of images 🖼️ based on face detection. It works by identifying the largest face (i.e., the face that's likely closest to the camera) in an image, adds a margin around it (which you can customize), and then crops the image to this area. This tool is ideal for quickly cropping batches of images for social media 👥, user avatars 🚀, or AI training datasets 💡.

![Demo](example.png)

## Dependencies 🛠️

FaceCrop depends on the following Python libraries:

- OpenCV
- PIL
- glob
- argparse
- os

Please make sure these are installed. You can install them using pip:

```sh
pip install opencv-python Pillow
```

## Usage 💻

This tool can be used through the command line. Here is the general syntax:

```sh
python3 facecrop.py [input_directory] -o [output_directory] -s [desired_size] -r [margin_ratio]
```

Where:
- `[input_directory]` is the path to the directory containing the images you want to crop.
- `[output_directory]` (optional) is the path to the directory where you want to save the cropped images. If not provided, a new folder named "resized" will be created in the input directory.
- `[desired_size]` (optional) is the desired size of the output images in pixels (default is 500).
- `[margin_ratio]` (optional) is the margin around the face as a ratio of the face size (default is 0.2).

For example, the following command will crop all images in the "input_images" folder and save them to the "resized" folder. The size of the output images will be 500x500 pixels, and a 20% margin will be added around each detected face:

```sh
python3 facecrop.py input_images -o cropped_images -s 500 -r 0.2
```

## Notes 📝

- The face detection may not be perfect, especially with low-quality images, unusual lighting conditions, or uncommon face orientations. However, it should work well for typical photos 📷.
- The tool will try to center the eyes and mouth of the face to the center of the image 😊.
- The cropping and resizing process may distort the aspect ratio of the original image.
- Images without any detected faces will not be processed 🚫.
- The tool works with most common image formats (JPG, PNG, etc.).

## Future Features 🔮

Here are a few enhancements we're thinking about for future versions of FaceCrop:

1. **Custom Aspect Ratios**: Currently, the tool crops images to be squares (i.e., the width and height are the same). We plan to add an option to allow for custom aspect ratios. For example, you might want to crop images to be 500x700 pixels instead of just 500x500. This will provide greater flexibility for different use cases and requirements. 🔄

3. **Face Recognition**: We could integrate face recognition functionality to allow users to crop images based on specific individuals. This would be particularly useful for user-specific albums or datasets. 🕵️‍♀️

4. **Multiple Face Cropping**: Currently, the tool crops images around the largest face it detects. An option to crop around each detected face and save as separate images would be helpful in situations with group photos. 👪

5. **Command Line Interface (CLI) Improvements**: Making the tool more interactive through the CLI would also be a good feature. For example, we could add progress bars for batch processes, previews of cropped images, and options to adjust settings on the fly. ⌨️

6. **GUI Implementation**: A GUI version of the tool could make it more accessible for users who aren't as comfortable with command-line interfaces. The GUI could provide real-time previews and adjustments. 🖥️

7. **Machine Learning Improvements**: Enhancing the face detection algorithm with machine learning could improve its accuracy, particularly with more difficult images. This could be an interesting area for development and collaboration. 🤖

These are just a few of the possibilities. We welcome ideas and contributions from our users to make FaceCrop more useful! 🌟

## Contributing 🤝

Please feel free to fork this project, create a feature branch, and submit a pull request.

## Contact 📬

If you have any questions, feel free to open an issue or submit a pull request.
