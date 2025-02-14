-> This Pytest POM framework is used to maintain the testcase for "https://www.douglas.de/de"
-> It will be read the data file form test_data.xlsx file and apply the filer on perfume file(In progress)
-> After expectation, Framework will generate the report


Folder Structure



Pages-> This folder contains the locator and function for the pages as per POM
    1) Base_page.cy-> This page is used to contain the information about the base page 
  2) home_page.cy-> This page is used to contain the information of the home page
  3) purfume_page.cy-> This page is used to contain the information of the locator page
  



Test_data-> This folder contains the data which are used to in the project 
   1) Test_data.xlsx-> This file is used to maintain the data of filers
   
   
Tests-> This folder is used to maintain the all testcase of the Framework
   1) test_perfume_fielter.py-> This file is used to perform test case
  



Utils-> This file is used to maintain the utility that is used for the entire framework  
   1) Config.py-> This file is used to serve the configuration of the project 
   2) confiest.py-> This file is used to setup the webdirver 
   3) excel_reader.py-> This file is used to read the excel 
   4) loger.py-> This file is used to generate the log
   5) screenshot.py-> This file is used to take a screenshot
  
