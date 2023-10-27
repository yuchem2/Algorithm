import java.util.Scanner;
import java.util.StringTokenizer;

public class Problem7869 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		double x1, y1, r1, x2, y2, r2;

		StringTokenizer st = new StringTokenizer(scanner.nextLine());

		x1 = Double.valueOf(st.nextToken());
		y1 = Double.valueOf(st.nextToken());
		r1 = Double.valueOf(st.nextToken());
		x2 = Double.valueOf(st.nextToken());
		y2 = Double.valueOf(st.nextToken());
		r2 = Double.valueOf(st.nextToken());

		double dist = getDistance(x1, y1, x2, y2);
		double result, t1, t2;
		if (dist >= r1 + r2)
			result = 0;
		else if (dist <= Math.abs(r1 - r2))
			result = Math.PI * Math.pow(Math.min(r1, r2), 2);
		else {
			t1 = 2 * Math.acos((dist * dist + r1 * r1 - r2 * r2) / (2 * dist * r1));
			t2 = 2 * Math.acos((dist * dist + r2 * r2 - r1 * r1) / (2 * dist * r2));

			result = 0.5 * (r1 * r1 * t1 + r2 * r2 * t2 - r1 * r1 * Math.sin(t1) - r2 * r2 * Math.sin(t2));
		}

		System.out.println(String.format("%.3f", result));
	}

	static double getDistance(double x1, double y1, double x2, double y2) {
		return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
	}

}
