
import os
import sys
from PIL import Image

# list all files recursively in a directory
def list_files(directory, extensions = ['.png', '.jpg', '.jpeg', '.svg']):
    files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            # output file name and extension
            # append the file name to the list if extension is in the list
            if extension in extensions:
                files.append(os.path.join(root, filename))
    return files

# extract file name and folder name from a path
def extract_name(path):
    # get the folder name immediately above the file
    folder = os.path.basename(os.path.dirname(path))
    file = os.path.basename(path)
    return folder, file

# read a png image and slice it X rows and Y columns
def slice_image(image, rows, columns):
    width, height = image.size
    piece_width = width / columns
    piece_height = height / rows
    pieces = []
    for i in range(rows):
        for j in range(columns):
            box = (j * piece_width, i * piece_height,
                   (j + 1) * piece_width, (i + 1) * piece_height)
            pieces.append(image.crop(box))
    return pieces

def short_img_name(image_name, right=5):
    # remove image name extension
    name = os.path.splitext(image_name)[0]
    return name[-right:]

# save the pieces into a folder
def save_images(slices, output_folder, image_name):
    index = 1
    # remove image name extension
    slice_name = short_img_name(image_name, 5)
    output_path = output_folder + '/'
    # if path doesn't exist, create it
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for image in slices:
        image.save(os.path.join(output_path, slice_name + '_%s.png' % index))
        index += 1

# list all files in input folder
# for each file, slice the image and save the pieces into output folder

    

if __name__ == '__main__':
    
    input_folder = sys.argv[1] # input folder
    ouptut_folder = sys.argv[2] # output folder
    rows, columns = sys.argv[3].split(',') # capture matrix
    if not os.path.exists(ouptut_folder): os.mkdir(ouptut_folder)

    print('Input: {0}, Output: {1}, Matrix: {2}x{3}'.format(
        input_folder, ouptut_folder, rows, columns))

    # list all files in the input folder
    files = list_files(input_folder)
    for file in files:
        # extract file name and folder name
        folder, file_name = extract_name(file)
        # print processing folder, file_name
        # { code: '5b0-1', tiles: 9 },
        print('{0} code: {1}, tiles: {2}'.format(folder, short_img_name(file_name, 5), int(rows) * int(columns)))
        destination = ouptut_folder + '/' + folder
        # read image
        image = Image.open(file)
        # slice image
        slices = slice_image(image, int(rows), int(columns))
        # save pieces
        save_images(slices, destination, file_name)
    
    # activate the virtual environment
    # source venv/bin/activate
    # run the script
    # python img_slicer.py input output 3,3