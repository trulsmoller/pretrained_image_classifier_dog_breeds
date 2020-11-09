#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: Truls Møller
# DATE CREATED: 5-Nov-2020
# REVISED DATE:
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best'
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the
#          how to calculate the counts and percentages for this function.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics
#          (either a percentage or a count) where the key is the statistic's
#           name (starting with 'pct' for percentage or 'n' for count) and value
#          is the statistic's value.  This dictionary should contain the
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##

import numpy as np

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """

    # Extracting lists of values from results_dic

    # Value 1 for 'list_ind2' means the image is classified correctly
    # regardsless of what it is. Could be breed of dog, could be cat, etc.
    list_ind2 = [item[2] for item in results_dic.values()]

    # Value 1 for 'list_ind3' means the image is actually a dog based on the label
    list_ind3 = [item[3] for item in results_dic.values()]

    # Value 1 for 'list_ind4' means the image is classified as a dog.
    list_ind4 = [item[4] for item in results_dic.values()]

    # Initializing results_stats_dic
    results_stats_dic = dict()

    # Adding the following keys to the results_stats_dic:

    # n_images - number of images
    n_images = len(results_dic)
    results_stats_dic['n_images'] = n_images

    # n_dogs_img - number of dog images
    results_stats_dic['n_dogs_img'] = sum(list_ind3)

    # n_notdogs_img - number of NON-dog images
    results_stats_dic['n_notdogs_img'] = n_images - results_stats_dic['n_dogs_img']

    # n_match - number of matches between pet & classifier labels
    results_stats_dic['n_match'] = sum(list_ind2)

    # n_correct_dogs - number of correctly classified dog images. This needs
    # a value of 1 on both index 3 and 4.
    results_stats_dic['n_correct_dogs'] = np.sum(np.array(list_ind3) * np.array(list_ind4))

    # n_correct_notdogs - number of correctly classified NON-dog images. This needs
    # a value of 0 on both index 3 and 4.
    results_stats_dic['n_correct_notdogs'] = np.sum((1 - np.array(list_ind3)) * (1 - np.array(list_ind4)))

    # n_correct_breed - number of correctly classified dog breeds. This needs
    # a value of 1 on both index 2 and 3.
    results_stats_dic['n_correct_breed'] = np.sum(np.array(list_ind2) * np.array(list_ind3))

    # pct_match - percentage of correct matches
    results_stats_dic['pct_match'] = 100*(results_stats_dic['n_match'] / n_images)

    # pct_correct_dogs - percentage of correctly classified dogs
    results_stats_dic['pct_correct_dogs'] = 100*(results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'])

    # pct_correct_breed - percentage of correctly classified dog breeds
    results_stats_dic['pct_correct_breed'] = 100*(results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img'])

    # pct_correct_notdogs - percentage of correctly classified NON-dogs
    results_stats_dic['pct_correct_notdogs'] = 100*(results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'])


    return results_stats_dic
