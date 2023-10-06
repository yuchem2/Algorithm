import java.io.*;
import java.util.StringTokenizer;

class Point {
	private int x, y;

	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int ccw(Point p1, Point p2) {
		long crossProduct = (long) (this.x - p1.x) * (p1.y - p2.y) - (long) (p1.x - p2.x) * (this.y - p1.y);

		if (crossProduct > 0)
			return 1;
		else if (crossProduct < 0)
			return -1;
		else
			return 0;
	}

	// return this >= p1
	public boolean compare(Point p1) {
		if (this.x == p1.x)
			return this.y >= p1.y;
		else
			return this.x >= p1.x;
	}

}

class Line {
	private Point p1, p2;

	public Line(Point p1, Point p2) {
		this.p1 = p1;
		this.p2 = p2;
	}

	public boolean isCross(Line l1) {
		int this_l1, l1_this;
		this_l1 = p1.ccw(p2, l1.p1) * p1.ccw(p2, l1.p2);
		l1_this = l1.p1.ccw(l1.p2, p1) * l1.p1.ccw(l1.p2, p2);

		if (this_l1 == 0 && l1_this == 0) {
			if (p1.compare(p2))
				swap();
			if (l1.p1.compare(l1.p2))
				l1.swap();

			if (p2.compare(l1.p1) && l1.p2.compare(p1))
				return true;
			else
				return false;
		} else {
			if (this_l1 <= 0 && l1_this <= 0)
				return true;
			else
				return false;
		}
	}

	public void swap() {
		Point temp;
		temp = p1;
		p1 = p2;
		p2 = temp;
	}

}

class Lineset {

	private Line[] values;
	private int[][] sets;
	private int len, maxSize, groupNum;

	public Lineset(int len) {
		this.len = len;
		groupNum = len;
		values = new Line[len];
		sets = new int[len][2];

		for (int i = 0; i < len; i++) {
			sets[i][0] = i;
			sets[i][1] = 1;
		}

		maxSize = 1;
	}

	public void setLine(int idx, Point p1, Point p2) {
		if (idx < len)
			values[idx] = new Line(p1, p2);
	}

	public int getMaxSize() {
		return maxSize;
	}

	public int getGroupNum() {
		return groupNum;
	}

	private boolean link(int l1, int l2) {
		int size;
		if (sets[l1] == sets[l2])
			return false;

		size = sets[l1][1] + sets[l2][1];
		if (sets[l1][1] >= sets[l2][1]) {
			sets[l1][1] = size;
			sets[l2][0] = l1;
		} else {
			sets[l2][1] = size;
			sets[l1][0] = l2;
		}

		if (maxSize < size)
			maxSize = size;

		groupNum--;

		return true;
	}

	public int find(int l1) {
		int parent;
		parent = sets[l1][0];
		if (parent == l1)
			return parent;
		else
			return find(parent);
	}

	public boolean union(int l1, int l2) {
		if (values[l1].isCross(values[l2]))
			return link(find(l1), find(l2));
		else
			return false;
	}
}

public class Problem2162 {

	static Lineset lines;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n, i, j;
		n = Integer.parseInt(br.readLine());

		lines = new Lineset(n);
		for (i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			Point p1, p2;
			p1 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			p2 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

			lines.setLine(i, p1, p2);
		}

		for (i = 0; i < n - 1; i++) {
			for (j = i + 1; j < n; j++)
				lines.union(i, j);
		}

		System.out.println(lines.getGroupNum());
		System.out.println(lines.getMaxSize());

	}

}
