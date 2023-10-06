import java.io.*;
import java.util.StringTokenizer;

public class Problem20149 {

	static int x[], y[], ccw[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int i, j, result;

		x = new int[4];
		y = new int[4];
		ccw = new int[4];

		for (i = 0; i < 2; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (j = 0; j < 2; j++) {
				x[2 * i + j] = Integer.parseInt(st.nextToken());
				y[2 * i + j] = Integer.parseInt(st.nextToken());
			}
		}

		ccw[0] = ccw(0, 1, 2);
		ccw[1] = ccw(0, 1, 3);
		ccw[2] = ccw(2, 3, 0);
		ccw[3] = ccw(2, 3, 1);

		// 교차 검증
		if (ccw[0] * ccw[1] == 0 && ccw[2] * ccw[3] == 0) {
			if (compare(0, 1))
				swap(0, 1);

			if (compare(2, 3))
				swap(2, 3);

			if (compare(1, 2) && compare(3, 0))
				result = 1;
			else
				result = 0;
		} else {
			if (ccw[0] * ccw[1] <= 0 && ccw[2] * ccw[3] <= 0)
				result = 1;
			else
				result = 0;
		}

		if (result == 1) {
			System.out.println(1);
			findInterection();
		} else {
			System.out.println(0);
		}
	}

	public static int ccw(int p1, int p2, int p3) {
		long crossProduct = (long) (x[p1] - x[p2]) * (y[p2] - y[p3]) - (long) (x[p2] - x[p3]) * (y[p1] - y[p2]);

		if (crossProduct > 0)
			return 1;
		else if (crossProduct < 0)
			return -1;
		else
			return 0;
	}

	// return p1 >= p2
	public static boolean compare(int p1, int p2) {
		if (x[p1] == x[p2]) {
			return y[p1] >= y[p2];
		} else {
			return x[p1] >= x[p2];
		}
	}

	public static boolean isSame(int p1, int p2) {
		return x[p1] == x[p2] && y[p1] == y[p2];
	}

	public static void swap(int p1, int p2) {
		int temp;
		temp = x[p1];
		x[p1] = x[p2];
		x[p2] = temp;

		temp = y[p1];
		y[p1] = y[p2];
		y[p2] = temp;
	}

	public static void findInterection() {
		double denominator, temp1, temp2;
		denominator = (long) (x[0] - x[1]) * (y[2] - y[3]) - (long) (y[0] - y[1]) * (x[2] - x[3]);
		if (denominator == 0) {
			if (isSame(1, 2) && !compare(0, 3))
				System.out.print(x[1] + " " + y[1]);
			else if (isSame(3, 0) && !compare(2, 1))
				System.out.print(x[0] + " " + y[3]);
		} else {
			double xNumberator, yNumberator;
			temp1 = ((long) x[0] * y[1] - (long) y[0] * x[1]);
			temp2 = ((long) x[2] * y[3] - (long) y[2] * x[3]);
			xNumberator = (temp1 * (x[2] - x[3]) - (x[0] - x[1]) * temp2) / denominator;
			yNumberator = (temp1 * (y[2] - y[3]) - (y[0] - y[1]) * temp2) / denominator;

			if (xNumberator % 1 == 0 && yNumberator % 1 == 0)
				System.out.print(String.format("%d %d", (int)xNumberator, (int)yNumberator));
			else if (xNumberator % 1 == 0)
				System.out.print(String.format("%d %f", (int)xNumberator, yNumberator));
			else if (yNumberator % 1 == 0)
				System.out.print(String.format("%f %d", xNumberator, (int)yNumberator));
			else
				System.out.print(xNumberator + " " + yNumberator);
		}
	}

}
