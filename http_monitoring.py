#! /usr/bin/env python3

import http_monitoring
import sys

cli = http_monitoring.Cli(sys.argv[1:])
cli.run()