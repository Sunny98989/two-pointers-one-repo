class Solution {
public:
    double angleClock(int hour, int minutes) {
        double a = 30 * hour;
        if(hour==12)
        {
            double ans1 = ((minutes*6) - (minutes*0.5));
            return min(abs(ans1),360-abs(ans1));
        }
        else if(hour>6 && hour!=12)
        {
            double ans2 = ((minutes*0.5) + a) - (minutes*6);
            return min(abs(ans2),360-abs(ans2));
        }
        else
        {
            double ans3 = (minutes*6) - ((minutes*0.5) + a);
            return min(abs(ans3),360-abs(ans3));;
        }
        return 1;
    }
};
