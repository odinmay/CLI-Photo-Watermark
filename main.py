import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=False,
                help='Path to target file')
ap.add_argument('-w', '--watermark', required=True,
                help='Text you would like to watermark image with | (Enclose in quotes if there are spaces)')
ap.add_argument('-d', '--directory', required=False,
                help='Processes every image in the CWD')
ap.add_argument('-p', '--pos', required=True,
                help='Options are "ul"(upper left) "ur"(upper right) "ll"(lower left) "lr"(lower right)')
args = ap.parse_args()


def process_image(filename, watermark, pos):
    working_image = cv2.imread(filename)
    font = cv2.FONT_HERSHEY_COMPLEX
    text_length = len(watermark)
    color = (255, 255, 255)
    thickness = 4
    if working_image.shape[0] >= 4000:
        avg_char = 120
        text_width = text_length * avg_char
        fontScale = 6
        image_ul = (0, 150)
        image_ur = (working_image.shape[1] - text_width, 150)
        image_ll = (0, working_image.shape[0] - 50)
        image_lr = (working_image.shape[1] - text_width, working_image.shape[0] - 50)
    else:
        avg_char = 80
        text_width = text_length * avg_char
        fontScale = 4
        image_ul = (0, 100)
        image_ur = (working_image.shape[1] - text_width, 100)
        image_ll = (0, working_image.shape[0] - 50)
        image_lr = (working_image.shape[1] - text_width, working_image.shape[0] - 50)

    if pos == 'ul':
        new_image = cv2.putText(working_image, args.watermark, image_ul, font, fontScale, color, thickness, cv2.LINE_AA)

    if pos == 'ur':
        new_image = cv2.putText(working_image, args.watermark, image_ur, font, fontScale, color, thickness, cv2.LINE_AA)

    if pos == 'll':
        new_image = cv2.putText(working_image, args.watermark, image_ll, font, fontScale, color, thickness, cv2.LINE_AA)

    if pos == 'lr':
        new_image = cv2.putText(working_image, args.watermark, image_lr, font, fontScale, color, thickness, cv2.LINE_AA)

    if not os.path.exists(args.directory + '\\Watermarked'):
        os.mkdir(args.directory + '\\Watermarked')

    path = args.directory + '\\' + 'Watermarked' + '\\' + file
    cv2.imwrite(path, new_image)


for file in os.listdir(args.directory):
    if file.endswith('.jpg') or file.endswith('.png'):
        process_image(args.directory + '\\' + file, args.watermark, args.pos)
