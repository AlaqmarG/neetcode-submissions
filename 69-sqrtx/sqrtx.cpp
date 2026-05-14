class Solution {
public:
    int mySqrt(int x) {
        // Brute force square root
        long i = 0;

        while (true) {
            if (i * i > x) {
                return i - 1;
            }

            i++;
        }

        return -1; // Unreachable
    }
};