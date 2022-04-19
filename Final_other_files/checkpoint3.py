

def main_pgm_write():
    image = Netpbm("images_checkpoint/pgm/checkpoint1_opl.pgm")
    header = ['P2', '# no comment', [2, 3], 128]
    pixels = [0, 16, 32, 32, 64, 128]
    image._header = header  # bad style -- but for helping students test!
    image._pixels = pixels  # bad style -- but for helping students test!

    fname_good    = "images_checkpoint/pgm/checkpoint3.pgm"
    fname_student = "images_checkpoint/pgm/checkpoint3_student.pgm" 
    print("Testing your PGM writeImage implementation:")
    image.writeImage(fname_student)

    import filecmp
    correct = '+' if filecmp.cmp(fname_good, fname_student) else 'x'
    print(f"\t [{correct}] Written output file matches expected")
    print(f"\nYour written file:")
    print('-' * 40)
    with open(fname_student, 'r') as infile:
        all_ = infile.read(); print(all_.strip())
    print('-' * 40)
    print(f"\nExpected file:")
    print('-' * 40)
    with open(fname_good, 'r') as infile:
        all_ = infile.read(); print(all_.strip())
    print('-' * 40)

def main_ppm_write():
    image = Netpbm("images_checkpoint/ppm/checkpoint1_ovl.ppm")
    header = ['P3', '# no comment', [2, 3], 17]

    # use sequential numbers for RGB to make debugging easier
    #pixels = [[0,8,16,32,0,8],[8,16,32,64,8,16],[16,32,64,128,16,32]]
    pixels = [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17]]
    image._header = header  # bad style -- but for helping students test!
    image._pixels = pixels  # bad style -- but for helping students test!

    fname_good    = "images_checkpoint/ppm/checkpoint3.ppm"
    fname_student = "images_checkpoint/ppm/checkpoint3_student.ppm" 
    print("Testing your PPM writeImage implementation:")
    image.writeImage(fname_student)

    import filecmp
    correct = '+' if filecmp.cmp(fname_good, fname_student) else 'x'
    print(f"\t [{correct}] Written output file matches expected")
    print(f"\nYour written file:")
    print('-' * 40)
    with open(fname_student, 'r') as infile:
        all_ = infile.read(); print(all_.strip())
    print('-' * 40)
    print(f"\nExpected file:")
    print('-' * 40)
    with open(fname_good, 'r') as infile:
        all_ = infile.read(); print(all_.strip())
    print('-' * 40)
    
main_pgm_write()
#main_ppm_write()
