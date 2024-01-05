import java.io.*;
import java.util.StringTokenizer;

public class problem2098 {
    static BufferedReader br;
    static BufferedWriter bw;
    static int[][] w, dp;
    static int n;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        w = new int[n][n];
        dp = new int[n][1 << n];
        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++)
                w[i][j] = Integer.parseInt(st.nextToken());
        }
    
        bw.write(tsp(0, 1) + "\n");
        bw.flush();

        br.close();
        bw.close();
    }

    public static int tsp(int current, int bitmask) {
        if (bitmask == ((1 << n) - 1)) {
            if (w[current][0] == 0)
                return 987654321;
            else 
                return w[current][0];
        }
        
        if (dp[current][bitmask] != 0)
            return dp[current][bitmask];
        dp[current][bitmask] = 987654321;

        for(int i=0; i<n; i++) {
            if (w[current][i] == 0 || (bitmask & (1 << i)) == (1 << i)) 
                continue;
            dp[current][bitmask] = Math.min(dp[current][bitmask], w[current][i] + tsp(i, bitmask | 1 << i));
        }
        return dp[current][bitmask];
    }
    
}
