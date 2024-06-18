#!/usr/bin/env python
# coding: utf-8

# # Phone Scraper

# In[5]:


pdf = """EXAMPLE PHONE AND EMAIL
DIRECTORY
This example PDF was created to practice writing programs that could automatically get phone numbers
and email addresses from PDFs.
You can learn to program with the free resources at https://inventwithpython.com
PUBLIC DOMAIN IMAGE OF THE SEAL OF APPROVAL
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."
Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com 724-900-2986
Rayford Sutton rayfords66@hotmail.com 242-391-3183
Jerome Gentry jgentry@me.com 604-720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
Quinton Franks qfranks@comcast.net 209-754-9111
Adam Hubbard cygzfjd61@outlook.com 641-433-6698
Jarred Fox jfox39@live.com 701-528-9851
Arnoldo Parker aparker39@sbcglobal.net 304-491-9583
Sid Mcdaniel mcdanie3354@att.net 863-583-8107
Raymon Combs uqcwsntti71@att.net 507-948-3980
Ervin Francis efrancis@optonline.net 546-367-3454
Gilberto Austin austi363@optonline.net 321-854-5616
Lino Barlow lbarlow22@me.com 904-896-2920
Stacey Shepherd sshepherd61@sbcglobal.net 309-387-1990
Roscoe Terry rterry64@outlook.com 605-373-2329
Eddie Meadows eddiem89@yahoo.com 573-454-1209
Carlos Simpson csimpson8@verizon.net 252-822-2439
Jerome Manning jmanning54@optonline.net 586-481-1805
Hong Erickson herickson3@me.com 615-716-5379"""


# In[6]:


import re 
Phoneregex = re.compile(
r'''
(
((\d\d\d) | (\(\d\d\d\)))?    # Optional area code: can be 123 or (123)
(\s|-)?                       # Optional separator: space or dash
\d\d\d                        # First 3 digits of the phone number
-                             # Separator: dash
\d\d\d\d                      # Last 4 digits of the phone number
(((ext(\.)?\s) | x)          # Optional extension prefix: ext, ext., or x
(\d{2,5}))?                   # Optional extension number: 2 to 5 digits
)
''', re.VERBOSE)


# In[7]:


phoneNumbers = Phoneregex.findall(pdf)

allPhoneNumbers = []
for Number in phoneNumbers:
    allPhoneNumbers.append(Number[0])
    
allPhoneNumbers


# # Email Scraper

# In[8]:


import re 

emailregex = re.compile(
    r'''
    [a-zA-Z0-9_.+]+  #name
    @                #symbol
    [a-zA-Z0-9_.+]+  #domain name part
    ''', re.VERBOSE)


# In[9]:


allemails = emailregex.findall(pdf)
print(allemails)

