import java.util.ArrayList;
import java.util.Arrays;

public class BruteCollinearPoints {
    
    private ArrayList<LineSegment> tempSegments = new ArrayList<LineSegment>(); // hold temporary segments
    
    /*
     * Constructor initializes instance var.
     */
    public BruteCollinearPoints(Point[] points)    // finds all line segments containing 4 points
    {
        int N = points.length;
        
        /*
         * following inner loop (x4) gives permutation for all elements in set
         */
        for (int a=0; a < N-3; a++){
            for (int b=a+1; b < N-2; b++){
                for (int c=b+1; c < N-1; c++){
                    for (int d=c+1; d < N; d++){
                        if (points[a].slopeTo(points[b]) == points[a].slopeTo(points[c])){ // if two slopes are not same, move on
                            if (points[a].slopeTo(points[b]) == points[a].slopeTo(points[d])){ // if three slopes are same
                                Point[] tempPoints = new Point[4]; // create a seperate array to sort the four points by natural order
                                Arrays.sort(tempPoints);
                                tempSegments.add(new LineSegment(tempPoints[0],tempPoints[3])); // add resulting linesegment to arraylist.
                            }
                        }
                    }
                }
            }
        }                              
    }
    
    public int numberOfSegments()      // the number of line segments
    { return tempSegments.size();}
    
    public LineSegment[] segments() // the line segments (order the points so that only 1 segment can be made. but do i really need to?)
    {
        LineSegment[] finalSegments = new LineSegment[numberOfSegments()];

        int i = 0;
        
        for (LineSegment lineSegment : tempSegments)
        {
            finalSegments[i] = lineSegment;
            i++;
        }
        
        return finalSegments;
    }
}
