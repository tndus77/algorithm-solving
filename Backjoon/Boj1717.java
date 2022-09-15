import java.io.*;
import java.util.*;

/*
 * Backjoon
 * 
 * 1717번 집합의 표현
 * 
 * @see https://www.acmicpc.net/problem/1717
 * 
 * UnionFind 문제
 */

public class Boj1717 {
  public static int[] parent;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    // parent는 n 이하의 자연수 
    parent = new int[n+1];
    for(int i=1; i<=n; i++) {
      parent[i] = i;
    }

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<m; i++) {
      st = new StringTokenizer(br.readLine());
      int command = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      if (command == 0) {
        union(a, b);
      } else if(command == 1) { //command == 1
        sb.append((isSameParent(a, b) ? "YES" : "NO") + "\n");
      } else {
        continue;
      }
    }
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }


  private static void union(int x, int y) {
    //가장 작은 부모 찾기
    x = find(x);
    y = find(y);

    // 같은 부모를 가지고 있지 않을 때 
    if(x != y) {
      if(x < y) {// x가 더 작을 때
        parent[y] = x;
      } else {// y가 더 작을 떄
        parent[x] = y;
      }
    } 
  }

  private static boolean isSameParent(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) 
      return true;

    return false;
  }

  private static int find(int x) {
    if(x == parent[x]) 
      return x;
    else 
      return parent[x] = find(parent[x]);
  }
}
