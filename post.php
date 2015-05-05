<!--
Student Name: Ahmed Ulde
CSE6339
PA5
http://ec2-52-4-3-110.compute-1.amazonaws.com/post.php
-->

<html>
<head>
</head>
<body>

<form enctype="multipart/form-data" action="post.php" method="post">
<input type="hidden" name="upload" value="1" />
Submit this file: <input name="userfile" type="file" /><br/>
Enter Number of Clusters:<input name="N" type="number"/><br/>
<input type="submit"  value="Send File" />
</form>


<?php
if(isset($_POST['upload'])){
	$thisfile = $_FILES['userfile']['name'];
	move_uploaded_file($_FILES['userfile']['tmp_name'],"uploads/" . $thisfile);
	echo("Uploaded to Server!!");
}
else{echo "error";}

if(isset($_POST['N'])){
exec("java -cp weka.jar weka.core.converters.CSVLoader uploads/user.csv > uploaded.arff", $output);
//exec("java -cp weka.jar weka.clusterers.SimpleKMeans -t okar.arff -N 3 > okarop.csv", $output);//this line outputs only cluster info
exec("java -cp weka.jar weka.filters.unsupervised.attribute.AddCluster -i uploaded.arff -o output.arff -W \"weka.clusterers.SimpleKMeans -N ".$_POST['N']."\"", $output);//this command appends cluster to input file
exec("java -cp weka.jar weka.core.converters.CSVSaver -i output.arff -o output.csv", $output); 

echo("Clustering Done...");
$_POST['start']=1;
}
if(isset($_POST['start'])){
	header("Location:test.html");
}
?>
</body>
</html>















