
def main_pgm_multiple_pixels_per_line():
    ''' function to test student's code presuming PGM and
        one or more pixel values per line of the PGM file
    '''
    filename = "checkpoint1_mpl.pgm"
    try:
        image = Netpbm(f"images_checkpoint/pgm/{filename}")
    except Exception as error:
        print(f"Error in reading PGM {filename}")
        print(error)
        return
    else:
        header = ['P2', '# PGM checkpoint #1, multiple pixel values per line', [2,2], 255]
        pixels = [0, 128, 129, 255]

        print(f"Your Netpbm object read:")
        correct_header = '+' if image._header == header else 'x'
        correct_pixels = '+' if image._pixels == pixels else 'x'
        print(f"\t [{correct_header}] header: {image._header}")
        print(f"\t [{correct_pixels}] pixels: {image._pixels}")
        print(f"Expected:")
        print(f"\t     header: {header}")
        print(f"\t     pixels: {pixels}")
        correct = int(correct_header == '+') + int(correct_pixels == '+')
        print(f"Correct lists: {correct} / 2")

def main_ppm_multiple_values_per_line():
    ''' function to test student's code presuming PPM and
        one or more R or G or B value per line of the PPM file
    '''
    filename = "checkpoint1_mvl.ppm"
    try:
        image = Netpbm(f"images_checkpoint/ppm/{filename}")
    except Exception as error:
        print(f"Error in reading PPM {filename}")
        print(error)
        return
    else:
        header = ['P3', '# PPM checkpoint #1, multiple values per line', [2,2], 255]
        reds   = [0, 128, 129, 255]
        greens = [0, 128, 129, 255]
        blues  = [0, 128, 129, 255]
        pixels = [reds, greens, blues]

        print(f"Your Netpbm object read:")
        correct_header = '+' if image._header == header else 'x'
        correct_pixels = '+' if image._pixels == pixels else 'x'
        print(f"\t [{correct_header}] header: {image._header}")
        print(f"\t [{correct_pixels}] pixels: {image._pixels}")
        print(f"\nExpected:")
        print(f"\t     header: {header}")
        print(f"\t     pixels: {pixels}")
        correct = int(correct_header == '+') + int(correct_pixels == '+')
        print(f"\nCorrect lists: {correct} / 2")


# UNCOMMENT THIS IF DOING PGM, WITH MULTIPLE PIXEL VALUES PER LINE
main_pgm_multiple_pixels_per_line()

# UNCOMMENT THIS IF DOING PPM, WITH MULTIPLE VALUES (R and/or G and/or B) PER LINE
#main_ppm_multiple_values_per_line()


