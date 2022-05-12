# Main def for scrapping
import schedule
from HTML_scrape import bots


# This will run all of the files
def HTML_scraping():

    # change this to daily
    schedule.every(5).seconds.do(bots.Colorado_bot)
    #schedule.every(5).seconds.do(bots.California_bot)
    # button to stop running the program    
    bots.run_continuously()
    #stop_run_continously = run_continuously()
    return

# Need to add, if schedule happens then do something with the newest file
Colorado_folder = "D:\Python\WebScraper\Colorado"
Colorado_time = "12:27"
# finding the newest file

if __name__ == "__main__":
    HTML_scraping()
'''
list_of_files = glob.glob('path to folder')
latest_file = max(list_of_files, key = os.path.getctime)
print(latest_file)
'''
