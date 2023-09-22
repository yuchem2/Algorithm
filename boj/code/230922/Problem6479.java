package project2;

import java.io.*;
import java.util.*;

class Pair implements Comparable<Pair> {
	private int v, w;

	public Pair(int v, int w) {
		this.v = v;
		this.w = w;
	}

	public int getV() {
		return this.v;
	}

	public int getW() {
		return this.w;
	}

	@Override
	public int compareTo(Pair o) {
		if (this.w > o.w)
			return 1;
		else if (this.w < o.w)
			return -1;
		else
			return 0;
	}
}

public class Problem6479 {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	StringTokenizer st = null;

	Problem6479() throws IOException {

		int n = -1, m = -1;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		while (!(n == 0 && m == 0)) {
			solve(n, m);
			
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());

		}

		br.close();
		bw.close();
	}

	public void solve(int n, int m) throws IOException {

		int x, y, z, i, result;
		ArrayList<LinkedList<Pair>> adj = new ArrayList<LinkedList<Pair>>();
		for (i = 0; i < n + 1; i++) {
			adj.add(new LinkedList<Pair>());
		}
		
		result = 0;
		for (i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			z = Integer.parseInt(st.nextToken());
			adj.get(x).add(new Pair(y, z));
			adj.get(y).add(new Pair(x, z));
			result += z;
		}

		PriorityQueue<Pair> que = new PriorityQueue<Pair>();
		int[] visited = new int[n + 1];
		Pair u;
		
		que.add(new Pair(0, 0));

		while (que.size() > 0) {
			u = que.poll();
			if (visited[u.getV()] == 1)
				continue;

			visited[u.getV()] = 1;
			result -= u.getW();

			for (Pair v : adj.get(u.getV())) {
				if (visited[v.getV()] == 0)
					que.add(v);
			}
		}

		bw.write(String.format("%d\n", result));
		bw.flush();
	}

	public static void main(String[] args) throws IOException {
		new Problem6479();
	}

}
