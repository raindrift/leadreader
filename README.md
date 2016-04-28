# leadreader
Reads leadsheets and analyze them

# Useful tools

- [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) for viewing database contents directly

# Dependencies

- Mongodb: `brew install mongodb`
- [SciPi Superpack](http://stronginference.com/ScipySuperpack/): `sh install_superpack.sh`

Don't have Homebrew? [Get it here](http://brew.sh/)

Installing SciPi takes a long time. Be forewarned.

# Setup for Development

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt
    pip install --editable .

You should be able to run the `leadreader` command in the shell. It should already be available in your path.

# Tests

We're using mamba with expects for unit testing.

To run tests, simply do:

    mamba
