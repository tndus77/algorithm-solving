package 정렬;
import java.util.*;
import java.io.*;
/*
 * 1. 아이디어
 * 
 * 2. 시간속도
 * O(nlogn)
 * 3. 자료구조
 * 정렬
 */

public class arrange {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        //정렬
        Arrays.sort(arr);
        
        //출력
        for(int a : arr) {
            System.out.println(a);
        }
    }
}
