import logging
import logstash
import sys 
import time

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('35.171.25.13', 5959, version=1))

def addNumbers(x, y):
    sum = x + y
    return sum

result1 = addNumbers(1, 2)
result2 = addNumbers(2, 3)
result3 = addNumbers(3, 4)
result4 = addNumbers(4, 5)

test_logger.info('Addition result 1: '.format(result1))
test_logger.info('Addition result 2: '.format(result2))
test_logger.info('Addition result 3: '.format(result3))
test_logger.info('Addition result 4: '.format(result4))

# add extra field to logstash message
extra = {
    'test_string' : 'python version: ' + repr(sys.version_info),
    'test_boolean' : True,
    'test_dict' : {'a': 1, 'b': 'c'},
    'test_integer': 126,
    'test_list': [1,2,3],
}
test_logger.info('python-logstash: test extra fields', extra=extra)