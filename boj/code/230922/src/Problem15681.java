import java.io.*;
import java.util.*;

public class Problem15681 {

	static ArrayList<LinkedList<Integer>> edge;
	static int[] vNum;

	public static void main(String[] args) throws IOException {
		int n, root, q, i, query;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		root = Integer.parseInt(st.nextToken()) - 1;
		q = Integer.parseInt(st.nextToken());

		edge = new ArrayList<LinkedList<Integer>>();
		for (i = 0; i < n; i++) {
			edge.add(new LinkedList<Integer>());
		}

		for (i = 0; i < n - 1; i++) {
			int u, v;
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken()) - 1;
			v = Integer.parseInt(st.nextToken()) - 1;
			edge.get(u).add(v);
			edge.get(v).add(u);
		}

		vNum = new int[n];
		treeCount(root, root);

		for (i = 0; i < q; i++) {
			query = Integer.parseInt(br.readLine()) - 1;
			bw.write(String.valueOf(vNum[query] + 1) + "\n");
		}

		bw.flush();
		br.close();
		bw.close();

	}

	public static int treeCount(int cntNode, int parent) {
		int cnt = 0;
		for (int v : edge.get(cntNode)) {
			if (v != parent) {
				vNum[cntNode] += treeCount(v, cntNode);
				cnt++;
			}
		}

		vNum[cntNode] += cnt;
		return vNum[cntNode];
	}

}
