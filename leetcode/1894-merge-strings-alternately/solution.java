class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();  
        int i = 0;
        for(i = 0; i < Math.min(word1.length(), word2.length()) ; i++){
            res.append(word1.charAt(i));
            res.append(word2.charAt(i));
        }        
        if (word1.length() > word2.length()){
            res.append((word1.substring(word2.length())));
        }
        if (word2.length() > word1.length()){
            res.append((word2.substring(word1.length())));
        }
        return res.toString();
    }
}
