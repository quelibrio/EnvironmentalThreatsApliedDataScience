import csv
import urllib2
import sys
import requests

root = 'http://environment.data.gov.uk/'
where = 'flood-monitoring/data/'
start_date = '2017-03-12'
end_date = '2017-03-14'

#url = 'http://environment.data.gov.uk/flood-monitoring/data/readings.csv?date=' + start_date + "&_view=full"
url = root + where + 'readings.csv?startdate=' + start_date + '&enddate=' + end_date + "&_view=full"

with requests.Session() as s:
    print 'downloading...'
    download = s.get(url)

    print 'decoding...'
    decoded_content = download.content.decode('utf-8')

    print 'reading csv...'
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

#output_filename = 'full_' + start_date + '.csv'
output_filename = 'full_' + start_date + '_' + end_date + '.csv'
print 'writing...'
with open(output_filename, "wb") as f:
    writer = csv.writer(f)
    writer.writerows(my_list)
