
def main():
    image = Netpbm("images_checkpoint/pgm/checkpoint1_opl.pgm")
    header = ['P2', '# no comment', [2, 3], 128]
    pixels = [0, 16, 32, 32, 64, 128]
    image._header = header  # bad style -- but for helping students test!
    image._pixels = pixels  # bad style -- but for helping students test!

    results = [
        image.getMagicNumber(),
        image.getComment(),
        image.getNumCols(),
        image.getNumRows(),
        image.getMaxLevel(),
        image.getHeader(),
        image.getPixels()]

    correct = [''] * len(results)
    correct[0] = '+' if header[0]    == results[0] else 'x'
    correct[1] = '+' if header[1]    == results[1] else 'x'
    correct[2] = '+' if header[2][0] == results[2] else 'x'
    correct[3] = '+' if header[2][1] == results[3] else 'x'
    correct[4] = '+' if header[3]    == results[4] else 'x'

    # header must match, and be a copy
    if header == results[5] and id(image._header) != id(results[5]):
        correct[5] = '+'
    else:
        correct[5] = '-'

    # pixels must match, and be a copy
    if pixels == results[6] and id(image._pixels) != id(results[6]):
        correct[6] = '+'
    else:
        correct[6] = '-'

    print(f"Testing your getter methods:")
    print(f"\t [{correct[0]}] Magic #:   {results[0]} \t\t type: {type(results[0])}")
    print(f"\t [{correct[1]}] Comment:   {results[1]}   \t type: {type(results[1])}")
    print(f"\t [{correct[2]}] # Cols:    {results[2]} \t\t type: {type(results[2])}")
    print(f"\t [{correct[3]}] # Rows:    {results[3]} \t\t type: {type(results[3])}")
    print(f"\t [{correct[4]}] Max Level: {results[4]} \t\t type: {type(results[4])}")
    print()
    is_a_copy = id(results[5]) != id(image._header)
    print(f"\t [{correct[5]}] Header:    {results[5]}   \t is a copy?: {is_a_copy}")
    is_a_copy = id(results[6]) != id(image._pixels)
    print(f"\t [{correct[6]}] Pixels:    {results[6]} \t\t is a copy?: {is_a_copy}")

    print(f"\nExpected:")
    print(f"\t     Magic #:   {header[0]} \t\t type: {type(header[0])}")
    print(f"\t     Comment:   {header[1]}   \t type: {type(header[1])}")
    print(f"\t     # Cols:    {header[2][0]} \t\t type: {type(header[2][0])}")
    print(f"\t     # Rows:    {header[2][1]} \t\t type: {type(header[2][1])}")
    print(f"\t     Max Level: {header[3]} \t\t type: {type(header[3])}")
    print()
    print(f"\t     Header:    {header}   \t is a copy?: {True}")
    print(f"\t     Pixels:    {pixels} \t\t is a copy?: {True}")

    num_correct = sum(ans == '+' for ans in correct)
    print(f"\nCorrect getters: {num_correct} / {len(correct)}")

main()

