# leadreader

[![CircleCI](https://circleci.com/gh/raindrift/leadreader.svg?style=svg&circle-token=4d5fadd2ea005b0aa3af46e1a58f40c857d26eec)](https://circleci.com/gh/raindrift/leadreader)

Reads and analyzes leadsheets.

# Useful tools

- [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) for viewing database contents directly

# Dependencies

- Mongodb: `brew install mongodb`
- [SciPi Superpack](http://stronginference.com/ScipySuperpack/): `sh install_superpack.sh`
- Python3+

Don't have Homebrew? [Get it here](http://brew.sh/)

Installing SciPi takes a long time. Be forewarned.

### For ArchLinux:

Install Mongodb with `pacman -S mongodb` then `systemctl start mongodb.service`.

# Setup for Development

    # To ensure Python3: virtualenv -p python3 env
    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt
    pip install --editable .

You should be able to run the `leadreader` command in the shell. It should already be available in your path.

# Tests

We're using mamba with expects for unit testing.

To run tests, simply do:

    mamba
