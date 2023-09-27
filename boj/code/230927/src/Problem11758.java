import java.io.*;
import java.util.*;

public class Problem11758 {

	static int[] x;
	static int[] y;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int i;

		x = new int[3];
		y = new int[3];
		for (i = 0; i < 3; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			x[i] = Integer.parseInt(st.nextToken());
			y[i] = Integer.parseInt(st.nextToken());
		}

		int crossProduct = (x[0] - x[1]) * (y[1] - y[2]) - (x[1] - x[2]) * (y[0] - y[1]);

		if (crossProduct > 0) 
			System.out.println(1);
		else if(crossProduct < 0) 
			System.out.println(-1);
		else
			System.out.println(0);
		
		br.close();
	}

}
