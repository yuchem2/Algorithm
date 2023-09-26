import java.io.*;
import java.util.*;

public class problem2213 {

	static int[] weight, visited;
	static int[][] dp;
	static ArrayList<LinkedList<Integer>> edges;
	static ArrayList<Integer> path;

	public static void main(String[] args) throws IOException {

		BufferedReader bw = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n, u, v, i;
		n = Integer.parseInt(bw.readLine());
		weight = new int[n];
		edges = new ArrayList<LinkedList<Integer>>();
		st = new StringTokenizer(bw.readLine());

		for (i = 0; i < n; i++) {
			weight[i] = Integer.parseInt(st.nextToken());
			edges.add(new LinkedList<Integer>());
		}

		for (i = 0; i < n - 1; i++) {
			st = new StringTokenizer(bw.readLine());
			u = Integer.parseInt(st.nextToken()) - 1;
			v = Integer.parseInt(st.nextToken()) - 1;
			edges.get(u).add(v);
			edges.get(v).add(u);
		}

		dp = new int[n][2];
		dfs(0, -1);
		System.out.println(Math.max(dp[0][0], dp[0][1]));

		visited = new int[n];
		path = new ArrayList<Integer>();
		trace(0, 0);
		path.sort(Comparator.naturalOrder());
		for (int vertex : path)
			System.out.print(vertex + " ");
	}

	public static void dfs(int cnt, int parent) {
		dp[cnt][0] = 0;
		dp[cnt][1] = weight[cnt];

		for (int v : edges.get(cnt)) {
			if (v == parent)
				continue;
			dfs(v, cnt);
			dp[cnt][0] += Math.max(dp[v][0], dp[v][1]);
			dp[cnt][1] += dp[v][0];
		}
	}

	public static void trace(int cnt, int parent) {
		if (dp[cnt][1] > dp[cnt][0] && visited[parent] == 0) {
			path.add(cnt + 1);
			visited[cnt] = 1;
		}

		for (int v : edges.get(cnt)) {
			if (v == parent)
				continue;
			trace(v, cnt);
		}
	}
}
