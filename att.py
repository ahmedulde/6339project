import csv
f=open("yelp_academic_dataset_review.csv",'r')
#cw=csv.writer(f, delimiter=',')
csv_reader=csv.reader(f,delimiter=',')
file=open("log.txt",'w')
for row in csv_reader:
	file.write(str(row))
	break