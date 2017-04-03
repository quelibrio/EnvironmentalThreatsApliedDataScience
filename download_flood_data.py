import csv
import urllib2
import sys

root = 'http://environment.data.gov.uk/'
where = 'flood-monitoring/data/'
start_date = '2017-03-12'
end_date = '2017-03-14'
#url = 'http://environment.data.gov.uk/flood-monitoring/data/readings.csv?date=' + start_date + "&_view=full"
url = root + where + 'readings.csv?startdate=' + start_date + '&enddate=' + end_date + "&_view=full"


response = urllib2.urlopen(url)
reader = csv.reader(response)
#o_file = open('full_' + start_date + '.csv', "wb")
o_file = open('full_' + start_date + '_' + end_date + '.csv', "wb")
writer = csv.writer(o_file)

for row in reader:
    writer.writerow(row)

o_file.close()
print 'done'
