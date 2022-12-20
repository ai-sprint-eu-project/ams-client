# coding: utf-8

EXECUTION_TIME_METRIC_NAME = 'execution_time'

SESSION_ID_TAG_NAME = 'session_id'
KCI_TAG_NAME = 'kubernetes_cluster_id'
RESOURCE_ID_TAG_NAME = 'resource_id'
COMPONENT_NAME_TAG_NAME = 'component_name'

JOB_START_TIME_FIELD_NAME = 'job_start_time'
FUNCTION_START_TIME_FIELD_NAME = 'function_start_time'
JOB_END_TIME_FIELD_NAME = 'job_end_time'

FUNCTION_DURATION_FIELD_NAME = 'function_duration'
JOB_DURATION_FIELD_NAME = 'job_duration'
JOB_OVERHEAD_FIELD_NAME = 'job_overhead'

TELEGRAF_HOST_VARIABLE_NAME = 'MONIT_HOST'
TELEGRAF_PORT_VARIABLE_NAME = 'MONIT_PORT'
TELEGRAF_DEFAULT_HOST = '127.0.0.1'
TELEGRAF_DEFAULT_PORT = 8094

COMPONENT_NAME_VARIABLE_NAME = 'COMPONENT_NAME'

FLUENT_HOST_VARIABLE_NAME = 'MONIT_LOG_HOST'
FLUENT_PORT_VARIABLE_NAME = 'MONIT_LOG_PORT'
FLUENT_DEFAULT_HOST = '127.0.0.1'
FLUENT_DEFAULT_PORT = 24224
FLUENT_DEFAULT_FORMAT = {'host': '%(hostname)s',
                         'name': '%(module)s.%(funcName)s',
                         'level': '%(levelname)s',
                         'stack_trace': '%(exc_text)s'}
