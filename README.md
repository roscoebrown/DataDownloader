# DataDownloader

The Data downloader is the main program for collected permit data and location data.


# State List


### Texas
Bought the data from the state
you have the info already on how to move forward with a subscription to their FTP
link {Texas}

### Oklahoma 
Already have the data
The link takes you to the oil and gas file directory. Scroll down until “line 10” with the title “W17daily”.zip, Intent to Drill past 7 days. This downloads a zipped csv file that is updated daily.

### Colorado
Have some of the data

### Lousiana
This is the Lousiana Permit data with longitude and latitude coordinates. Louisiana does do a data service for this data for $300. 
However, this data can be downloaded for free manually in an excel file.

### North Dakota 
The link in the PDF takes you to the ND DMR website. At the top of the table on the left, you need to fill out the subscription form for the premium version ($175/yr has the most data, or if you want $50 for the basic and just has permits in XLS). This is updated daily at 5am in the well index. Once you subscribe, you go back to the DMR website, Click the left hand link for “Well Index”, login, and it will provide a link for the excel file where we then sort by descending dates to get the days approved permits.

 
### New Mexico 
The top link titled “NMODC” takes you to the permitting website. Once on the site, click the weekly Well Activity Link. Once there, click the “Excel” link in the top left hand corner to get the excel version of this report. The 2nd link titled “Public FTP” takes you directly to their FTP folder that is updated with different datasets occasionally.


### Alaska 
- Link takes you directly to the permit search field where it will populate the current month search (stored in cookies). Clicking the blue button downloads a zipped csv file of what’s shown in the table.


### Colorado 
- Link directly to Permit search page. Near the bottom, click the “Go” button under “Approved Permits Last 12 Months” - Permits to Drill (Form 2A). It will take a second for this to load, once it does, click the purple floppy disk with green arrow button revealing a drop down list and download a CSV file or any file type of your choice.

 
### California 
- FTP Server link. Click 2019 - then sort by last modified and download the latest excel file of approved permits.

 
### Wyoming 
The link takes you to the search field where you have to type in the dates, select “All Permitted Wells”, Check the box, then click Go Find. It will download a CSV file, then sort column W (Status_Dte) descending 

 
### Louisiana 
After paying the initial fee and monthly fee and request “WELL” data, they will provide you with a login. From there you can click the link in step 6 - How do I Automate the download process? and will walk you through setting up the script.
 

### Utah 
called Dave Doucette to try and get a hold of the PDF/Excel file of all approved permits. Otherwise, the link takes you to the search page of approved drilling permits. You have to chose in the drop down box, “BETWEEN” and format the search like this “06/01/2019,06/30/2019”. Then click the print buttons at the top of the search field section to get a CSV file.
 

### Kansas 
Link takes you to the O&G data page. Scroll to the bottom with the last table titled ASCII & Zipped Files Containing Well Data. Click the “Select Wells” button in the 2nd option down titled “Wells Permitted In…” and make sure the correct month is selected. This populates a table and then click save to file at the top (blue button). 

 
### Ohio
Brings you to the search field have to enter date and select permit in the “Plug or permit dropdown”. Talked with the state again and the most efficient way to get daily permit information is this way. Once loaded, click the purple floppy icon with green arrow and download xls or csv file.

 
### Montana
Montana does not have a great system in place for looking up data. Make sure the dropdown lists show Dt Effective and Prior To. Search in the format 07/01/2019 or whatever month is ahead of the current date. Sort by descending date effective and then click the excel button at the top right corner to download.

 
### Mississippi
Only have weekly PDFs not very much activity here (1 per week).

 
### West Virginia 
Link takes you directly to the WV DEP weekly update page. Towards the bottom of the page you will find a series of dates and links titled “Dates: 06-10-2019 thru 06-14-2019”. Clicking the most recent date range link will download a zipped folder with an xls file of most recent approved permits


### Offshore 
waiting for a call back from IT to get a refreshable csv/xls file to work with. Said you have to buy it on a daily basis which sounded expensive. Otherwise you would have to use the search feature in the Data Center on a daily basis but I know you don’t necessarily want to do it that way. The Data Center has a lot of information that could be automatically pulled and is a good resource on its own.


<br />

### Dictionary Example "$myDict := dict "name1" "name2""
[Texas]: http://www.rrc.state.tx.us/
