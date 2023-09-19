import java.io.*;

public class problem28278 {
	
	BufferedReader br = null;
	BufferedWriter bw = null;
	Integer[] array = new Integer[1000000];
	int len = 0;

	public int isempty() {
		if (len == 0) {
			return 1;
		} else
			return 0;
	}

	public void add(int num) {
		array[len] = num;
		len++;
	}

	public int pop() {
		if (isempty() == 1) {
			return -1;
		} else {
			int num = array[len - 1];
			len--;
			return num;
		}
	}

	public int size() {
		return len;
	}

	public int get() {
		if (isempty() == 1) {
			return -1;
		} else {
			int num = array[len - 1];
			return num;
		}
	}

	public problem28278() {
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		try {
			int line = Integer.parseInt(br.readLine());
			for (int i = 0; i < line; i++) {
				String command = br.readLine();
				int comInt = Character.getNumericValue(command.charAt(0));
				switch (comInt) {
				case 1:
					add(Integer.parseInt(command.substring(2)));
					break;
				case 2:
					bw.write(String.valueOf(pop()));
					bw.newLine();
					break;
				case 3:
					bw.write(String.valueOf(size()));
					bw.newLine();
					break;
				case 4:
					bw.write(String.valueOf(isempty()));
					bw.newLine();
					break;
				case 5:
					bw.write(String.valueOf(get()));
					bw.newLine();
					break;
				}
			}
		} catch(IOException e) {
			e.printStackTrace();
		}
		
		try {
			bw.flush();		
			br.close();
			bw.close();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		new problem28278();
	}

}
