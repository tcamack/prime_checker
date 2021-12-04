# Prime Number Finder

Script to find prime numbers within a specified range.

## Installation
```
git clone https://github.com/tcamack/prime_finder.git
```

## Usage

### Command Line
```
usage: prime.py [-h] [--min MIN] [--path PATH] [--log | --no-log] [--list | --no-list] max

Prime Checker

positional arguments:
  max                Maximum number to check as prime.
                     Must be a positive integer.

optional arguments:
  -h, --help         show this help message and exit
  --min MIN          Minimum number to check as prime.
                     Must be a positive integer, default is 1.
  --path PATH        Output path for generated log file.
                     Default is ./logs directory in source folder.
  --log, --no-log    Generate external file listing every prime.
  --list, --no-list  List prime numbers in CLI.
```

## Output

Logs are saved to the `./logs` directory unless otherwise specified.