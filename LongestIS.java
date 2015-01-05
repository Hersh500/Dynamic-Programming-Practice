import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class LongestIS
{
	public static void main (String[] args) 
	{
		int[] anArray = {10, 22, 9, 33, 21, 50, 41, 60, 80};
		SubsequenceFinder finder = new SubsequenceFinder(anArray); 
		int length = finder.findSubsequenceLength();
		ArrayList<Integer> seq = finder.getSubsequence();
		System.out.println("The Length of the LIS is " + length);
		System.out.println("The LIS is " + seq);
	}
}
	
class SubsequenceFinder
{
	private	int[] array; 
	private int[] subsequence; 
	private ArrayList<Integer> sVals;
	
	public SubsequenceFinder(int[] anArray)
	{
		array = anArray;
		subsequence = new int[array.length];
		sVals = new ArrayList<Integer>(); 
	}
	
	public int findSubsequenceLength()
	{
		ArrayList<Integer> maxes = new ArrayList<Integer>(); 
		subsequence[0] = 1;

		for (int i = 1; i < array.length; i++) 
		{
			for (int j = i; j >= 0; j--) 
			{
				if (array[j] < array[i]) 
					maxes.add(j);
			}
			if (maxes.size() > 0) 
				subsequence[i] = subsequence[findMaxIndex(maxes)] + 1; 	
			else
				subsequence[i] = 1;
			maxes.clear();
		}
		return (subsequence[findMaxIndex(subsequence)]);
	}
	
	public ArrayList<Integer> getSubsequence() 
	{
		ArrayList<Integer> indices = new ArrayList<Integer>();
		int x = findMaxIndex(subsequence);
		sVals.add(x);
		int i = x; 
		while (i >= 0) {
			if (array[i] < array[sVals.get(sVals.size() -1)] && subsequence[i] == subsequence[sVals.get(sVals.size() - 1)] - 1) {
				sVals.add(i);
			}
			i--;
		}

		for (i = 0; i < sVals.size(); i++) 
		{
			sVals.set(i, array[sVals.get(i)]);	
		}
		Collections.reverse(sVals);
		return(sVals);	
	}	
	
	public int findMaxIndex(int[] s)
	{
		int max = 0; 
		for (int i = 0; i < s.length; i++)
		{
			if (s[i] > s[max])
				max = i;
		}
		return(max);
	}	
	public int findMaxIndex(ArrayList<Integer> indices) 
	{
		int max = 0;	
		for (int index : indices) 
		{
			if (subsequence[index] > subsequence[max]) 
				max = index; 
		}
		return(max); 
	}
}
