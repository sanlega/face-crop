# FaceCrop 📸

FaceCrop is a simple command-line tool that automates the cropping of images based on face detection. It works by identifying the largest face (i.e., the face that's likely closest to the camera) in an image, adds a margin around it (which you can customize), and then crops the image to this area. This tool is ideal for quickly cropping batches of images for social media, user avatars, or AI training datasets.

![Demo](example.png)

## Dependencies

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

## Usage

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

## Notes

- The face detection may not be perfect, especially with low-quality images, unusual lighting conditions, or uncommon face orientations. However, it should work well for typical photos.
- The cropping and resizing process may distort the aspect ratio of the original image.
- Images without any detected faces will not be processed.
- The tool works with most common image formats (JPG, PNG, etc.).

## Contributing

Please feel free to fork this project, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feel free to open an issue or submit a pull request.
