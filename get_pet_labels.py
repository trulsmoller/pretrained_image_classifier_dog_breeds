#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Truls Møller
# DATE CREATED: 5-Nov-2020
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # initializing results dictionary
    results_dic = dict()

    # Creates list of files in directory
    in_files = listdir(image_dir)

    for idx in range(0, len(in_files), 1):

       # Skips file if starts with . (like .DS_Store of Mac OSX) because it
       # isn't an pet image file
       if in_files[idx][0] != ".":


           # Create temporary label variable to hold pet label name extracted

           # file name like 'Boston_Terrier_02259.jpg'
           file_name = in_files[idx]

           # get lower case file name with suffix removed and underscores replaced
           # like 'boston terrier 02259'
           pl = file_name.lower().split('.')[0].replace('_', ' ')

           # remove numeric part and strip to avoid whitespace at the end,
           # to achieve correct pet label like 'boston terrier'
           pet_label = ''.join([i for i in pl if not i.isdigit()]).strip()


           # If filename doesn't already exist in dictionary: adding it and its
           # pet label - otherwise: printing an error message because indicates
           # duplicate files (filenames)
           if in_files[idx] not in results_dic:

               results_dic[in_files[idx]] = [pet_label]

           else:
               print("** Warning: Duplicate files exist in directory:",
                     in_files[idx])


    return results_dic
