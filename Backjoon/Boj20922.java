import java.util.*;
import java.io.*;
/*
 * Backjoon
 * 
 * 20922 겹치는 건 싫어
 * 
 * @see https://www.acmicpc.net/problem/20922
 * 
 * 나중에 다시 풀어볼 것. 이해 안됨
 */

public class Boj20922 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer s = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(s.nextToken());
    int k = Integer.parseInt(s.nextToken());
    int[] a = new int[n];

    s = new StringTokenizer(br.readLine());
    for(int i=0; i<n; i++) {
      a[i] = Integer.parseInt(s.nextToken());
    }

    System.out.println(twoPointer(k, a));
  }

  private static int twoPointer(int K, int[] arr) {
    //deque 덱 -> double-ended queue
    Queue<Integer> q = new ArrayDeque<>();
    int[] cnt = new int[100001];
    int max = 0;

    for(int a : arr) {
      max = Math.max(max, q.size());

      while(cnt[a] == K) {
        cnt[q.poll()] --;
      }

      q.offer(a);
      cnt[a]++;
    }
    return Math.max(max, q.size());
  }

}
