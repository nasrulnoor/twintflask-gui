#!/usr/bin/env python3
import twint
# Search Input
search = input("Who do you want to search?\n")
c = twint.Config()
c.Search = search

twint.run.Search(c)
