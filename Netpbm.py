#####################################################################
# DCS 109
# Professor: Barry Lawson
# Final Project: Image processing--Fauxtoshop
# Author: Yuhao Zhao
# Last date modified: 4/17/2022
## Overview: In this final project, you will pull together your experience from the semester
# in completing the work to implement a PGM and/or PPM image processing utility.
# This project builds on work from recent breakout/homework assignments in class.
# As detailed below, you will have options for what to implement based on what level grade you are seeking for the project.
# Among these options will be moving your implementation from working on grayscale (PGM) images only to working on color (PPM) images instead (or in addition).

#####################################################################
import copy
import random
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

        if self._header[0]=='P2':
            self._pixels = self.readPixels(image_file)
        elif self._header[0]=='P3':
            self._pixels = self.readPixels_3d(image_file)

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
        pixel_list = [] # create Empty list
        while line != "":
            # TO BUILD A LIST OF PIXELS (EACH AS int)
            pixel_list += line.split()
            line = image_file.readline().strip()

        # Convert string variables to int variables
        for i in range(len(pixel_list)):
                pixel_list[i]= int(pixel_list[i])

        return pixel_list


    def readPixels_3d(self, image_file: 'FileHandle') ->list:
        '''
        This is the similar function as the one above.
        The only difference is it read the pixels from PPM file and return a list
        of three elements where each element is a 1D list of integers
        representing the red, green, and blue pixel values accordingly.
        '''

        red =[]
        green =[]
        blue =[]
        # read the pixel payload and build a list of pixel values
        line = image_file.readline().strip()
        pixel_list = []
        while line != "":
            # TO BUILD A LIST OF PIXELS (EACH AS int)
            pixel_list += line.split()
            line = image_file.readline().strip()
        # Convert string variables to int variables
        for i in range(len(pixel_list)):
                pixel_list[i]= int(pixel_list[i])
        # Get the three lists representing RGB respectively
        red += pixel_list[0::3]
        green += pixel_list[1::3]
        blue += pixel_list[2::3]

        return [red, green, blue]

##################################################################
'''
This section of fruitful function we have covered most of them in class.
So I save the space for commenting:p
'''
    def isPGM(self) -> bool:
        if self._header[0]=="P2":
            return True
        else:
            return False

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
'''
Note:
if you simply return self. header or self. pixels, you will be giving back the address of the list that is stored inside your object
— meaning that a user could directly modify that list, outside of your control. The proper OOP approach is to return a copy of the list.
where you will need to import copy at the top of your file. Note that use of deepcopy, rather than copy,
will ensure that Python will make copies of lists within lists (e.g., for PPM).

'''
    def getHeader(self) -> list:

        return copy.deepcopy(self._header)

    def getPixels(self) -> list:

        return copy.deepcopy(self._pixels)


###################################################################
    def writeImage(self, new_filename: str) -> None:
        '''
        This method should open for writing a new file with the given filename,
        and then should write to that file the contents of your instance variables, self._header and self._pixels.

        '''
        new_image_file = open(new_filename, "w")
        # Call helper methods (see below) to write the PGM header and
        # pixels information into the new file
        self.writeHeader(new_image_file)

        if self._header[0]=="P2":
            self.writePixels(new_image_file)
        else:
            self.writePixels_3d(new_image_file)

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
        helper method write the pixels of a new PGM file connecting to the instance variable self._pixels

        '''
        # write a single pixel value per line of the new file.
        for i in range(len(self._pixels)):
            new_image_file.write(f"{self._pixels[i]}\n")

    def writePixels_3d(self, new_image_file: 'FileHandle') -> None:
        '''
        Helper method write the pxiesl of a new PPM file connecting to the instance variable self._pixels
        '''
        for k in range(len(self._pixels[0])):
            for i in range(len(self._pixels)):
                new_image_file.write(f"{self._pixels[i][k]}\n")

###################################################################
    def changeBrightness(self, amount:int) -> None:
        '''
        The method that will allow the user to change the brightness of a PGM image.
        Walk through your self._pixels instance variable, adding the given amount directly
        to each pixel value in that list.

        '''
        if self._header[0]=="P2": # change Brightness for PGM
            for i in range(len(self._pixels)):
                self._pixels[i]= self._pixels[i]+ amount

                # the pixel value will limit to the 0- maxlevel of pixel values
                if self._pixels[i]<0:
                    self._pixels[i]=0
                elif self._pixels[i]>self._header[3]:
                    self._pixels[i]=self._header[3]
        else: # For PPM
            for k in range(len(self._pixels[0])):
                for i in range(len(self._pixels)):
                    self._pixels[i][k] = self._pixels[i][k]+amount
                    # the pixel value will limit to the 0- maxlevel of pixel values
                    if self._pixels[i][k]<0:
                        self._pixels[i][k]=0
                    elif self._pixels[i][k]>self._header[3]:
                        self._pixels[i][k]=self._header[3]




    def invert(self) -> None:
        '''
        This method Convert each pixel value in your image to the maximum value
        (which may or may not be 255) minus the pixel value.
        '''
        if self._header[0]=="P2": # PGM
            for i in range(len(self._pixels)):
                self._pixels[i]= self._header[3]-self._pixels[i] # Invert the pixel values
        else: # PPM
            for k in range(len(self._pixels[0])):
                for i in range(len(self._pixels)):
                    self._pixels[i][k] = self._header[3]-self._pixels[i][k]



    def rotate(self, rotate_right:bool= True) -> None:
        '''
        The rotate_right parameter1 corresponds to a boolean indicating whether you should rotate to the right (90
        degrees clockwise) or the left (90 degrees counter-clockwise).

        Suggestions:
        • Create a new local list of pixel values, and append to that new list appropriately. If you are working on PPMs, you will need a list per RGB color.
        • To rotate 90 degrees clockwise, the first column of the original image from bottom to top should become the first row of the new image from left to right.
        Then the second column of the original image from bottom to top should become the second row of the new image from left to right. And so on.
        • Consider using doubly-nested for-loops. Specifically, one of those loops will allow you to navigate rows, while the other will allow you to navigate columns.
        You will need to index into the self._pixels list using an appropriate mathematical expression.
        (This is where working by hand on paper will help tremendously — and is why you worked on this in a breakout in class.)
        Make sure that your mathematical expression works by hand to access the appropriate element in the pixels list before you move to implementing in code.
        • Update the number of columns and rows appropriately in your self._header,
        and also update the self._pixels instance variable to be the new rotated pixels list(s).

        '''
        # Create new empty lists for later store
        local_pixel_list=[]
        local_red=[]
        local_green=[]
        local_blue=[]
        num_cols = self._header[2][0]
        num_rows = self._header[2][1]
        if rotate_right== True: # For right rotation
            if self._header[0]=="P2": # For PGM
                #cols loop
                for c in range(0, num_cols, 1):
                    #rows loop
                    for r in range(num_rows-1, -1, -1):
                        pixel_index = (num_cols*r+c)
                        pixel = self._pixels[pixel_index]
                        local_pixel_list.append(pixel)
                # Update the instance variables
                self._pixels = local_pixel_list
                self._header[2][0] = num_rows
                self._header[2][1] = num_cols

            else: # For PPM
                for c in range(num_cols-1, -1, -1): # column decreasing
                    for r in range(0, num_rows, 1): # row increasing
                        pixel_index= (num_cols*r+c) # calculate the pixel index from number of cols and rows
                        pixels_red = self._pixels[0][pixel_index]
                        pixels_green = self._pixels[1][pixel_index]
                        pixels_blue = self._pixels[2][pixel_index]
                        # Append the values to the local empty lists
                        local_red.append(pixels_red)
                        local_green.append(pixels_green)
                        local_blue.append(pixels_blue)
                # Update the instance variables
                self._pixels = [local_red, local_green, local_blue]
                self._header[2][0] = num_rows
                self._header[2][1] = num_cols
        else:# Rotate left
            if self._header[0]=="P2":
                    # column decreasing
                for c in range(num_cols-1, -1, -1):
                    #rows increaing
                    for r in range(0, num_rows, 1):
                        pixel_index = (num_cols*r+c)
                        pixel = self._pixels[pixel_index]
                        local_pixel_list.append(pixel)
                # Update the instance variables
                self._pixels = local_pixel_list
                self._header[2][0] = num_rows
                self._header[2][1] = num_cols

            else:
                for c in range(num_cols-1, -1, -1): # column decreasing
                    for r in range(0, num_rows, 1): # Row increasing
                        pixel_index= (num_cols*r+c) # calculate the pixel index from number of cols and rows
                        pixels_red = self._pixels[0][pixel_index] # Store the Red pixel values
                        pixels_green = self._pixels[1][pixel_index] # Store the green pixel values
                        pixels_blue = self._pixels[2][pixel_index] # Store the blue pixel values
                        # Append the values to the empty lists
                        local_red.append(pixels_red)
                        local_green.append(pixels_green)
                        local_blue.append(pixels_blue)
                # Update the instance variables
                self._pixels = [local_red, local_green, local_blue]
                self._header[2][0] = num_rows
                self._header[2][1] = num_cols











    def flip(self,vertical:bool= True) -> None:
        '''
        The vertical parameter corresponds to a a boolean —
        True if the image should be flipped vertically, or False if the
        image should be flipped horizontally.

        Suggestions:
        • To flip vertically, the last row in the original image should become the first row in the new image, then the next-to-last row in the original image should become the second row in the new image, and so on.
        • To flip horizontally, the last column in the original image should become the first column in the new image, then the next-to-last column in the original image should become the second column in the new image, and so on.
        • Again, working by hand on paper will help tremendously. Make sure that your logic will work on a small PGM (or PPM) that you can work through by hand, before proceeding to implementation.

        '''
        local_pixel_list=[]
        local_red=[]
        local_green=[]
        local_blue=[]
        num_cols = self._header[2][0]
        num_rows = self._header[2][1]
        if vertical== True:# Vertical Flip
            if self._header[0]=="P2": #  For PGM
                for r in range(num_rows-1, -1, -1): # Row decreasing
                    for c in range(0, num_cols, 1): # column increasing
                        pixel_index = (num_cols*r+c)
                        pixel = self._pixels[pixel_index]
                        local_pixel_list.append(pixel)
                self._pixels = local_pixel_list
            else: # For PPM
                for r in range(num_rows-1, -1, -1): # same as above
                    for c in range(0, num_cols, 1):
                        pixel_index= (num_cols*r+c)
                        pixels_red = self._pixels[0][pixel_index] # Update every element(list) in the pixel_list
                        pixels_green = self._pixels[1][pixel_index]
                        pixels_blue = self._pixels[2][pixel_index]
                        local_red.append(pixels_red)
                        local_green.append(pixels_green)
                        local_blue.append(pixels_blue)
                self._pixels = [local_red, local_green, local_blue]
        else: # Horizontal flip
            if self._header[0]=="P2": # PGM
                for r in range(0, num_rows, 1): # Row increasing
                    for c in range(num_cols-1, -1, -1): # Column decreasing
                        pixel_index = (num_cols*r+c)
                        pixel = self._pixels[pixel_index]
                        local_pixel_list.append(pixel)
                self._pixels = local_pixel_list
            else: # PPM
                for r in range(0, num_rows, 1): # same as above
                    for c in range(num_cols-1, -1, -1):
                        pixel_index= (num_cols*r+c)
                        pixels_red = self._pixels[0][pixel_index]
                        pixels_green = self._pixels[1][pixel_index]
                        pixels_blue = self._pixels[2][pixel_index]
                        local_red.append(pixels_red)
                        local_green.append(pixels_green)
                        local_blue.append(pixels_blue)
                self._pixels = [local_red, local_green, local_blue]

    def posterize(self, num_levels:int) -> None:
        '''
        This function will posterize an image by reducing the overall number of level/colors available,
        as shown by the examples below left and right which use 256 and 2 levels respectively.
        Essentially, we are "binning" the list--taking a large set of values and mapping them onto a smaller set of values.
        '''
        # get the maximum level of pixel values
        max_level = self.getMaxLevel()
        # Calculate the bin width for binning the pixels
        bin_width = (max_level + 1) / num_levels
        if self._header[0]=="P2":# For PGM
            for i in range(len(self._pixels)):
                self._pixels[i]= int(self._pixels[i]/bin_width)
            self._header[3]=num_levels
        else: # For PPM
            for k in range(len(self._pixels[0])):
                for i in range(len(self._pixels)):
                    self._pixels[i][k]= int(self._pixels[i][k]/bin_width)
            self._header[3]=num_levels






    def crop(self, upper_left_row: int, upper_left_column: int, lower_right_row: int, lower_right_column: int) -> None:
        '''
        The function should should result in a 2×3 image containing the pixels
        from upper_left_row and upper_left_column through lower_right_row and lower_right_column(inlusive).
        The images below show an example of using Fauxtoshop to crop cat eyes.ppm via a click-drag-release rubber-banding box to indicate the crop.
        The upper_left_row and upper_left_column parameters are integers
        corresponding to the row and column posi- tions of the start of the crop (inclusive).
        The lower_right_row and lower_right_column parameters are integers
        corresponding to the row and column positions of the end of the crop (inclusive).

        '''
        # generate local empty lists
        local_pixel_list=[]
        local_red=[]
        local_green=[]
        local_blue=[]
        # get num of cols and rows from header infos
        num_cols = self._header[2][0]
        num_rows = self._header[2][1]
        #For PGM
        if self._header[0]=="P2":
            for r in range(upper_left_row-1, lower_right_row, 1):
                for c in range(upper_left_column-1, lower_right_column, 1):
                    pixel_index = (num_cols*r+c)
                    pixels = self._pixels[pixel_index]
                    local_pixel_list.append(pixels)
            # Update the instance variable
            self._pixels =local_pixel_list
            self._header[2][0]=abs(lower_right_column-upper_left_column)+1
            self._header[2][1]=abs(lower_right_row-upper_left_row)+1
        else: # For PPM
            for r in range(upper_left_row-1, lower_right_row, 1):
                for c in range(upper_left_column-1, lower_right_column, 1):
                    pixel_index= (num_cols*r+c)
                    pixels_red = self._pixels[0][pixel_index]
                    pixels_green = self._pixels[1][pixel_index]
                    pixels_blue = self._pixels[2][pixel_index]
                    local_red.append(pixels_red)
                    local_green.append(pixels_green)
                    local_blue.append(pixels_blue)
            # Update the instance variables
            self._pixels = [local_red, local_green, local_blue]
            self._header[2][0]=abs(lower_right_column-upper_left_column)+1
            self._header[2][1]=abs(lower_right_row-upper_left_row)+1

    def toGrayscale(self) -> None:
        '''
        This non-fruitful method must convert the current PPM (color) image into a PGM (grayscale) image:
        By following the HDTV conversion standard where each grayscale pixel pi
        in the resulting image is determined using the red (ri), green (gi),
        and blue (bi) pixel components of the current image according to the following equation:
        p_i = 0.2126r_i + 0.7152g_i + 0.0722b_i

        '''
        # Get number of cols and rows
        num_cols = self._header[2][0]
        num_rows = self._header[2][1]
        # Generate local empty list for pixel values
        local_pixel_list=[]
        for i in range(0, num_cols*num_rows, 1):
            # convert RGB pixel values into grayscale value
            p_i= 0.2126*self._pixels[0][i]+0.7152*self._pixels[1][i]+0.0722*self._pixels[2][i]
            # Then append the grayscale values to local list
            local_pixel_list.append(int(p_i))

        # update the instance variables
        self._pixels = local_pixel_list
        self._header[0] = "P2"


    def glass(self, radius: int) -> None:
        '''
        This non-fruitful method must implement an algorithm that
        converts the current image into one that appears as though looking at the image through textured glass,
        similar to that shown below. The effect is achieved by creating a new version of the image where,
        for each pixel, you choose a pixel at random from the original image within a given radius.

        '''
        # Get number of cols and rows
        num_cols = self._header[2][0]
        num_rows = self._header[2][1]
        # generate local empty list for PGM and PPM(THREE RGB lists)
        local_pixel_list=[]
        local_red=[]
        local_green=[]
        local_blue=[]

        if self._header[0]=="P2":# For PGM
            for r in range(0, num_rows, 1):
                for c in range(0, num_cols, 1):# navigate through cols and rows
                    random1 = random.randint(-radius, radius) # getting the first random number
                    random2 = random.randint(-radius, radius) # getting the secound random number
                    row_Index = ((r + random1) + num_rows)%num_rows # calculating the random row
                    col_Index = ((c + random2) + num_cols)%num_cols # calculating the random column
                    local_pixel_list.append(self._pixels[num_cols*row_Index+col_Index])
            # Update the instance variable
            self._pixels = local_pixel_list
        else:# For PPM
            for r in range(0, num_rows, 1):
                for c in range(0, num_cols, 1):# navigate through cols and rows
                    random1 = random.randint(-radius, radius) # getting the first random number
                    random2 = random.randint(-radius, radius) # getting the secound random number
                    row_Index = ((r + random1) + num_rows)%num_rows # calculating the random row
                    col_Index = ((c + random2) + num_cols)%num_cols # calculating the random column
                    local_red.append(self._pixels[0][num_cols*row_Index+col_Index])
                    local_green.append(self._pixels[1][num_cols*row_Index+col_Index])
                    local_blue.append(self._pixels[2][num_cols*row_Index+col_Index])
            # Update the instance variable
            self._pixels = [local_red, local_green, local_blue]


















###################################################################
def main():
    image = Netpbm("images_checkpoint/ppm/checkpoint3.ppm")
    print(f"Magic #:    {image.getMagicNumber()}")
    print(f"Dimensions: {image.getNumRows()} X {image.getNumCols()}")
    print(f"Header:     {image.getHeader()}")
    print(f"Pixels:     {image.getPixels()}")
    image.toGrayscale()
    image.writeImage("images_checkpoint/ppm/gray_cp3.pgm")
    #image.changeBrightness(50)
    #image.writeImage("images/ppm/sample_bright.ppm")



if __name__ == "__main__":  # won’t call Netpbm’s main when running Fauxtoshop
    main()
