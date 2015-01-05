import java.util.Arrays;
/* 
	Given a sequence of n real numbers A(1) ... A(n), determine a contiguous subsequence A(i) ... A(j) for which the sum of elements in the subsequence is maximized.
*/ 
public class mvcs 
{
	public static void main(String[] args) 
	{
		int[] array = {-1, 5, 2, -3, 4, 7, 8, -10, 9, 11};
		Finder finder = new Finder(array); 
		int sum = finder.findSum(array.length-1);
		System.out.println("The sum is " + sum); 
		finder.sequenceFinder();
		System.out.println("The beginning and end indices of the maximum-value subsequence are " + finder.i + " and " + finder.j); 
	}
}

class Finder 
{
	private int[] array;
	private int[] maxSum;
	private boolean[] sequence; 
	public int i = 0; 
	public int j = 0;

	public Finder(int[] anArray) 
	{
		array = anArray; 
		maxSum = new int[array.length + 1];
		sequence = new boolean[array.length+1];
	}

	public int findSum(int index) 
	{
		maxSum[0] = array[0];
		sequence[0] = false;

		for (int i = 1; i < array.length; i++) {

			if (maxSum[i-1] + array[i] > array[i]) {
				maxSum[i] = maxSum[i-1] + array[i];
				sequence[i] = true; 
			}
			else {
				maxSum[i] = array[i];
				sequence[i] = false;
			}
		}
				
		System.out.println(Arrays.toString(array));
		System.out.println(Arrays.toString(maxSum));
		System.out.println(Arrays.toString(sequence));
		return (maxInArray(maxSum));	
		
	}

	public void sequenceFinder() 
	{
		j = maxIndexInArray(maxSum) - 1; 
		i = j;
		while (sequence[i] && i > 0) {
			i--; 
		}
	}
	
	public int maxIndexInArray(int[] x) 
	{
		int max = x[0];
		int maxIndex = 0;
		for(int i = 1; i < x.length; i++) {
			if (x[i] > max) 
				max = x[i];
				maxIndex = i; 
		}
		return(maxIndex);
	}

	public int maxInArray (int[] x) 
	{
		int max = x[0];
		for(int i = 1; i < x.length; i++) {
			if (x[i] > max) 
				max = x[i];
		}
		return(max);
	}
}
		
		
		
