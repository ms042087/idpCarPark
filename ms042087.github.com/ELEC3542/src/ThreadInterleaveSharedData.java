public class ThreadInterleaveSharedData {

	public static int sharedData = 0;

	static class MyThread extends Thread {

		private int id;

		public MyThread(int i) {
			id = i;
		}

		public void run() {
			System.out.println("Thread " + id + " before update: " + sharedData++);
			System.out.println("Thread " + id + " after update: " + sharedData);
		}

	}

	public static void main(String[] args) {
		MyThread thread1 = new MyThread(1);
		MyThread thread2 = new MyThread(2);
		MyThread thread3 = new MyThread(3);
		MyThread thread4 = new MyThread(4);

		thread1.start();
		thread2.start();
		thread3.start();
		thread4.start();

		// Make the main thread sleep for 1000 ms
		/*
		 * try {
		 /*
			Thread.currentThread().sleep(1000);
		} catch (InterruptedException ie) {
			System.exit(1);
		}
		*/

		System.out.println("Final value = " + sharedData);
	}

}
