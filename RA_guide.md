## Step by step process to BIDs-ifying data and validating that it worked

*Will need to figure out if we can keep the scripts outside of .bidsignore otherwise will need to write outputs 
* Open the terminal and go to the directory iNetworks directory
  * ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti ```
* Check the QC sheet to see what subjects are not yet BIDs-ified, then run the following code to BIDs raw dcms to a bids nifti version, if the raw files are zipped you'll need to unzip 
  * ``` dcm2bids -d ${dcm_dir} -p ${sub} -s ${ses} -c config.json --clobber ```
  * ex ``` dcm2bids -d ~/Box/DATA/iNetworks/BIDS/DICOM/sub-INET001/INET001_1/SCANS -p INET001 -s 1 -c ~/Box/DATA/iNetworks/BIDS/Nifit/.bidsignore/config.json --clobber ```
  * this will take awhile to process all your files and turn them into nifti's
 * Fix the fieldmaps, the current pipeline dcm2bids does not account for a fieldmap to apply to multiple runs therefore to account for this you'll need to run this script. You have to feed them as strings, you don't need to list the sub or ses parts the script takes care of that 
  *  ``` python -c "execfile('fix_jsons.py');fix_jsons('SUBID','SES')"```
  * ex  ``` python -c "execfile('fix_jsons.py');fix_jsons('INET001','1')"```
* Once complete you should see if the Nifti folder passes the bids validator 
  * http://bids-standard.github.io/bids-validator/
  * If there are errors read over the bids documentation to see what exactly is problematic and open the files 
  * Make notes of this in the QC doc 
* Now you'll need to deface anatomical images so everything can go onto Quest --only necessary for T1 images
  * ``` cd ${bidsdir}/${sub}/${ses}/anat ```
  * ``` pydeface ${sub}_${ses}_acq-RMS_T1w.nii.gz --outfile ${sub}/${ses}_acq-RMS_T1w.nii.gz --force ```
  * ex ``` pydeface sub-INET001_ses-3_acq-RMS_T1w.nii.gz --outfile sub-INET001_ses-3_acq-RMS_T1w.nii.gz --force ```
  * the name should be the exact same so it overwrite the current file to the defaced one
* Once complete make sure the now defaced data passes the bids validator
* Open the file using afni to see if the anatomical is truly defaced 
  * ``` afni ```
  * if everything worked you should see a brain image without a face on it 
