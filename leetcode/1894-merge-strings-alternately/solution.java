class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder result = new StringBuilder();

        int l1 = word1.length();
        int l2 = word2.length();
        int min = Math.min(l1,l2);
        int i = 0;

        while(i<min)
        {
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
            i++;
        }
        if (l1>l2)
        {
            result.append(word1.substring(i));
        }
        else if (l2>l1)
        {
            result.append(word2.substring(i));
        }
        return result.toString();
    }
}
