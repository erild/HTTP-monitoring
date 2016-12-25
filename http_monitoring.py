import http_monitoring
import sys

cli = http_monitoring.Cli(sys.argv)
# cli = http_monitoring.Cli({'logfile':'file.log', 'threshold': 3})
cli.run()