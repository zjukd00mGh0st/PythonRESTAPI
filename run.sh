#!/bin/bash

gunicorn --config gunicorn.conf.py "src.app:app"