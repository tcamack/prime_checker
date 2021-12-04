"""Module for finding every prime number within a specified range."""
import argparse
import os

from time import strftime


def positive(value):
    """Define positive integer for type checking with argparser."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError('Integer should be a positive whole '
                                         f'number. {ivalue} is not recognized '
                                         'as a positive integer.')
    return ivalue


def prime(max=None, min=1, path='./logs', log=False, list_primes=False):
    """
    Prime finding math function.

    Arguments:
    max -- the maximum integer to be checked as a prime.
    min -- the minimum number to be checked as a prime.
    path -- Directory in which log file is saved.
            Defaults to ./logs directory.
            Passed through to logger() function.
    log -- Boolean toggle for logging primes in specified location.
           Location is set to path directory.
    list_primes -- Boolean toggle for listing primes in the CLI.
    """
    primes = []

    for value in range(min, max + 1):
        if value > 1:
            for i in range(2, value):
                if (value % i) == 0:
                    break
            else:
                primes.append(value)

    output_str = f'Prime numbers found from {min} -> {max}: {len(primes)}'
    output_length = len(output_str)

    if log:
        logger(path, primes, output_str, output_length)

    if list_primes:
        return(f'{output_str}'
               f'\n{"*" * output_length}\n'
               f'{primes}')

    elif not list_primes:
        return(f'{output_str}')


def logger(path, primes, output_str, output_length):
    """
    Log function to create external file listing primes.

    Arguments:
    path -- Directory in which log filed is saved.
            Defaults to ./logs directory.
    primes -- List of all primes found within tested range.
    output_str -- String containing information from test.
    output_length -- Length of output string.
    """
    if not os.path.isdir(path):
        os.mkdir(path)

    with open(f'{path}/{strftime("%d%m%Y%H%M%S")}_primes.txt', 'w') as outfile:
        outfile.write(f'{output_str}')
        outfile.write(f'\n{"*" * output_length}\n')
        outfile.write('\n'.join(str(n) for n in primes))
    return


class SmartFormatter(argparse.HelpFormatter):
    """Class to redefine argparser help string formatting."""

    def _split_lines(self, text: str, width: int) -> list[str]:
        """Define new line behavior."""
        if text.startswith('SF|'):
            return text[3:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prime Checker',
                                     formatter_class=SmartFormatter)
    parser.add_argument('max',
                        type=positive,
                        help='SF|Maximum number to check as prime.\n'
                             'Must be a positive integer.')
    parser.add_argument('--min',
                        default=1,
                        type=positive,
                        help='SF|Minimum number to check as prime.\n'
                             'Must be a positive integer, default is 1.\n')
    parser.add_argument('--path',
                        type=str,
                        default='./logs',
                        help='SF|Output path for generated log file.\n'
                             'Default is ./logs directory in source folder.')
    parser.add_argument('--log',
                        action=argparse.BooleanOptionalAction,
                        help='Generate external file listing every prime.')
    parser.add_argument('--list',
                        action=argparse.BooleanOptionalAction,
                        help='List prime numbers in the CLI.')

    args = parser.parse_args()
    print(prime(args.max, args.min, args.path, args.log, args.list))
