
public class SwapArrEltRunnableDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = {4,8};
		System.out.println("arr = " + arr[0] +", " + arr[1]);
		Thread t = new Thread(new SwapArrEltRunnable(arr));
		t.start();
		
		try{
			Thread.sleep(100);
		}catch (InterruptedException e){
			System.exit(1);
		}
		System.out.println("arr = " + arr[0] +", " + arr[1]);
	}

}
