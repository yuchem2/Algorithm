import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Problem11723 {
	static BufferedReader br;
	static BufferedWriter bw;
	static int bitmask;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int m = Integer.parseInt(br.readLine());
		bitmask = 0;

		for (int i = 0; i < m; i++)
			union();

		bw.flush();
		br.close();
		bw.close();
	}

	public static void union() throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());

		String oper = st.nextToken();
		if (oper.compareTo("add") == 0) {
			bitmask = bitmask | (1 << Integer.parseInt(st.nextToken()));

		} else if (oper.compareTo("remove") == 0) {
			bitmask = bitmask & ~(1 << Integer.parseInt(st.nextToken()));

		} else if (oper.compareTo("check") == 0) {
			int buff = bitmask & (1 << Integer.parseInt(st.nextToken()));
			if (buff == 0)
				bw.write(0 + "\n");
			else
				bw.write(1 + "\n");

		} else if (oper.compareTo("toggle") == 0) {
			bitmask = bitmask ^ (1 << Integer.parseInt(st.nextToken()));

		} else if (oper.compareTo("all") == 0) {
			bitmask = 0;
			bitmask = ~bitmask;

		} else {
			bitmask = 0;

		}

	}

}
