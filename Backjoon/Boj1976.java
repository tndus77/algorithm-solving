import java.io.*;
import java.util.*;

/*
 * Backjoon
 * 
 * 16916 부분 문자열
 * 
 * @see https://www.acmicpc.net/problem/1976
 * 
 */
/*
 * 1. 아이디어 
 * 
 * Union-find 알고리즘 사용
 */

 public class Boj1976 {
    static int[] parent;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine()); // 도시의 수
    int m = Integer.parseInt(br.readLine()); // 여행 계획에 속한 도시들의 수
    parent = new int[n+1];

    for(int i=1; i<n+1; i++) {
      parent[i] = i;
    }

    for(int i=1; i<n+1; i++) {
      st = new StringTokenizer(br.readLine());
      for(int j=1; j<m+1; j++) {
        int temp = Integer.parseInt(st.nextToken());

        if(temp == 1) {
          union(parent, i, j);
        }
      }
    }
    st = new StringTokenizer(br.readLine());
    // 첫 도시가 포함되어 있는지 check하기 위해
    int start = getParent(parent, Integer.parseInt(st.nextToken()));
    for(int i=0; i<m-1; i++) {
      int ans = Integer.parseInt(st.nextToken());

      if(start != getParent(parent, ans)) {
        System.out.println("NO");
        return;
      }
    }
    System.out.println("YES");

  }

  // x의 부모를 찾는 함수
  static int getParent(int parent[], int x) {
    if(parent[x] == x) return x;
    return parent[x] = getParent(parent, parent[x]);
  }

  // 두 부모 노드를 합치는 함수
  static void union(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    if(a>b) {
      parent[a] = b;
    }
    else {
      parent[b] = a;
    }
  }
 }