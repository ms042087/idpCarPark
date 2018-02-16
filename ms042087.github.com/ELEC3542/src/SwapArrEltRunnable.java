
public class SwapArrEltRunnable implements Runnable{
	private int[] arr;
	
	public SwapArrEltRunnable(int[] list){
		arr= list;
	}
	public void run()
	{
		int temp = arr[0];
		arr[0] = arr[1];
		arr[1] = temp;
	}
}
