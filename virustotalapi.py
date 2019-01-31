import urllib
import urllib2
import json
import sys
hash_value = sys.argv[1]
vt_url = "https://www.virustotal.com/vtapi/v2/file/report"
api_key = "<update your api key here>"
parameters = {'apikey': api_key, 'resource': hash_value}
encoded_parameters = urllib.urlencode(parameters)
request = urllib2.Request(vt_url, encoded_parameters)
response = urllib2.urlopen(request)
json_response = json.loads(response.read())
if json_response['response_code']:
detections = json_response['positives']
total = json_response['total']
scan_results = json_response['scans']
print "Detections: %s/%s" % (detections, total)
print "VirusTotal Results:"
for av_name, av_data in scan_results.items():
print "\t%s ==> %s" % (av_name, av_data['result'])
else:
print "No AV Detections For: %s" % hash_value
