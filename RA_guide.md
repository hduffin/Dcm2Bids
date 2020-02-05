## Step by step process to BIDs-ifying data and validating that it worked
 
 
**Some notes before you start. These are the variables you'll need to change in order to run each script**



| Variable   | Definition     |  Example  |
|----|:-----:|-------------:|
| ${sub} | This is the subject ID. This will change depending on what subject you're working on, this will always be in the form INET###. Please note that sometimes you'll have to put quotation marks around the subject. | INET001| INET001|
| ${ses} | This is the session. This will change depending on what session you're working with, this will always be in the form of a number 1, 2, 3. Please note that sometimes you'll have to put quotation marks around the session. | 1 |
|${dcm_dir} | This is the directory that has all the raw dicoms for that particular subject and session. If the files doesn't exist in the box directory you'll need to download it from Nunda and unzip the folder. The format of each folder provides the subject ID followed by the session. In the example provided we are working with INET001 session 1 | ~/Box/DATA/iNetworks/BIDS/DICOM/sub-INET001/INET001_1/SCANS |

* Open the terminal and go to the iNetworks directory
  * ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti ```
* Check the QC sheet to see what subjects are not yet BIDs-ified, determine if any new folders need to be downloaded and unzipped from Nunda then run the following code to BIDs raw dcms to a bids nifti version. 
  * ``` dcm2bids -d ${dcm_dir} -p ${sub} -s ${ses} -c ~/Box/DATA/iNetworks/BIDS/Nifti/.bidsignore/config.json --clobber ```
  * ex ``` dcm2bids -d ~/Box/DATA/iNetworks/BIDS/DICOM/sub-INET001/INET001_1/SCANS -p INET001 -s 1 -c ~/Box/DATA/iNetworks/BIDS/Nifti/.bidsignore/config.json --clobber ```
  * this will take awhile to process all your files and turn them into nifti's
 * Fix the fieldmaps, the current pipeline dcm2bids does not account for a fieldmap to apply to multiple runs therefore to account for this you'll need to run this script. You have to feed them as strings, you don't need to list the sub or ses parts the script takes care of that 
  * change directories to the folder with the python script
  * ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti/.bidsignore ```
  *  ``` python -c "execfile('fix_jsons.py');fix_jsons('${sub}','${ses}')"```
  **Please note here that the ${sub} and ${ses} need to be in 'quotes'**
  * ex  ``` python -c "execfile('fix_jsons.py');fix_jsons('INET001','1')"```
* Once complete you should see if the Nifti folder passes the bids validator 
  * http://bids-standard.github.io/bids-validator/
  * If there are errors read over the bids documentation to see what exactly is problematic and open the files 
  * Make notes of this in the QC doc 
* Now you'll need to deface anatomical images so everything can go onto Quest --only necessary for T1 images which are only taken during **session 3**
  * ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti/${sub}/ses-3/anat ```
  * ``` pydeface ${sub}_ses-3_acq-RMS_T1w.nii.gz --outfile ${sub}_ses-3_acq-RMS_T1w.nii.gz --force ```
  * ex ``` pydeface sub-INET001_ses-3_acq-RMS_T1w.nii.gz --outfile sub-INET001_ses-3_acq-RMS_T1w.nii.gz --force ```
  * the name should be the exact same so it overwrites the current file to the defaced one
* Once complete make sure the now defaced data passes the bids validator
  * http://bids-standard.github.io/bids-validator/
* Open the file using afni to see if the anatomical is truly defaced 
  * ``` afni ```
  * if everything worked you should see a brain image without a face on it 
