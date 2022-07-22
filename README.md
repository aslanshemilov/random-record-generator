# Random Sales Record
#### Vanilla Python Solution 🍦🐍
This repository contains a solution to the random sales record technical test. The solution intends to meet the acceptance criteria provided without the use of nice tools or techniques.

## Running
### Virtual Environment
Consider running this application in a virtual environment to isolate it on your system:
```bash
    # Create a virtual environment called "venv".
    python -m venv venv
```

### Install Dependencies
To simply run the application, only the production dependencies are needed:

```bash
   pip install -r requirements.txt
```

To run with the development toolchain, development dependencies are also needed:
```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
```

To see the exact versions of dependencies used on my system, see [requirements-freeze.txt](./../requirements-freeze.txt).

## Running the Application
To run the application use the following command.
```bash
    # python main.py --count {RECORD_COUNT} --out {PATH_TO_OUTPUT_CSV}
    python main.py --count 10 --out './test-10.csv'
```

Note that a new CSV file is created by the application, so one need not exist prior. If the file already exists it will be overwritten.

## Approach
To begin the sales record was represented as a Python class. The class is a POPO (Plain Old Python Object) containing only the data structure and no business logic.

The business logic was broken down into various layers.

The lowest layer of business logic concerns generating a Sales record instance with its attributes set to random values. In order to achieve this the Python Library [Faker](https://faker.readthedocs.io/en/master/) was used.

Faker was chosen as it was a freely available production-grade library, as determined by its development status in pypy and commits and star counts in GitHub. The documentation available was also of a high quality.

I decided to use a library rather than implement the random generation logic myself in order to speed up development in a manner embraced in commericial software development and no security restrictions advised otherwise.

The higher level of business logic concerned combining the random sales record generation with writing data to CSV. The Python core `csv` library was used to write the records to CSV. A "serializer" class was utilised to encapsulate converting the `SalesRecord` class into a format usable by `csv`.

At the highest level `argparse` was used to create a command line interface. As argparse is notably tricky to test, the business logic was extracted into a "controller" class. The command line interface accepts the number of records to generate and the path to the output file.

It is possible to generate 1 million records on a typical workstation. On my machine this took ~3 minutes.


## Toolchain
This is the sequence of tools run on `make build`:

#### 1. Format: `black`
The [black](https://github.com/psf/black) code formatter automatically formats Python
code using an opinionated, but largely PEP8 compliant style. Used to ensure a consistent style.

Can be run independently using `make format`.

#### 2. Lint: `flake8`
The tool "flake8" enforces PEP8 compliant code style across the codebase and identify common bugs. USed to improve code quality.

Can also be run through `make lint`.

#### 3. Security Check Dependencies: `safety`
["Vulnerable and Outdated Components"](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
is entry #6 in the 2021 OWASP Top Ten.

The [safety](https://pypi.org/project/safety/) project goes some way to reduce this risk
by checking the project's installed dependencies for known security vulnerabilities.

The build will fail if the project contains a known vulnerability.

Can also be run through `make security`.

#### 4. Security Check Code: `bandit`
The tool `bandit` scans the project code to find common security issues.

If a common security issue is found, then the build will fail.

Can also be run through `make security`.

## Testing
Tests are provided across the codebase. The unittest style of testing was chosen based on personal preference. The test current cover `>95%` of the codebase.

## Improvements
Improvements I would like to make in future include:

### More Accurate Random Values
With some additional advice on the bounds of each random attribute I believe I could generate more real-to-life values and provide additional value.

For example, knowing the minimum and maximum bounds of a widget's price would allow me to ensure random values remain between these bounds.

### Docker
The virtual environment goes some way to isolate the appliation from your system, however this could be improved by using Docker.

Using Docker would allow for all python and system dependencies to be packaged into a container. This container could then be run as an executable.

## Thanks
Thank you for the opportunity to complete this technical test. I look forward to your feedback. Equally, I would be more than happy to share my thoughts on the exercise if this is something of interest.

Thank you.
