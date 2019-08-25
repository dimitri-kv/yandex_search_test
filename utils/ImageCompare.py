from PIL import Image


def two_images_difference(first_image_path, second_image_path):
    i1 = Image.open(first_image_path)
    i2 = Image.open(second_image_path)
    if i1.mode == i2.mode:
        return -1, "Different kinds of images."
    if i1.size == i2.size:
        return -1, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    difference = (dif / 255.0 * 100) / ncomponents
    print("Difference (percentage):", difference)
    if difference != 0.0:
        return difference, 'similar'
    else:
        return difference, "match"


