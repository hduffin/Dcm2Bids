# A Guide to Using the BIDS Pipeline
Examples given are from the 5000 Scenes study

### Installations you will need
* Follow the instructions on the README.md for installing dcm2bids and the appropriate dependencies
* In order to use bids-validator, mriqc and fmriprep you will need to install docker (https://docs.docker.com/install/#supported-platforms) **be sure to follow post installation steps if using Ubuntu system**


* Check to see if mriqc works

`docker run -it poldracklab/mriqc:latest --version`
* Current version mriqc **v0.14.2** 
* Current version docker **18.06.1-ce**
* Install fmriprep

`pip install --user --upgrade fmriprep-docker`
* Current version fmriprep **v1.1.7**

**If you have issues with installation check neurostars.org**


### Now that you are up to date

You will need a config file in order for dcm2bids to organize your data into bids format bids2dcm has a helper tool that will give you information that you can use to create the appropriate config file. Over time you will likely have a central config file when running studies

**To use helper tool**


`dcm2bids_helper -d /home/toulmin/Documents/bid_conversion/DICOM_DIR/01_Unfilt_BOLD_CSI2_Sess-5_Run-1/02-
0001-000001.dcm [-o]`

**What your config file should look like**


{
    "descriptions": [
        {
            "dataType": "anat",
            "modalityLabel": "T2w",
            "criteria": {
                "SeriesDescription": "*T2*",
                "EchoTime": 0.1
            }
        },
        {
            "dataType": "func",
            "modalityLabel": "bold",
            "customLabels": "task-rest",
            "criteria": {
                "SidecarFilename": "006*"
            }
        }
    ]
}



Next you will want to create a skeleton of a bids appropriate folder


**To use tool**


`cd /PATH/TO/OUTPUT/DIR`
`dcm2bids_scaffold`

You will need to manually enter participant info in the participants.tsv (not required to be bids compliant)

Now you are ready to make your data bids compliant

**Make sure you are in your output dir before running**

`dcm2bids -d /home/toulmin/Documents/bid_conversion/DICOM_DIR/ -p 1 -s 5 -c 5000Sc_s1_ses4_config.json`

**The script does not provide task name within each dataset_description.json file you will need to add that in, you will also need to manually move the events.tsv and json files per task unless this is resting state data.** 
For an example visit http://bids.neuroimaging.io/bids_spec.pdf


Next you’ll want to run this through the bids validator app to ensure you’ve run successfully
http://incf.github.io/bids-validator/

You can also run bids validator through the terminal via docker
`docker run -ti --rm -v /path/to/data:/data:ro bids/validator /data`

Run mriqc


**You have to feed it the full directory**

`docker run -it --rm -v /home/toulmin/Documents/bid_conversion/5000scenes/:/data:ro -v /home/toulmin/Documents/bid_conversion/output-folder/:/out poldracklab/mriqc:latest /data /out participant `

**This will take awhile to run**

Run fmriprep

`docker run -ti --rm -v /Documents/bid_conversion/BIDS-examples-master/ds001:/data:ro -v /Documents/bid_conversion/fmri_prep_output:/out -v /usr/local/freesurfer/license.txt:/opt/freesurfer/license.txt poldracklab/fmriprep:latest /data /out/out participant --ignore fieldmaps`

or (recommended)

`fmriprep-docker /home/toulmin/Documents/bid_conversion/5000scenes/ /home/toulmin/Documents/bid_conversion/fmri_prep_output\ -w /home/toulmin/Documents/bid_conversion/scratch --fs-license-file /usr/local/freesurfer/license.txt  `


If you are running fieldmaps will need an "IntendedFor" section within json file in fmap dir. This can be added to the config file. If you run a subjects entire session of scans it will retroactively add the intended for directory so long as the config file specified the correct index placement of the functional scan. 










