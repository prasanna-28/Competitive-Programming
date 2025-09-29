import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        FastScanner() { br = new BufferedReader(new InputStreamReader(System.in)); }
        String next() throws IOException {
            while (st == null || !st.hasMoreElements()) st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt() throws IOException { return Integer.parseInt(next()); }
        long nextLong() throws IOException { return Long.parseLong(next()); }
    }

    public static void main(String[] args) throws IOException {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);

        int t = fs.nextInt();
        for (int tc = 0; tc < t; tc++) {
            int n = fs.nextInt();
            long y = fs.nextLong();
            int[] c = new int[n];
            int max = 0;
            for (int i = 0; i < n; i++) { c[i] = fs.nextInt(); if (c[i] > max) max = c[i]; }

            int[] p = new int[max + 2];
            for (int v : c) p[v]++;
            for (int i = 1; i < p.length; i++) p[i] += p[i - 1];

            long result = -(1L << 60);
            for (int x = 2; x <= max + 1; x++) {
                int nx = x;
                long sum = 0;
                int overlaps = 0;
                while (nx <= max + x + 2) {
                    int left = Math.min(max + 1, nx - x);
                    int right = Math.min(max + 1, nx);
                    int total = p[right] - p[left];
                    int q = nx / x;
                    int fq = (q <= max) ? (p[q] - p[q - 1]) : 0;
                    if (total != 0) {
                        sum += (long) q * total;
                        overlaps += Math.min(total, fq);
                    }
                    nx += x;
                }
                long income = sum - (long) (n - overlaps) * y;
                if (income > result) result = income;
            }
            out.println(result);
        }
        out.flush();
    }
}

