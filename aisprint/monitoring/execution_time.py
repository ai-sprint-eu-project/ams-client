# coding: utf-8

from numbers import Real

from ._constants import (EXECUTION_TIME_METRIC_NAME, SESSION_ID_TAG_NAME,
                         KCI_TAG_NAME, RESOURCE_ID_TAG_NAME,
                         COMPONENT_NAME_TAG_NAME, JOB_START_TIME_FIELD_NAME,
                         FUNCTION_START_TIME_FIELD_NAME,
                         JOB_END_TIME_FIELD_NAME, FUNCTION_DURATION_FIELD_NAME,
                         JOB_DURATION_FIELD_NAME, JOB_OVERHEAD_FIELD_NAME)
from ._utils import get_telegraf_client


def report_execution_time_metrics(
    session_id: str,
    kubernetes_cluster_id: str,
    resource_id: str,
    component_name: str,
    job_start_time: Real,
    function_start_time: Real,
    job_end_time: Real
) -> None:

    tags = {SESSION_ID_TAG_NAME: session_id,
            KCI_TAG_NAME: kubernetes_cluster_id,
            RESOURCE_ID_TAG_NAME: resource_id,
            COMPONENT_NAME_TAG_NAME: component_name}

    values = {JOB_START_TIME_FIELD_NAME: job_start_time,
              FUNCTION_START_TIME_FIELD_NAME: function_start_time,
              JOB_END_TIME_FIELD_NAME: job_end_time,
              FUNCTION_DURATION_FIELD_NAME: (
                  job_end_time - function_start_time
              ),
              JOB_DURATION_FIELD_NAME: (
                  job_end_time - job_start_time
              ),
              JOB_OVERHEAD_FIELD_NAME: (
                  function_start_time - job_start_time
              )}

    telegraf_client = get_telegraf_client(tags=tags)
    telegraf_client.metric(EXECUTION_TIME_METRIC_NAME, values)
