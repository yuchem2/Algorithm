import java.io.*;
import java.util.StringTokenizer;

public class Problem1069 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int x, y, d, t;
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());

		double dist = Math.sqrt(x * x + y * y);
		int jump = (int) (dist / d);
		double remain = dist - jump * d;
		double ans = Math.min(dist, remain + jump * t); // walk & jump + remain

		ans = Math.min(ans, (jump + 1) * d - dist + (jump + 1) * t); // jump + jump - walk

		if (jump > 0)
			ans = Math.min(ans, (double) (jump + 1) * t); // only jump
		else if (dist < d)
			ans = Math.min(ans, t * 2.0); // twice jump

		System.out.print(ans);

		br.close();
	}

}
