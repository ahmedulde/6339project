#generating a yelp social graph

import json
import csv
yelpuser=open('socialgraph.csv','w')
writer=csv.writer(yelpuser)
#writer.writerow(['user_id','review_count','cool','useful','funny','elite','fans','friends','avg_stars'])
for line in open('yelp_academic_dataset_user.json'):
	l=json.loads(line)
	userid=l['user_id']
	friends=l['friends']
	for f in friends:
		row=[userid,f]
		writer.writerow(row)
print("Success!!")
yelpuser.close()

	

