# Pre-trained Image Classifier for identifying dog breeds
## by Truls Møller

### Date created
2020-11-05

## Summary
As part of Udacity's AI Programming with Python Nanodegree program, I have
completed this mini-project where I used a Pre-trained Image Classifier to
identify dog breeds from picture files.

For the image classification task I used an image classification application
using the deep learning model convolutional neural network (CNN). CNNs work
particularly well for detecting features in images like colors, textures, and
edges; then using these features to identify objects in the images. I used a CNN
that had already learned the features from a giant dataset of 1.2 million images
called ImageNet. There are different types of CNNs that have different
structures (architectures) that work better or worse depending on your criteria.
With this project I explored three different architectures (AlexNet, VGG, and
ResNet) and determined which is best for the application.

## Files
- imagenet1000_clsid_to_human.txt - A sample of 1000 image labels from ImageNet.
- pet_images - folder with 40 .jpg picture files of mainly dogs, but also some
other animals. (Labels extracted from the file names)
- classifier.py - based on pytorch. Provided by Udacity for use in the project.
- test_classifier.py - Provdided by Udacity for use in the project. To
demonstrate the proper usage of the classifier() function that is defined in
classifier.py This function uses CNN model architecture that has been pretrained
on the ImageNet data to classify images. The only model architectures that this
function will accept are: 'resnet', 'alexnet', and 'vgg'
- print_functions_for_lab_checks.py - Provided by Udacity for use in the
project. Set of functions I used to check my code after programming each
function in the remaining files on this list starting with check_images.py.
- check_images.py. Contains main program function, which times the runtime.
- get_input_args.py. Contains function check_command_line_arguments(), which
prints an overview of the arguments
- get_pet_labels.py. Contains function get_pet_labels(), which creates results
dictionary that contains the results from get_pet_labels function
- classify_images.py. Contains function classify_images(), which creates
Classifier Labels with classifier function, Compares Labels, and adds these
results to the results dictionary
- adjust_results4_isadog.py. Contains function adjust_results4_isadog(), which
adjusts the results dictionary to determine if classifier correctly classified
images as 'a dog' or 'not a dog'. This demonstrates if model can correctly
classify dog images as dogs (regardless of breed).
- calculates_results_stats.py. Contains function calculates_results_stats(),
which calculates the results of run and puts statistics in the Results
Statistics Dictionary - called results_stats
- print_results.py. Contains function print_results, which prints summary
results, incorrect classifications of dogs (if requested) and incorrectly
classified breeds (if requested).

When run the program generates a text report for each architecture. The output
files will be:
- alexnet_pet-images.txt
- resnet_pet-images.txt
- vgg_pet-images.txt


## Running the app from the command line

sh run_models_batch.sh

This generates three reports, one for each CNN. Example: Alexnet. The report includes the following:

Results Summary for CNN Model Architecture ALEXNET
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10

pct_match           : 75.00
pct_correct_dogs    : 100.00
pct_correct_breed   : 80.00
pct_correct_notdogs : 100.00

Total Elapsed Runtime: 0:0:2

## Conclusion

The best method is the VGG with 87.5 percent matches. Resnet 82.5 percent.
Alexnet 75 percent. However the VGG is by far the slowest in terms of run time.
Hence which is betterdepends on the volume of image files to process and what is
considered an acceptable runtime.
