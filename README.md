# ATC Chain

> Implements a proof of concept beacon chain for a sharded pos atc chain. Spec in progress can be found [here](https://github.com/atcswap/atc_chain).

## Installation
Using a python3.6.* environment, run the following to install required libraries:
```
pip install -e .[dev]
```

NOTE: We suggest using virtualenv to sandbox your setup.

## Tests
```
pytest tests
```

Run with `-s` option for detailed log output


## Installation through Docker
```
make build

make deploy
```

---

# Simple Serialize
[here](https://github.com/atcswap/atc_chain/tree/master/ssz)
