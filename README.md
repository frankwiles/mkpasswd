# mkpasswd

## Overview

A Python 3.7+ command line utility to generate strong passwords quickly from
the commandline.

**NOTE:** This is provided as is and I do not intend to support this outside of my own use.

## Usage

You can run this in a pip environment easily by pip installing it or if you're working on it run `pip install -e .`.

The easiest way to use it is via Docker, so after getting the code just run:

```shell
$ docker build -t mkpasswd .
$ docker run --rm mkpasswd
```

Options are:

- `-s` include symbols in the password
- `-l X` generate a password of length X.  The default is 16 characters
- `-q` just generate the password without any text around it

## Setup Shell alias

To make this the most useful you should setup a shell alias in your shell of choice, for bash that would be adding this
to your `~./bashrc` or `~/.bash_profile`: 

```shell
alias mkpasswd="docker run --rm mkpasswd"
```

## Examples

Default

```shell
$ mkpasswd
--- Generating a strong password of length 16 ---
Xw4152W5wJj2YZg2
---
```

Long

```shell
$ mkpasswd -l 24
--- Generating a strong password of length 24 ---
Hy?U>%i/"RzT%Q,lOFuiu2Io
---
```

Long, No symbols, and Quiet

```shell
$ mkpasswd -l 30 -q
963885FzMLDerFdSxUh5QmuYbpx42o
```

## License

BSD Licensed. However, I do not plan to support this.  It's just a tool I use and find useful.

## Author

[Frank Wiles](https://frankwiles.com) <frank@revsys.com>
