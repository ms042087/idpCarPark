

public class ThreadForLoopAssignment {

		static int size=12;
		static int[] x = new int[size];

		static class LoopThread extends Thread {

			public void run() {
				x[0]=0;
				x[1]=1;
				for(int i =3; i<size; i=i+2)
					x[i] = x[i-2] + 2*i-1;
			}

		}

		public static void main(String[] args) {

			LoopThread thread = new LoopThread();
			thread.start();
			
			for(int i = 2; i<size; i=i+2)
				x[i] = x[i-2] + 2*i-1;
			
			// Make the main thread sleep for 1000 ms
			try {
				Thread.currentThread().sleep(1000);
			} catch (InterruptedException ie) {
				System.exit(1);
			}

			System.out.print("The x[] is: ");
			for (int i = 0; i < x.length; i++)
				System.out.print(x[i] + " ");
			System.out.println();


		}

	}
