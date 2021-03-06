'''Constant values for Wolverine Lambda'''
from xlibs.constants import *  # NOQA


REQUIRED_ARGS = [
    'name',
    'region',
]

# Parameters to gather Lambda metrics from CloudWatch
METRICS_MAX_DATAPOINTS = 1000
METRICS_TIME_PERIOD = 300  # Seconds
METRICS_DAYS_AGO = 3

if METRICS_DAYS_AGO * 3600 / METRICS_TIME_PERIOD * 24 > METRICS_MAX_DATAPOINTS:
    raise ValueError(
        'The value of METRICS_DAYS_AGO * 3600 / METRICS_TIME_PERIOD * 24 must '
        'be lower than the value of METRICS_MAX_DATAPOINTS.'
    )

# Startup time sensitivity coefficients
STARTUP_TIME = {
    'csharp': {
        'intercept': 11.66002128,
        'x': -0.646476376,
    },
    'java': {
        'intercept': 13.07755393,
        'x': -0.939170773,
    },
    'nodejs': {
        'intercept': 10.94274242,
        'x': -1.361245192,
    },
    'python': {
        'intercept': 6.163939579,
        'x': -0.600820477,
    },
    'default': {
        'startup_time': 10000,
        'vpc_overhead': 8000,  # Milliseconds
    },
}
