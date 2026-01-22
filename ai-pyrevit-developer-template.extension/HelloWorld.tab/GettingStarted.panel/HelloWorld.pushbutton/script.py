#! python
# Minimal Hello World scaffold for validating pyRevit setup.

from pyrevit import forms


def main():
    forms.alert("Hello from the template scaffold.", title="Hello World")


if __name__ == "__main__":
    main()
