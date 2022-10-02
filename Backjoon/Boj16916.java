import java.io.*;
import java.util.*;

/*
 * Backjoon
 * 
 * 16916 부분 문자열
 * 
 * @see https://www.acmicpc.net/problem/16916
 * 
 */
/*
 * 1. 아이디어 
 * 
 * KMP 알고리즘 사용
 */

public class Boj16916 {
  static int ans=0;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String parent = br.readLine();
    String pattern = br.readLine();

    KMP(parent, pattern);
    System.out.print(ans);
  }

  public static void KMP(String parent, String pattern) {
    int j=0;
    int[] table = makeTable(pattern);
    for(int i=0; i<parent.length(); i++) {
      while(j>0 && parent.charAt(i) != pattern.charAt(j)) {
        j = table[j-1];
      }
      if(parent.charAt(i) == pattern.charAt(j)) {
        if(j == pattern.length()-1) {
          j = table[j];
          ans = 1;
          break;
        } else {
          j++;
        }
      }
    }
  }

  public static int[] makeTable(String pattern) {
    int j=0;
    int[] table = new int[pattern.length()];

    for(int i=1; i<pattern.length(); i++) {
      while(j>0 && pattern.charAt(i) != pattern.charAt(j)) {
        j = table[j-1];
      }
      if(pattern.charAt(i) == pattern.charAt(j)) {
        table[i] = ++j;
      }
    }
    return table;
  }
}
