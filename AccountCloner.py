import urllib2
import json
from git import Repo
import os
import base64

GIT_API_URL='https://api.github.com'
USER = 'MaxKramer'
API_TOKEN='XXXX'
OUTPUT_DIR= "/Users/Max/code/github/"

def get_api(url):
	request = urllib2.Request(GIT_API_URL + url)
	base64string = base64.encodestring('%s/token:%s' % (USER, API_TOKEN)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	result = urllib2.urlopen(request)
	return result.read()

repoJson = get_api("/user/repos")
repositories = json.loads(repoJson)

for r in repositories:
	print "Cloning " + r["name"] + " from " + r["ssh_url"]
	Repo.clone_from(r["ssh_url"], OUTPUT_DIR + r["name"])