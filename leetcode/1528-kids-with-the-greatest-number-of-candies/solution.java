class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) 
    {
            int Greatest = Arrays.stream(candies).max().getAsInt();
            int i = 0;
            List<Boolean> result = new ArrayList<>();
            for(i=0;i<candies.length;i++)
            {
                if(candies[i]+extraCandies >= Greatest)
                {
                    result.add(true);
                }
                else{
                    result.add(false);
                }
            } 
        return result;
    }
}
