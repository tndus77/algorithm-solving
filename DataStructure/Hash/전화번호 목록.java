import javax.naming.spi.DirStateFactory.Result;

import java.util.*;

// 배열 이용
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        for(int i=0; i<phone_book.length-1; i++) {
            for(int j=i+1; j<phone_book.length; j++) {}
            if(phone_book[i].startsWith(phone_book[j])) return false;
           if(phone_book[j].startsWith(phone_book[i])) return false;
        }
    
        return answer;
    }
}

//해시 이용
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<>();

        //모든 전화번호를 해시맵에 넣는다.
        for(int i=0; i<phone_book.length; i++) {
            map.put(phone_book[i], i);
        }

        //해시맵에 전화번호가 있는지 확인한다.
        for(int i=0; i<phone_book.length; i++) {
            for(int j=0; j<phone_book[i].length(); j++) {
                if(map.containsKey(phone_book[i].substring(0, j)))
                    return false;
            }
        }
        return answer;
    }
}