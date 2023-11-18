Name: Charan Sai Chintha
Stevens login:

GITHUB URL: https://github.com/Charansaichintha/charan-sai-project-1-stevens/tree/main

No. of hours spent on project = time spent on Problem Statement Analysis + Development Phase hours + Testing and Bug removal
Total Time = 40 mins + (2.5hrs+ 2.5hrs+ 3o min)  + 2hr = 8hr 10 min

Testing of Code : The code was tested by providing the sample data provided in the instruction. Each code was fed with sample data input and tested and updated till it matches the expected output. 

Bugs that couldn't be resolved :
    gron command is not able to print file name as parent json object properly.

Bugs that were resolved
    gron.py program was earlier not able to print parent dictionary, to resolve this program was redesigned to keep track of parent dictionary and append it to current one.

Extensions
1. To add support of multiple files input in wc program : the script can be used with multiple file paths, and it will display the line, word, and character counts for each file, followed by the total counts if more than one file is provided. The script takes multiple file names as command line argument.
2. To add support of different flags with wc command : User can use flags -l, -w, and -c  or combine them to get only the specific information likewise lines, word or only characters. These flags are taken input as command line argument by script and then output based on these only.
3. To add support for an --obj flag that allows specifying a different base object for gron program : the script uses argparse module to handle the --obj flag and use it as base object.

