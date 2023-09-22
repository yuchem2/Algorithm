package project2;

import java.io.*;
import java.util.*;

class Point {
	private int x, y;

	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public int dist(Point o) {

		if (x == o.x)
			return Math.abs(y - o.y) - 1;
		else if (y == o.y)
			return Math.abs(x - o.x) - 1;
		else
			return -1;

	}
}

class Bridge implements Comparable<Bridge> {
	private int w, u, v;

	Bridge(int u, int v, int w) {
		this.u = u;
		this.v = v;
		this.w = w;
	}

	public int getU() {
		return u;
	}

	public int getV() {
		return v;
	}

	public int getW() {
		return w;
	}

	@Override
	public int compareTo(Bridge o) {
		if (w < o.w)
			return -1;
		else if (w > o.w)
			return 1;
		else
			return 0;
	}

}

public class Problem17472 {

	private static boolean[][] map;
	private static ArrayList<Point> islandList;
	private static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n, m, i, j, cur, cnt, result;
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		cnt = 0;
		map = new boolean[n][m];
		islandList = new ArrayList<Point>();
		for (i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (j = 0; j < m; j++) {
				cur = Integer.parseInt(st.nextToken());
				if (cur == 1) {
					map[i][j] = true;
					islandList.add(new Point(i, j));
					cnt++;
				}
			}
		}

		PriorityQueue<Bridge> q = new PriorityQueue<Bridge>();
		for (i = 0; i < islandList.size() - 1; i++) {
			for (j = i + 1; j < islandList.size(); j++) {
				int w = islandList.get(i).dist(islandList.get(j));
				if (w == 0 || (w > 1 && isValid(i, j)))
					q.add(new Bridge(i, j, w));

			}
		}

		parent = new int[islandList.size()];
		for (i = 0; i < parent.length; i++)
			parent[i] = i;

		result = 0;
		while (!q.isEmpty()) {
			Bridge u = q.poll();
			if (union(u.getU(), u.getV())) {
				result += u.getW();
				cnt--;
			}
			if (cnt == 1)
				break;
				
		}
		System.out.println(cnt == 1 ? result : -1);
		br.close();
	}

	public static boolean isValid(int a, int b) {
		
		int maxX, minX, maxY, minY;
		Point st = islandList.get(a), ed = islandList.get(b);

		if (st.getX() == ed.getX()) {
			minY = Math.min(st.getY(), ed.getY());
			maxY = Math.max(st.getY(), ed.getY());
			for (int i = minY+1; i < maxY; i++) {
				if (map[st.getX()][i])
					return false;
			}
		} else if (st.getY() == ed.getY()) {
			minX = Math.min(st.getX(), ed.getX());
			maxX = Math.max(st.getX(), ed.getX());
			for (int i = minX+1; i < maxX; i++) {
				if (map[i][st.getY()])
					return false;
			}
		}

		return true;
	}

	public static int find(int x) {
		int c = parent[x];
		if (c == x)
			return c;
		else
			return find(c);
	}

	public static boolean union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y)
			return false;

		parent[x] = y;
		return true;
	}

}
