#####################################################################
# DCS 109 Lab 3
# Author: Yuhao Zhao
# the date of last modification:
# Overall Description:
## This program is designed to build a new class of objects called Netpbm--which
## encapsulate the details of reading, writing, and modifying an image so that we
## can easily manipulate the image file like we did in basic data structure before
## --like lists/strings.

#####################################################################
# Define Netpbm Class
class Netpbm:

    # indicating the intended names of your instance variables
    __slots__ = ('_header', '_pixels')

    def  __init__(self, filename: str):
        '''
        Initializer method: set up initial values for the instance variables.
        Para:
              self: current object of this class type
              filename: input file to be read
        Returns:
              None
        '''
        # Open for reading the file with the given filename.
        image_file  = open(filename, "r")
        # Call helper methods (see below) to read and store into the
        # corresponding instance variable the PGM header and pixels information
        self._header = self.readHeader(image_file)
        self._pixels = self.readPixels(image_file)
        # Close the file
        image_file.close()



    def readHeader(self, image_file: 'FileHandle') -> list:
        '''
        The method will accept as its argument the file handle (not the filename)
        opened for reading back in __init__. The method should only read the
        first four lines of the file, and return a list containing the header information.
        '''
        # read the four lines of the PGM header
        magic_number   = image_file.readline().strip()
        comment        = image_file.readline().strip()
        cols_rows_line = image_file.readline().strip()
        max_level      = int(image_file.readline().strip())

        # convert the cols_rows_line (a str) into a list of two
        # integers -- remember .split() and int()
        cols_rows_list = cols_rows_line.split()
        for i in range(len(cols_rows_list)):
            cols_rows_list[i] = int(cols_rows_list[i])

        # create a list of the header info, each item of appropriate type (see above)
        header = [magic_number, comment, cols_rows_list, max_level]

        return header


    def readPixels(self, image_file: 'FileHandle') -> "list[int]":
        '''
        This method will accept as its argument the file handle (not the filename)
        opened for reading back in __init__.The method should read the
        remainder of the file, which corresponds to the pixel payload,
        and should return a list containing (as integers) all of the pixel values from the image
        '''
        # read the pixel payload and build a list of pixel values
        line = image_file.readline().strip()
        pixel_list=[]
        while line != "":
            # TO BUILD A LIST OF PIXELS (EACH AS int)
            pixel_list += line.split()
            line = image_file.readline().strip()

        # Convert string variables to int variables
        for i in range(len(pixel_list)):
                pixel_list[i]= int(pixel_list[i])
        return pixel_list

#######################################################
# Return the the corresponding values stored inside an instance variable.

    def getMagicNumber(self) -> str:

        return self._header[0]

    def getComment(self) -> str:

        return self._header[1]

    def getNumCols(self) -> int:

        return self._header[2][0]

    def getNumRows(self) -> int:

        return self._header[2][1]

    def getMaxLevel(self) -> int:

        return self._header[3]

    def getPixels(self) -> "list[int]":
        # Since list are mutable and we don't want it change,
        # use the .copy() method available from the list class to return a copy of self._pixels.
        Pixels = self._pixels.copy()
        return Pixels

######################################################
# Write and Adjust Image file .pgm

    def writeImage(self, new_filename: str) -> None:
        '''
        This method should open for writing a new file with the given filename,
        and then should write to that file the contents of your instance variables, self._header and self._pixels.

        '''
        new_image_file = open(new_filename, "w")
        # Call helper methods (see below) to write the PGM header and
        # pixels information into the new file

        self.writeHeader(new_image_file)
        self.writePixels(new_image_file)
        # Close the file
        new_image_file.close()


    def writeHeader(self, new_image_file: 'FileHandle') -> None:
        '''
        Helper method write the header of a new file connecting to the instance variable self._reader

        '''
        #write header info to the file precisely in expected PGM format
        new_image_file.write(f"{self._header[0]}\n")
        new_image_file.write(f"{self._header[1]}\n")
        new_image_file.write(f"{self._header[2][0]} {self._header[2][1]}\n")
        new_image_file.write(f"{self._header[3]}\n")

    def writePixels(self, new_image_file: 'FileHandle') -> None:
        '''
        helper method write the pixels of a new file connecting to the instance variable self._pixels

        '''
        # write a single pixel value per line of the new file.
        for i in range(len(self._pixels)):
            new_image_file.write(f"{self._pixels[i]}\n")


    def changeBrightness(self, amount: int) -> None:
        '''
        The method that will allow the user to change the brightness of a PGM image.
        Walk through your self._pixels instance variable, adding the given amount directly
        to each pixel value in that list.

        When adding the amount, any pixel value that would be negative is set to zero,
        and any pixel value that would be greater than the max value is set to the max value.

        '''
        for i in range(len(self._pixels)):
            self._pixels[i]= self._pixels[i]+ amount

            if self._pixels[i]<0:
                self._pixels[i]=0
            elif self._pixels[i]>self._header[3]:
                self._pixels[i]=self._header[3]

######################################################



    def __str__(self) -> str:
        ''' method to return a string representation of the Netpbm object
        Returns:
            a string containing the header info and the first 3 and last
            3 pixel values
        '''
        string = f"{self._header[0]}\n{self._header[1]}\n" \
               + f"{self._header[2][0]} {self._header[2][1]}\n" \
               + f"{self._header[3]}\n"
        for i in range(0, 3, 1):
            string += f"{self._pixels[i]} "
        string += "... "
        for i in range(len(self._pixels) - 3, len(self._pixels), 1):
            string += f"{self._pixels[i]} "
        return string


#####################################################################
def main():
    image = Netpbm("sample.pgm")
    print(image)
    print()

    ###########
    # INCLUDE NEW TESTS HERE TO TEST YOUR GETTER METHODS
    ###########
    print(image.getMagicNumber()+"\n")
    print(image.getComment()+"\n")
    print(image.getNumCols())
    print(image.getNumRows())
    print()
    print(image.getMaxLevel())
    print()
    print(image.getPixels())


    print()

    ###########
    # UNCOMMENT THIS WHEN READY TO TEST writeImage
    ###########
    image_copy = image.writeImage("sample_copy.pgm")

    ###########
    # UNCOMMENT THIS WHEN READY TO TEST changeBrightness
    ###########
    image.changeBrightness(20)
    image.writeImage("sample_bright.pgm")

    lilly = Netpbm("lilly.pgm")
    print(lilly)

    ###########
    # UNCOMMENT THIS WHEN READY TO TEST changeBrightness
    ###########
    lilly.changeBrightness(100)
    lilly.writeImage("lilly_bright.pgm")

main()
