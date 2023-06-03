#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int MAX = 20000000;
const int SEGMENT_SIZE = 10000;

vector<int> primes;  // Stores the generated primes

void segmentedSieve() {
    int sqrtMax = sqrt(MAX) + 1;
    int segmentStart = 2;
    int segmentEnd = SEGMENT_SIZE;

    // Generate primes up to sqrt(MAX)
    vector<bool> sieve(sqrtMax, true);
    for (int i = 2; i < sqrtMax; i++) {
        if (sieve[i]) {
            for (int j = i * i; j < sqrtMax; j += i) {
                sieve[j] = false;
            }
            primes.push_back(i);
        }
    }

    // Generate twin prime pairs
    vector<bool> isPrime(SEGMENT_SIZE, true);
    for (int k = 0; k < primes.size(); k++) {
        int p = primes[k];
        int start = max(p * p, (segmentStart + p - 1) / p * p);
        for (int j = start; j <= segmentEnd; j += p) {
            isPrime[j - segmentStart] = false;
        }
    }

    int count = 0;
    for (int i = segmentStart; i <= segmentEnd; i++) {
        if (isPrime[i - segmentStart] && isPrime[i - segmentStart + 2]) {
            count++;
            if (count == 1)
                cout << "(" << i << ", " << i + 2 << ")";
            else
                cout << endl << "(" << i << ", " << i + 2 << ")";
        }
        if (count == SEGMENT_SIZE)
            break;
    }
}

int main() {
    int S;
    while (cin >> S) {
        segmentedSieve();
    }
    return 0;
}
