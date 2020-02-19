## Step by step process to BIDs-ifying data and validating that it worked
 
 
**Some notes before you start. These are the variables you'll need to change in order to run each script**



| Variable   | Definition     |  Example  |
|----|:-----:|-------------:|
| ${sub} | This is the subject ID. This will change depending on what subject you're working on, this will always be in the form INET###. Please note that sometimes you'll have to put quotation marks around the subject. | INET001| INET001|
| ${ses} | This is the session. This will change depending on what session you're working with, this will always be in the form of a number 1, 2, 3. Please note that sometimes you'll have to put quotation marks around the session. | 1 |


  **Follow along using the QC sheet**
  
  ### Downloaded
  * Download the files off of Nunda, DO NOT UNZIP
  
  ### iNet2BIDS_all
  * Open the terminal type in the following
  
  
   ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti/.bidsignore ```
   
   
  * Run the following **change based on your subject and session**
  
  
  ``` ./iNet2BIDS_all ${sub} ${ses} ```
  
  
  ex
  
  
   ``` ./iNet2BIDS_all INET001 1 ```
   
   
 * Fill out the QC sheet with the number 1 to indicate the script is running
 ## After the script is complete go through this verification process 
 ### fix_jsons
* Verify the script worked, go to the json website and select the phase diff json file in the fmap folder, look for the section IntendedFor. This should have a list of paths of all the functional scans 
* https://jsoneditoronline.org/
* ex "IntendedFor": [
        "ses-3/func/sub-INET001_ses-3_task-rest_run-05_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-mixed_run-02_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-ambiguity_run-02_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-mixed_run-01_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-ambiguity_run-01_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-03_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-06_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-08_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-01_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-slowreveal_run-02_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-04_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-slowreveal_run-01_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-07_bold.nii.gz", 
        "ses-3/func/sub-INET001_ses-3_task-rest_run-02_bold.nii.gz"
    ]
### pydeface
* Verify the anatomicals were defaced
* Open the terminal and go to the anat folder


``` cd ~/Box/DATA/iNetworks/BIDS/Nifti/sub-${sub}/${ses}/anat ```


ex


  ``` cd ~/Box/DATA/iNetworks/BIDS/Nifti/sub-INET001/ses-3/anat ```
  
  
  ``` afni ```
  
  Click overlay and then click T1
  
* This will open the afni program and show you the anatomical scan if one exists. The image should NOT have a face on it. 
  
### bids_valid
* Verify the script worked, open the subjects session in the Nifti folder it should look bids appropriate 
* Then go to this website and select the entire Nifti folder 
* http://bids-standard.github.io/bids-validator/
  
  
