import java.util.*;
import java.io.*;

/*
 * 1. 아이디어
 * 
 * 2. 시간 복잡도 
 * O(log N)??
 */
public class dot {
  static int n, m;
  static int[] dot;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    StringTokenizer st = new StringTokenizer(s);
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    //점
    dot = new int[n];
    st = new StringTokenizer(br.readLine());
    for(int i=0; i<n; i++) {
      dot[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(dot);

    //선분
    for(int i=0; i<m; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      int sum = m; 

      //최소값 좌표보다 작은 점의 갯수
      int left = 0; int right = n-1;
      while(left <= right) {
        int mid = (left+right) / 2;
  
        if(dot[mid] < x) {
          left = mid+1;
        } else {
          right = mid-1;
        }
      }
      sum -= left;
      left=0; right=n-1;

      while(left <= right) {
        int mid = (left+right) / 2;

        //최대값 좌표보다 큰 점의 갯수
        if(dot[mid] > y) {
          right = mid-1;
        } else {
          left = mid+1;
        }
      }
      sum -= (m-left);
      System.out.println(sum);
    }
    
  }
}
