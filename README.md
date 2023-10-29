# app-average-erp

Brainlife App to create an Evoked data structure, given an Epochs object and conditions to use for averaging.

1) Input file is: 
    * `fname` data file for the Epochs object
2) Input string is:
    * 'stimulus names' list of strings, each string is one of the stimulus names to use for averaging
    * 'condition' a string to use for the condition name in the Evoked object
3) Input boolean is:
    * 'average all' if true, average all epochs in the Epochs object, regardless of the stimulus name

4) Ouput files are:
    * `ave/fif`
    * HTML report
    * Figure of the evoked data


## Authors
- Kamilya Salibayeva (ksalibay@iu.edu)
