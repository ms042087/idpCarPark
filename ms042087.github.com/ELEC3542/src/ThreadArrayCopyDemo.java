public class ThreadArrayCopyDemo {

	public static int[] x = { 1, 2, 3, 4, 5 }, y;

	static class CopyThread extends Thread {

		// Copy the even elements from x to y
		public void run() {
			for (int i = 0; i < x.length; i = i + 2)
				y[i] = x[i];
		}

	}

	public static void main(String[] args) {
		y = new int[x.length];

		CopyThread thread = new CopyThread();
		thread.start();

		for (int i = 1; i < x.length; i = i + 2)
			y[i] = x[i];

		/*
		// Make the main thread sleep for 1000 ms
		try {
			Thread.currentThread().sleep(1000);
		} catch (InterruptedException ie) {
			System.exit(1);
		}
		*/

		System.out.print("The original x[] is: ");
		for (int i = 0; i < x.length; i++)
			System.out.print(x[i] + " ");
		System.out.println();

		System.out.print("y[] is: ");
		for (int i = 0; i < y.length; i++)
			System.out.print(y[i] + " ");
		System.out.println();
	}

}
