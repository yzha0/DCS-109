from MakeSong import *   # allows use of the MakeSong() utility

import random

def reverseSong(song: str) -> str:
    ''' Function to create and return a new string that is the reverse of the
        given song string.
    Args:
        song: a string of musical notes
    Returns:
        reversed version of the given string
    '''
    Rsong=""
    for i in range(len(song) - 1, -1, -1):
        Rsong= Rsong+ str(song[i])
    return Rsong
    #return song[::-1] which is convienient way but we coudn't use the string slicing

def raiseOctave(lower_octave_song: str)-> str:
    '''
    this function must return a new string in which the notes have been raised (uppercased) to the upper octave.

    Parameters:
    lower_octave_song: A song string consists of lowercase notes in the lower octave
    Returns:
    a new string where the notes have all been raised to the upper octave.

    '''
    Raised_Song=""
    for i in range(len(lower_octave_song)):
        Raised_Song=Raised_Song+lower_octave_song[i].upper()

    return Raised_Song




def lowerOctave(Upper_octave_song: str)-> str:
    '''
    this function return a new string in which the notes have been lowered to the lower octave.

    Parameters:
    Upper_octave_song: A song string consists of Uppercase notes in the upper octave
    Returns:
    a new string where the notes have all been lower to the lower octave.

    '''
    Lower_Song=""
    for i in range(len(Upper_octave_song)):
        Lower_Song=Lower_Song+Upper_octave_song[i].lower()

    return Lower_Song


def raiseOctavePart(song:str, start:int, stop:int)-> str:
    '''
    Given a song string consisting of (at least some) lowercase notes in the lower octave,
    this function must return a newly-built string in which only the notes
    between indices start and stop both inclusive have been raised to the upper octave.

    Parameters:
    song: string consists of some lowercase notes in the lower octave
    start:
    stop:
    Returns:
    a raised song string of upper octave
    '''
    adjusted_song=""
    for i in range(0, start, 1):
        adjusted_song= adjusted_song+ song[i]
    for k in range(start, stop+1, 1):
        adjusted_song= adjusted_song+ song[k].upper()
    for j in range(stop+1, len(song),1):
        adjusted_song= adjusted_song + song[j]

    return adjusted_song


def lowerOctavePart(song:str, start:int, stop:int)-> str:
    '''
    Given a song string consisting of (at least some) uppercase notes in the upperer octave,
    this function must return a newly-built string in which only the notes
    between indices start and stop both inclusive have been lowered to the lower octave.

    Parameters:
    song: string consists of some uppercase notes in the upper octave
    start:
    stop:

    Returns:
    a lowered song string of lower octave

    '''

    lower_adjusted_song=""
    for i in range(0, start, 1):
        lower_adjusted_song= lower_adjusted_song+ song[i]
    for k in range(start, stop+1, 1):
        lower_adjusted_song= lower_adjusted_song+ song[k].lower()
    for j in range(stop+1, len(song),1):
        lower_adjusted_song= lower_adjusted_song + song[j]

    return lower_adjusted_song

def randomsong(notes: str, min_notes:int, max_notes:int )-> str:
    '''
    This function must build from scratch and then return a new string
    consisting of notes chosen at random from the given notes string.

    Parameters:
    notes:   an input note string
    min_note:  an integer where to start to select notes
    max_note:  an integer indicates where to stop to select notes

    Returns:
     a new string consisting of notes chosen at random from the given notes string.

    '''
    random_song=""
    lenth_song= random.randint(min_notes, max_notes)
    for i in range(lenth_song):
        random_song=random_song+notes[random.randint(0, len(notes)-1)]

    return random_song






################################################################################
def printTest(function_call_str: str, result: str, expected: str) -> None:
    ''' Streamlines regression testing calls, displaying the function call being
        made, the actual result, & the expected result.
    Parameters:
        function_call_str: a string representing the function call, e.g.,
                           'reverseSong("abcde")'
        result:            the actual result of that function call
        expected:          the expected result of that function call
    Returns:
        None -- just prints
    '''
    print(f"Testing {function_call_str}:")
    print(f"   Result:   {repr(result)}")
    print(f"   Expected: {repr(expected)}")

################################################################################
def main():
    # some fun song strings, in order:
    #   (a) "Mary Had A Little Lamb"
    #   (b) "Twinkle Twinkle Little Star"
    #   (c) "Smoke On The Water" intro, by Deep Purple
    #   (d) opening eight measures from Suite No. 1 in G Major for Cello,
    #       by J.S. Bach (transposed to C b/c of MakeSong limitations)
    mary    = "edcdeee ddd egg edcdeeeeddedc"
    twinkle = "ccggaag-ffeeddc-ggffeed-ggffeed-ccggaag-ffeeddc"
    smoke   = "gga#a#CC--ga#a#C#CC--gga#a#CC--a#ggg--"
    cello   = "cgEDEgEgcgEDEgEgcaFEFaFacaFEFaFacbFEFbFbcbFEFbFbcCEDECECcCEDECEb"
    youWhoLove105c = "EEFEDEa DCa-C-D DDEDCDE CaC-C-a EEFEDCE-DEa aCb-bbE-D-C-"
    # create a WAV file for the Cello suite intro with note duration 0.25s,
    # and then Twinkle Twinkle
    MakeSong(filename = "cello.wav", notes = cello, note_duration = 0.25)
    MakeSong("smoke.wav", smoke, 0.25)
    MakeSong("twinkle.wav", twinkle, 0.25)
    MakeSong("热爱105.wav", youWhoLove105c, 0.25)# This is the new song that I created 




  #Test of reverse_song
    song     = "abcde"
    result   = reverseSong(song)
    expected = "edcba"
    printTest(f"reverse_song({repr(song)})", result, expected)

    song2    = "accdeed"
    result2   = reverseSong(song2)
    expected2 = "deedcca"
    printTest(f"reverse_song({repr(song2)})", result2, expected2)

    song3    =  mary
    result3   = reverseSong(song3)
    expected3 = "cdeddeeeedcde gge ddd eeedcde"
    printTest(f"reverse_song({repr(song3)})", result3, expected3)

# Test of raiseOctave
    result4   =  raiseOctave(song)
    expected4 = "ABDCDE"
    printTest(f"raiseOctave({repr(song)})", result4, expected4)

    result5   = raiseOctave(song2)
    expected5  = "ACCDEED"
    printTest(f"raiseOctave({repr(song2)})", result5, expected5)

    result6   = raiseOctave(song3)
    expected6 = "EDCDEEE DDD EGG EDCDEEEEDDEDC"
    printTest(f"raiseOctave({repr(song3)})", result6, expected6 )

# Test of lowerOctave

    song8 ="ADFGAD"
    result_10 = lowerOctave(song8)
    expected_10 = "adfgad"
    printTest(f"lowerOctave({repr(song8)})", result_10, expected_10)

    song9 ="AADDFFGGCCB"
    result_11 = lowerOctave(song9)
    expected_11 = "aaddffggccb"
    printTest(f"lowerOctave({repr(song9)})", result_11, expected_11)


    song_10 ="AACCBCAGG"
    result_12= lowerOctave(song_10)
    expected_12="aaccbcagg"
    printTest(f"lowerOctave({repr(song_10)})", result_12, expected_12)

# Test of raiseOctavePart
    song5 = "ABcdeFG"
    result7= raiseOctavePart(song5, 2, 4)
    expected7 = "ABCDEFG"
    printTest(f"raiseOctavePart({repr(song5)}, 2, 4)", result7, expected7)

    song6 = "ADbfG"
    result8 = raiseOctavePart(song6, 2, 3)
    expected8 = "ADBFG"
    printTest(f"raiseOctavePart({repr(song6)}, 2, 3)", result8, expected8)

    song7 = "adfgecCC"
    result9 = raiseOctavePart(song7, 0, 5)
    expected9 = "ADFGECCC"
    printTest(f"raiseOctavePart({repr(song7)}, 0, 5)", result9, expected9)



# Test of lowerOctavePart
    song8 ="adeDEFFa"
    result_13 = lowerOctavePart(song8, 3, 6)
    expected_13 ="adedeffa"
    printTest(f"lowerOctavePart({repr(song8)}, 3, 6)", result_13, expected_13)

    song9 = "adebbBBDde"
    result_14 = lowerOctavePart(song9, 5, 7)
    expected_14 = "adebbbbdde"
    printTest(f"lowerOctavePart({repr(song9)}, 5, 7)", result_14, expected_14)


    song10 = "aACCCFGg"
    result_15 = lowerOctavePart(song10, 1, 6)
    expected_15 = "aacccfgg"
    printTest(f"lowerOctavePart({repr(song10)}, 1, 6)", result_15, expected_15)



# Test of randomsong
    random.seed(2345678)
    randomS=randomsong(mary, 2, 5)
    expected_s= "geede"
    printTest(f"randomsong({repr(mary)},2, 5)", randomS, expected_s)

    random.seed(2345678)
    randomS_2 = randomsong(youWhoLove105c, 3, 10)
    expected_s2= "C-D- CaEE"
    printTest(f"randomsong({repr(youWhoLove105c)},3, 10)", randomS_2, expected_s2)

    random.seed(2345678)
    randomS_3 =randomsong(cello, 3, 20)
    expected_s3= "CcacFCFDgFEDEgaEFCcE"
    printTest(f"randomsong({repr(cello)}), 3, 20", randomS_3, expected_s3)

main()
