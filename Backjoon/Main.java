/*
 * 1. 아이디어
 * readline으로 한줄씩 받고
 * 같은 이름이 있는지 check 후 전체 분포도 조사 -> HashMap 사용 (문자, 횟수)
 * 사전순 정렬 -> compareTo() 메소드 사용해서 
 * 2. 시간 복잡도
 */


package Backjoon;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int count = 0; //전체 갯수
        TreeMap<String, Integer> map = new TreeMap<>();
        
        String name = br.readLine();

        //받을 때까지
        while(true) {
            map.put(name, map.getOrDefault(name, 0) + 1);
            count ++;
            name = br.readLine();

            //빈 문자열이면 반복문 탈출
            if(name.isEmpty()) 
                break;
        }

        //키 사전순 정렬
        Iterator<String> tree = map.keySet().iterator();

        while(tree.hasNext()) {
            String key = tree.next();
            int value = map.get(key);
            double per = (double)(value*100)/count;
            System.out.println(key + " " + String.format("%.4f", per));
        }

    }
}
