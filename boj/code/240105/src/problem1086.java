import java.io.*;
import java.util.Arrays;

public class problem1086 {
    static int n, k;
    static int[] setNum, setSize;
    static int[] pow = new int[51];
    static long[][] dp;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        String[] set = new String[n];
        for (int i=0; i<n; i++) 
            set[i] = br.readLine().strip();
        k = Integer.parseInt(br.readLine());
        
        setNum = new int[n];
        setSize = new int[n];
        pow[0] = 1;
        long q = 1;
        for (int i=1; i<51; i++)
            pow[i] = (pow[i-1] * 10) % k;
        for (int i=0; i<n; i++) {
            q *= (i+1);
            setSize[i] = set[i].length();
            setNum[i] = 0;
            for(int j=0; j<setSize[i]; j++) {
                setNum[i] += (set[i].charAt(setSize[i] - j - 1) - '0') * pow[j] % k;
            }
        }
        dp = new long[k+1][1 << n];
        for (int i=0; i<k+1; i++)
            Arrays.fill(dp[i], -1);
        dfs(0, 0);

        long num = gcd(q, dp[0][0]);
        dp[0][0] = dp[0][0]/num;
        q = q/num;
        System.out.println(dp[0][0] + "/" + q);
        br.close();
    }

    public static long dfs(int current, int bitmask) {
        if (bitmask == (1 << n) - 1)
            return current % k == 0 ? 1 : 0;
        
        if (dp[current][bitmask] != -1)
            return dp[current][bitmask];
        dp[current][bitmask] = 0;
        for(int i=0; i<n; i++) {
            if ((bitmask & (1 << i)) == (1 << i))
                continue;
            int next = (current * pow[setSize[i]] + setNum[i]) % k;
            dp[current][bitmask] += dfs(next, bitmask | (1 << i));
        }
        return dp[current][bitmask];
    }

    public static long gcd(long a, long b) {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }
}
