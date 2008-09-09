#!/bin/bash
cd $1
rm -rf ve
python create-ve.py
python ve-bootstrap.py ve
