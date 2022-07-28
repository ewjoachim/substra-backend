import copy


def orc_to_localrep(data: dict) -> dict:
    """Convert a compute task from the orchestrator format to the localrep format"""

    res = copy.deepcopy(data)
    res["inputs"] = [_input_to_localrep(input) for input in res["inputs"]]
    res["outputs"] = [{"identifier": identifier, **output} for identifier, output in res["outputs"].items()]
    return res


def _input_to_localrep(input: dict) -> dict:
    """Convert a compute task input from the orchestrator format to the localrep format"""

    if "parent_task_output" not in input:
        return input

    return {
        "identifier": input["identifier"],
        "parent_task_key": input["parent_task_output"]["parent_task_key"],
        "parent_task_output_identifier": input["parent_task_output"]["output_identifier"],
    }
