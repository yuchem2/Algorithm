import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Problem1311 {

	static int n;
	static int[][] dp;
	static int[][] work;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(br.readLine());
		work = new int[n][n];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++)
				work[i][j] = Integer.parseInt(st.nextToken());
		}

		dp = new int[n][1 << n];
		for (int i = 0; i < n; i++)
			Arrays.fill(dp[i], -1);
		System.out.print(dfs(0, 0));

		br.close();
	}

	public static int dfs(int x, int visited) {
		if (visited == (1 << n) - 1)
			return 0;
		if (dp[x][visited] != -1)
			return dp[x][visited];

		dp[x][visited] = 123456789;
		for (int i = 0; i < n; i++) {
			if ((visited & (1 << i)) > 0)
				continue;

			dp[x][visited] = Math.min(dp[x][visited], dfs(x + 1, visited | (1 << i)) + work[x][i]);
		}

		return dp[x][visited];
	}

}
