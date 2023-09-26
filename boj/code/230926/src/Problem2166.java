import java.io.*;
import java.util.*;

class Point {
	private long x, y;

	public Point(long x, long y) {
		this.x = x;
		this.y = y;
	}

	public long getX() {
		return x;
	}

	public long getY() {
		return y;
	}

	public double area(Point o) {
		return o.x * this.y - o.y * this.x;
	}

}

public class Problem2166 {

	static Point[] labels;

	public static void main(String[] args) throws IOException {

		BufferedReader bw = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n, i, j;
		double area = .0;

		n = Integer.parseInt(bw.readLine());

		labels = new Point[n];
		for (i = 0; i < n; i++) {
			st = new StringTokenizer(bw.readLine());
			labels[i] = new Point(Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken()));
		}

		j = n - 1;
		for (i = 0; i < n; i++) {
			area += labels[i].area(labels[j]);
			j = i;
		}

		System.out.println(String.format("%.1f", Math.abs(area) / 2));

		bw.close();
	}

}
