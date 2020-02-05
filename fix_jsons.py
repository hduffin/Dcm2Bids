#!/usr/bin/env python
# coding: utf-8

# In[51]:


if __name__ == "__main__":
    def fix_jsons(sub='sub', ses='ses'):
        import json
        import os 
        import fnmatch
        with open ('~/Box/DATA/iNetworks/BIDS/Nifti/sub-' +sub+ '/ses-' +ses+ '/fmap/sub-' +sub+ '_ses-' +ses+ '_phasediff.json') as write_file:
            j_data = json.load(write_file)
            def find_files(base, pattern):
    #Return list of files matching pattern in base folder.
                return [n for n in fnmatch.filter(os.listdir(base), pattern) if
                    os.path.isfile(os.path.join(base, n))]

            nii_files = find_files('~/Box/DATA/iNetworks/BIDS/Nifti/sub-' +sub+ '/ses-' +ses+ '/func', '*.nii.gz')
        #add the extra subfolder info
            files=[]
            for i in nii_files:
                fname= "ses-" +ses+ "/func/"
                files.append(os.path.join(fname,i))
            j_data['IntendedFor']=files
        with open('~/Box/DATA/iNetworks/BIDS/Nifti/sub-' +sub+ '/ses-' +ses+ '/fmap/sub-' +sub+ '_ses-' +ses+ '_phasediff.json', 'w') as f:
            json.dump(j_data, f, indent=4, sort_keys=True)
        
#in command line write python -c "execfile('fix_jsons.py');fix_jsons('SUBID',SES)"


# In[ ]:




