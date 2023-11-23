#!/usr/bin/env python3

# Evoked is a datatype that contains the result of averaging an Epochs structure based on several criteria.
import mne
import json
import os
import os.path as op
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
import numpy as np
import matplotlib.pyplot as plt
import sys

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import mne


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the meg file
epochs = config.pop('fname')
# Read in the epochs file
epo = mne.read_epochs(epochs)

# Read the names of the stimuli and the name of the condition
stimuli = config.pop('stimulus_names')
stimuli = stimuli.split(',')
cond = config.pop('condition')
peaks = config.pop('peaks')

if peaks == 'None':
    peaks = 'auto'
else:
    peaks = peaks.split(',')
    peaks = [float(i) for i in peaks]

#Create the evoked object from epo at stimulus conditions
evo = epo[stimuli].average()

#Create figure of evoked response
fig = evo.plot_joint(title='Evoked response for condition '+cond, times = peaks)

report = mne.Report(title='Report')

#Add evoked to the report
report.add_evoked(evo, title='Evoked response for condition '+cond)

#Add figure of evoked response to the report
report.add_figs_to_section(fig, captions='Evoked response for condition '+cond)

# == SAVE REPORT ==
report.save(os.path.join('out_dir','report.html'))

# == SAVE FIGURE ==
fig.savefig(os.path.join('out_figs', 'evoked.png'))

 # == SAVE FILE ==
evo.save(os.path.join('out_dir', 'ave.fif'), overwrite=True)
