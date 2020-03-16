#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging
logging.basicConfig(filename='example.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)

logging.warning('Watch out!')
a=2
logging.info('I told you so %s', (a))