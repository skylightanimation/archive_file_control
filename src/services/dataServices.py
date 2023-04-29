from flask import render_template, request, redirect, flash, url_for
from app import app

from datetime import datetime
import locale

import sys
sys.path.append('../')


# from services.scrapy import ScrapyHandler