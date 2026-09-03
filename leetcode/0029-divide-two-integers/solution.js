// Define a function that takes the dividend and divisor as input.
function divide(dividend, divisor) {
    // Store the maximum value allowed for a 32-bit signed integer.
    const MAX = 2 ** 31 - 1;

    // Store the minimum value allowed for a 32-bit signed integer.
    const MIN = -(2 ** 31);

    // Determine whether the final quotient should be negative.
    const isNegative = (dividend < 0) !== (divisor < 0);

    // Convert the dividend to a positive value for easier subtraction.
    let dividendAbs = Math.abs(dividend);

    // Convert the divisor to a positive value for easier subtraction.
    const divisorAbs = Math.abs(divisor);

    // Store the quotient that we will build.
    let quotient = 0;

    // Continue while the remaining dividend is large enough to subtract the divisor.
    while (dividendAbs >= divisorAbs) {
        // Start with one copy of the divisor.
        let currentDivisor = divisorAbs;

        // Start with a quotient contribution of one.
        let currentQuotient = 1;

        // Keep doubling the divisor while the doubled value still fits.
        while (currentDivisor + currentDivisor <= dividendAbs) {
            // Double the current divisor without using multiplication.
            currentDivisor += currentDivisor;

            // Double the corresponding quotient contribution.
            currentQuotient += currentQuotient;
        }

        // Subtract the largest possible doubled divisor from the remaining dividend.
        dividendAbs -= currentDivisor;

        // Add the corresponding quotient contribution to our final quotient.
        quotient += currentQuotient;
    }

    // Apply the correct sign to the quotient.
    quotient = isNegative ? -quotient : quotient;

    // If the quotient exceeds the maximum 32-bit integer, return the maximum value.
    if (quotient > MAX) {
        return MAX;
    }

    // If the quotient is smaller than the minimum 32-bit integer, return the minimum value.
    if (quotient < MIN) {
        return MIN;
    }

    // Return the calculated quotient.
    return quotient;
}
