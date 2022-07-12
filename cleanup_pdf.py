'''
created this to clean up a 400 page pdf at work and could 
not think of a faster way to do it acrobat or bluebeam,
basically just needed to remove two images from each page and two
links for each pagenot my best work, but maybe my fastest
'''

#try and except was for pages that did not have the buttons or links


import pikepdf
from tqdm import tqdm
file = 'lol'
pdf = pikepdf.open(file)

# removes rando buttons
for page in tqdm(pdf.pages):
    for item in page.Resources.XObject:
        try:
            if page.Resources.XObject[item]['/Height'] == 103 or page.Resources.XObject[item]['/Height'] == 101:
                del page.Resources.XObject[item]
        except:
            pass

# removes urls from button images that were removed in the code above
for page in pdf.pages:
        try:
            for num, item in enumerate(page['/Annots']):
                stuff = item['/A']['/URI']
               
                if 'sowl' in str(stuff):
                    del page['/Annots'][num]
                    del page['/Annots'][num]
                    pass
        except:
            pass
         
            

pdf.save('save.pdf')
