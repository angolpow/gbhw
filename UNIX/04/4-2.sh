#!/usr/bin/env bash

tailf -0 /var/log/secure | egrep '[Ff]ail'
