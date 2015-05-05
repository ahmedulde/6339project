#Preparing dataset for classifying and clustering of users
#Here we are extracting a basic profile for each user
import json
import csv
yelpuser=open('user.csv','w')
writer=csv.writer(yelpuser)
writer.writerow(['user_id','review_count','cool','useful','funny','elite','fans','friends','avg_stars'])
for line in open('yelp_academic_dataset_user.json'):
	l=json.loads(line)
	userid=l['user_id']
	reviewcount=l['review_count']
	avgstars=l['average_stars']
	elite=len(l['elite'])#considering number of years as elite
	fans=l['fans']
	friends=len(l['friends'])
	d={}
	d=l['votes']#funny, cool, useful
	row=[userid,reviewcount,d['cool'],d['useful'],d['funny'],elite,fans,friends,avgstars]
	if any(row):
		writer.writerow(row)
print("Success!!")
yelpuser.close()

	

