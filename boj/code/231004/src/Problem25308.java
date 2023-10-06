import java.io.*;
import java.util.*;

public class Problem25308 {

	static final int STATS_NUM = 8;
	static int cnt = 0;
	static int[] stats, polygon;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		stats = new int[STATS_NUM];
		for (int i = 0; i < STATS_NUM; i++)
			stats[i] = Integer.parseInt(st.nextToken());

		visited = new boolean[STATS_NUM];
		polygon = new int[STATS_NUM];
		Arrays.fill(visited, false);
		makePolygon(0);
		System.out.print(cnt);

		br.close();

	}

	public static boolean isValid() {
		double x, y, z;

		for (int i = 0; i < STATS_NUM; i++) {
			x = stats[polygon[i]];
			y = stats[polygon[(i + 1) % STATS_NUM]] / Math.sqrt(2);
			z = stats[polygon[(i + 2) % STATS_NUM]];

			if (y + (x / z) * y - x < 0)
				return false;
		}

		return true;
	}

	public static void makePolygon(int idx) {
		if (idx == STATS_NUM) {
			if (isValid())
				cnt++;
			return;
		}

		for (int i = 0; i < STATS_NUM; i++) {
			if (visited[i])
				continue;

			visited[i] = true;
			polygon[idx] = i;
			makePolygon(idx + 1);
			visited[i] = false;
		}

	}

}
