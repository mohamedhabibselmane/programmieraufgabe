import unittest
import random
from urllib.request import urlopen
from prime_number_generator import is_prime


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        # primes is a list of the first prime numbers under 1000, taken from a random website
        primes = urlopen('https://www.di-mgt.com.au/primes1000.txt').readlines()
        primes = [int(prime) for prime in primes]

        # denotes the number of random numbers used to test is_prime
        nb_test_cases = 120

        # execute this test for the indicated nb_test_cases
        for counter in range(nb_test_cases):
            # choose a random number under 1000 to check whether it's prime
            random_nb = random.randrange(1000)

            self.assertEqual(is_prime(random_nb), random_nb in primes)

        print(nb_test_cases, "test cases were included for this unit: is_prime. ")


if __name__ == '__main__':
    unittest.main()
