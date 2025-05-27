# Algorithms and Data Structures on Python implemented, tested and documented

All folders' and files' places are given as if you are in Algorithms-master
folder.

All source code is inside the `./Algorithms_Python/` folder
and can be imported with statement

```python
from Algorithms_Python.<filename>... import ...
```

provided you are inside `Algorithms_Python-master/` or this folder is added
to your PYTHONPATH by

```python
import sys

sys.path.append('path/to/Algorithms_Python-master/')
```

or any other way.

Table of contents is
[here](./Algorithms_Python/docs/Table_of_contents.md).

All documentation is within the source code so that it automatically loads by
any decent IDE. In Vim works perfectly :)

All tests are inside `./tests/`, examples of usage are also there.

For sorts and some interesting data types performance tuning and comparing
to python standard ones can be found in
[here](./Algorithms_Python/speed_tuning/README.md).

Virtual environment made by venv with requirements for python listed in
`requirements.txt`

Tests are performed by pytest.

Tests coverage checked by

```bash
coverage run
```

Security issues discovered by

```python
bandit -r ./Algorithms_Python -b bandit.json
```

Baseline for bandit was generated using

```bash
bandit -r ./Algorithms_Python -f json -o bandit.json
```

Documentation coverage is checked by

```bash
interrogate ./Algorithms_Python -vv
```

All configs are in `setup.cfg`.

Workflows are set using Github Actions with
`./.github/workflows/python-app.yml` file

## TODOs

- implement algorithms for strings
- implement parser (maybe even interpreter)
- implement a library for topology (geometry)

## Contact

[baravoi.ivan@gmail.com](mailto:baravoi.ivan@gmail.com)
