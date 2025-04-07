#!/usr/bin/env python3

import logging
import time

logging.basicConfig(filename='my_script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Script started.')

# My logic
logging.info('Sleeping for 5 seconds...')
time.sleep(5)  # Pause for 5 seconds

logging.info('Resuming after sleep.')

logging.info('Data processing complete.')