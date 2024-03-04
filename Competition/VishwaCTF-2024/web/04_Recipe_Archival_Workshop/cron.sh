#!/bin/bash

find uploads/ -type f -cmin +5 -exec rm {} \;