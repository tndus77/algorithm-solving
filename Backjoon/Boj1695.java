import java.io.*;
import java.util.*;

/*
 * Backjoon
 * 
 * 1695 팰린드롬 만들기
 * 
 * @see https://www.acmicpc.net/problem/1695
 * 
 */
/*
 * 1. 아이디어 
 * 제일 짧은 팰린드롬의 길이를 구한다.
 * -> 원래 문자열의 접미사와 뒤집은 문자열의 접두사가 제일 많이 겹치는 길이를 구해야함.
 */
public class Boj1695 {
  public static int N;
  public static int[][] dp;
  public static int[] arr;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    N = Integer.parseInt(br.readLine());
    dp = new int[N+1][N+1];
    arr = new int[N+1]; // dp에서 배열은 0이 아닌 1부터 사용하자

    for(int i=0; i<N; i++) {
      Arrays.fill(dp[i], -1);
    }

    st = new StringTokenizer(br.readLine());
    for(int i=0; i<N; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    int res = dp(0, N-1);
    System.out.println(res);
  }

  public static int dp(int start, int end) {
    if(start>=end) return 0;
    // 이미 찾은 값이면
    if(dp[start][end] != -1) return dp[start][end];
    int min = 0;
    // 팰린드롬 상태이면, 양쪽 한칸씩 땡김
    if(arr[start] == arr[end]) return min = dp(start+1, end-1);
    // 아니면, 왼쪽에 삽입하는 경우와 오른쪽에 삽입하는 경우를 순회후 비교
    else 
      min = Math.min(dp(start+1,end)+1, dp(start, end-1)+1);
    return dp[start][end] = min;
  }
}
