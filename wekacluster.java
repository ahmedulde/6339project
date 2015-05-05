package clustering;
import java.awt.BorderLayout;
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.*;
import java.lang.*;

import weka.clusterers.*;
import weka.core.Instances;
import weka.gui.explorer.ClustererPanel;
import weka.gui.visualize.PlotData2D;
import weka.gui.visualize.VisualizePanel;

public class wekacluster {
public static void main(String args[])throws Exception{
	//DataInputStream dis=new DataInputStream(System.in);
	//DataSource source = new DataSource("C:\\Users\\Ahmed\\Desktop\\all_month.csv");
	//Instances instances=source.getDataSet();
	BufferedReader inputReader = new BufferedReader(new FileReader("C:\\Users\\Ahmed\\workspace\\clustering\\okar.csv"));
	Instances dataa = new Instances(inputReader);
	inputReader.close();
	// create the model 
	    SimpleKMeans kMeans = new SimpleKMeans();
	    kMeans.setNumClusters(3);
	    kMeans.buildClusterer(dataa); 

	    // print out the cluster centroids
	    Instances centroids = kMeans.getClusterCentroids(); 
	    for (int i = 0; i < centroids.numInstances(); i++) { 
	      System.out.println( "Centroid " + i+1 + ": " + centroids.instance(i)); 
	    } 

	    // get cluster membership for each instance 
	    for (int i = 0; i < dataa.numInstances(); i++) { 
	      System.out.println( dataa.instance(i) + " is in cluster " + kMeans.clusterInstance(dataa.instance(i)) + 1); 

	    }
	    
	    //evaluate cluster
	    ClusterEvaluation eval=new ClusterEvaluation();
	    eval.setClusterer(kMeans);
	    eval.evaluateClusterer(dataa);
	    
	    // setup visualization
	    // taken from: ClustererPanel.startClusterer()
	    PlotData2D predData = ClustererPanel.setUpVisualizableInstances(dataa, eval);
	    String name = (new SimpleDateFormat("HH:mm:ss - ")).format(new Date());
	    String cname = kMeans.getClass().getName();
	    if (cname.startsWith("weka.clusterers."))
	      name += cname.substring("weka.clusterers.".length());
	    else
	      name += cname;
	 
	    VisualizePanel vp = new VisualizePanel();
	    vp.setName(name + " (" + dataa.relationName() + ")");
	    predData.setPlotName(name + " (" + dataa.relationName() + ")");
	    vp.addPlot(predData);
	 
	    // display data
	    // taken from: ClustererPanel.visualizeClusterAssignments(VisualizePanel)
	    String plotName = vp.getName();
	    final javax.swing.JFrame jf = 
	      new javax.swing.JFrame("Weka Clusterer Visualize: " + plotName);
	    jf.setSize(500,400);
	    jf.getContentPane().setLayout(new BorderLayout());
	    jf.getContentPane().add(vp, BorderLayout.CENTER);
	    jf.addWindowListener(new java.awt.event.WindowAdapter() {
	      public void windowClosing(java.awt.event.WindowEvent e) {
	        jf.dispose();
	      }
	    });
	    jf.setVisible(true);
	  
	}
}
