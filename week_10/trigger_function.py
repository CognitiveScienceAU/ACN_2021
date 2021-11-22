import numpy as np


def convert_triggers(events, return_event_ids=False):
    """Function to convert triggers to failed and successful inhibition.

    Trigger codes:
    stop_signal: 11,
    go: 10,
    response: 1,
    stop_signal_only: 12,
    failed_inhibition_response: 2,
    failed_inhibition: 37,
    successful_inhibition: 35

    Parameters
    ----------
    events : numpy array
        The original events
    return_event_id: bool
        If true return event_id that matches the new triggers.

    Returns
    -------
    converted_events
        The converted events.
    """
    events_tmp = events.copy()
    for idx, line in enumerate(events_tmp):
        if line[2] == 20:
            if events_tmp[idx + 1][2] == 1:
                events_tmp[idx][2] = 30  # go_before_stop
            elif (events_tmp[idx + 1][2] == 11) and (events_tmp[idx + 2][2] != 1):
                events_tmp[idx][2] = 35  # successful inhibition
            elif (events_tmp[idx + 1][2] == 11) and (events_tmp[idx + 2][2] == 1):
                events_tmp[idx][2] = 37  # failed inhibition
                events_tmp[idx + 2][2] = 2  # failed inhibition response

    event_id = {
        "stop_signal": 11,
        "go": 10,
        "response": 1,
        "stop_signal_only": 12,
        "failed_response": 2,
        "failed_inhibition": 37,
        "successful_inhibition": 35,
    }

    if return_event_ids:
        return (
            events_tmp,
            event_id,
        )
    else:
        return events_tmp
