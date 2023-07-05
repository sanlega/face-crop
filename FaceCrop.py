import cv2
import os
import glob
import argparse
from PIL import Image

def get_largest_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if isinstance(faces, tuple):
        return []

    largest_face = max(faces, key=lambda rectangle: rectangle[2] * rectangle[3])

    return largest_face


def crop_to_face(image_path, output_path, desired_size, margin_ratio):
    largest_face = get_largest_face(image_path)

    if len(largest_face) == 0:
        print(f"No faces detected in the image: {image_path}")
        return

    im = Image.open(image_path)

    left = largest_face[0]
    top = largest_face[1]
    right = left + largest_face[2]
    bottom = top + largest_face[3]

    width = right - left
    height = bottom - top
    margin_x = width * margin_ratio
    margin_y = height * margin_ratio

    left = max(0, left - margin_x)
    top = max(0, top - margin_y)
    right = min(im.width, right + margin_x)
    bottom = min(im.height, bottom + margin_y)

    im_cropped = im.crop((left, top, right, bottom))

    im_resized = im_cropped.resize((desired_size, desired_size), Image.LANCZOS)

    im_resized.save(output_path)


def process_directory(input_directory, output_directory, desired_size, margin_ratio):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    image_files = glob.glob(os.path.join(input_directory, '*.[pjJ][npNP][gG]*'))

    for image_file in image_files:
        file_name = os.path.basename(image_file)
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(output_directory, f"{base_name}_crop{ext}")
        crop_to_face(image_file, output_file, desired_size, margin_ratio)


def main():
    # Argument parser:
    parser = argparse.ArgumentParser(description='Process some images.')
    parser.add_argument('input_directory', type=str, help='Path to the input directory')
    parser.add_argument('-o', '--output_directory', type=str, help='Path to the output directory')
    parser.add_argument('-s', '--desired_size', type=int, default=500, help='Desired size of output images')
    parser.add_argument('-r', '--margin_ratio', type=float, default=0.2, help='Margin around the face as a ratio of face size')
    args = parser.parse_args()

    output_directory = args.output_directory if args.output_directory else os.path.join(args.input_directory, 'resized')

    process_directory(args.input_directory, output_directory, args.desired_size, args.margin_ratio)

if __name__ == '__main__':
    main()
