# DataDownloader

The Data downloader is the main program for collected permit data and location data. <br />
<br />
What is this project trying to acheive? <br />
<br />
The goal of the DataDownloader project is to automatically download permit and location data from state websites. <br />
Then automatically organize and upload to the Gibson Reports AWS server. Each of the branches hold a component of the project. <br />
As of right now I have finished the automatic data download and transfer to csv. files from their respective state websites.


# State List

### Alabama
link: [Alabama]

### Alaska 
<br />
Note<br />
Link takes you directly to the permit search field where it will populate the current month search (stored in cookies). Clicking the blue button downloads a zipped csv file of what’s shown in the table. <br />
link: [Alaska]

### Arizona
link: [Arizona]

### Arkansas
link: [Arkansas] 
  
### California 
California_bot complete <br />
FTP Server link. Click 2019 - then sort by last modified and download the latest excel file of approved permits. <br />
link: [California]

### Colorado 
Colorado_bot complete <br />
Note<br />
Link directly to Permit search page. Near the bottom, click the “Go” button under “Approved Permits Last 12 Months” - Permits to Drill (Form 2A). It will take a second for this to load, once it does, click the purple floppy disk with green arrow button revealing a drop down list and download a CSV file or any file type of your choice.<br />
link: [Colorado]

### Connecticut
N/A

### Delaware
N/A

### Florida
N/A

### Georgia
N/A

### Hawaii
N/A

### Idaho
link: [Idaho]

### Illinois
link: [Illinois]

### Indiana
link: [Indiana]

### Iowa
link: [Iowa]

### Kansas 
<br />
Link takes you to the O&G data page. Scroll to the bottom with the last table titled ASCII & Zipped Files Containing Well Data. Click the “Select Wells” button in the 2nd option down titled “Wells Permitted In…” and make sure the correct month is selected. This populates a table and then click save to file at the top (blue button). <br />
link: [Kansas]

### Kentucky
link: [Kentucky]

### Louisiana
Louisiana_bot is in progress will complete after setting SQL code<br />
This is the Lousiana Permit data with longitude and latitude coordinates. Louisiana does do a data service for this data for $300. 
However, this data can be downloaded for free manually in an excel file. <br />
After paying the initial fee and monthly fee and request “WELL” data, they will provide you with a login. From there you can click the link in step 6 - How do I Automate the download process? and will walk you through setting up the script.<br />
link: [Louisiana]

### Maine
N/A

### Maryland
N/A

### Massachusetts
N/A

### Michigan
link: [Michigan]

### Minnesota
N/A

### Mississippi
<br />
Only have weekly PDFs not very much activity here (1 per week).<br />
link: [Mississippi]

### Missouri
link: [Missouri]

### Montana
<br />
Montana does not have a great system in place for looking up data. Make sure the dropdown lists show Dt Effective and Prior To. Search in the format 07/01/2019 or whatever month is ahead of the current date. Sort by descending date effective and then click the excel button at the top right corner to download.<br />
link: [Montana]

### Nebraska
link: [Nebraska]

### Nevada
link: [Nevada]

### New Hampshire
N/A

### New Jersey
N/A

### New Mexico 
<br />
The top link titled “NMODC” takes you to the permitting website. Once on the site, click the weekly Well Activity Link. Once there, click the “Excel” link in the top left hand corner to get the excel version of this report. The 2nd link titled “Public FTP” takes you directly to their FTP folder that is updated with different datasets occasionally.<br />
link: [New Mexico]

### New York
link: [New York]

### North Carolina
N/A

### North Dakota 
<br />
The link in the PDF takes you to the ND DMR website. At the top of the table on the left, you need to fill out the subscription form for the premium version ($175/yr has the most data, or if you want $50 for the basic and just has permits in XLS). This is updated daily at 5am in the well index. Once you subscribe, you go back to the DMR website, Click the left hand link for “Well Index”, login, and it will provide a link for the excel file where we then sort by descending dates to get the days approved permits.<br />
link: [North Dakota]

### Ohio
<br />
Brings you to the search field have to enter date and select permit in the “Plug or permit dropdown”. Talked with the state again and the most efficient way to get daily permit information is this way. Once loaded, click the purple floppy icon with green arrow and download xls or csv file.<br />
link: [Ohio]

### Oklahoma 
<br />
The link takes you to the oil and gas file directory. Scroll down until “line 10” with the title “W17daily”.zip, Intent to Drill past 7 days. This downloads a zipped csv file that is updated daily.<br />
link: [Oklahoma]

### Oregon
N/A

### Pennsylvania
N/A

### Rhode Island
N/A

### South Carolina
N/A

### South Dakota
link: [South Dakota]

### Tennessee
N/A

### Texas
<br />
Bought the data from the state
you have the info already on how to move forward with a subscription to their FTP<br />
link [Texas]

### Utah 
<br />
called Dave Doucette to try and get a hold of the PDF/Excel file of all approved permits. Otherwise, the link takes you to the search page of approved drilling permits. You have to chose in the drop down box, “BETWEEN” and format the search like this “06/01/2019,06/30/2019”. Then click the print buttons at the top of the search field section to get a CSV file.<br />
link: [Utah]

### Vermont
N/A

### Virginia
N/A

### Washington
link: [Washington]

### West Virginia 
<br />
Link takes you directly to the WV DEP weekly update page. Towards the bottom of the page you will find a series of dates and links titled “Dates: 06-10-2019 thru 06-14-2019”. Clicking the most recent date range link will download a zipped folder with an xls file of most recent approved permits<br />
Link: Need to get

### Wisconsin
N/A

### Wyoming 
<br />
The link takes you to the search field where you have to type in the dates, select “All Permitted Wells”, Check the box, then click Go Find. It will download a CSV file, then sort column W (Status_Dte) descending <br />
link: [Wyoming]

### Offshore 
waiting for a call back from IT to get a refreshable csv/xls file to work with. Said you have to buy it on a daily basis which sounded expensive. Otherwise you would have to use the search feature in the Data Center on a daily basis but I know you don’t necessarily want to do it that way. The Data Center has a lot of information that could be automatically pulled and is a good resource on its own.


<br />

### Dictionary Example "$myDict := dict "name1" "name2""
[Alabama]: http://www.gsa.state.al.us/
[Alaska]: https://commerce.alaska.gov/web/aogcc
[Arizona]: http://www.azogcc.az.gov/
[Arkansas]: http://www.aogc.state.ar.us/Pages/Default.aspx
##### Change this one
[California]: https://www.conservation.ca.gov/ 
[Colorado]: https://cogcc.state.co.us/#/home
[Idaho]: http://www.idahogeology.org/
[Illinois]: http://www.isgs.illinois.edu/iloil
[Indiana]: https://igs.indiana.edu/pdms/
[Iowa]: http://www.iowadnr.gov/Environment/GeologyMapping.aspx
[Kansas]: http://www.kgs.ku.edu/Magellan/Qualified/index.html
[Kentucky]: https://www.uky.edu/KGS/emsweb/
[Louisiana]: http://www.sonris.com/
[Michigan]: http://www.deq.state.mi.us/dataminer/
[Mississippi]: https://www.ogb.state.ms.us/
[Missouri]: http://dnr.mo.gov/geology/geosrv/ogc/index.html
[Montana]: http://bogc.dnrc.mt.gov/onlinedata.asp
[Nebraska]: http://www.nogcc.ne.gov/
[Nevada]: http://minerals.nv.gov/
[New Mexico]: http://www.emnrd.state.nm.us/ocd/
[New York]: http://www.dec.ny.gov/cfmx/extapps/GasOil/
[North Dakota]: https://www.dmr.nd.gov/oilgas/
[Ohio]: http://oilandgas.ohiodnr.gov/well-information/oil-gas-well-database
[Oklahoma]: http://www.occeweb.com/Orawebapps/OCCORaWebAppsone.html
[Oregon]: http://www.oregongeology.org/mlrr/oilgas-logs.htm
[South Dakota]: http://denr.sd.gov/des/og/welldata.aspx
[Texas]: http://www.rrc.state.tx.us/
[Utah]: https://oilgas.ogm.utah.gov/oilgasweb/live-data-search/lds-main.xhtml
[Washington]: http://www.dnr.wa.gov/programs-and-services/geology/energy-mining-and-minerals/oil-and-gas-resources
[Wyoming]: http://wogcc.state.wy.us/






