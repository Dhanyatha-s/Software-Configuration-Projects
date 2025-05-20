# This module will:
# - Take loaded config JSON and employee data
# - Loop through all "rules" in the config
# - Evaluate conditions per rule (supports: equals, gte, lte, all/and)
# - Apply actions to the config when conditions match

import copy

def evaluate_condition(condition, employee):
    """
    Recursively evaluate the condition dict against employee data.
    Supports:
        - equals: value equality
        - gte: greater than or equal
        - lte: less than or equal
        - all: list of AND conditions
    """
    if 'all' in condition:
        return all(evaluate_condition(sub_condition, employee) for sub_condition in condition['all'])

    field = condition.get('field')
    if not field or field not in employee:
        return False

    value = employee[field]

    if 'equals' in condition:
        return value == condition['equals']
    if 'gte' in condition:
        return value >= condition['gte']
    if 'lte' in condition:
        return value <= condition['lte']

    return False

def apply_actions(config, actions):
    """
    Recursively merge the actions dict into the config dict.
    Overwrites existing values or adds new keys.
    """
    for key, value in actions.items():
        if (
            isinstance(value, dict)
            and key in config
            and isinstance(config[key], dict)
        ):
            apply_actions(config[key], value)
        else:
            config[key] = value

def apply_rules(config, employee):
    """
    Applies all rules defined in config["rules"] to a deep copy of the config
    based on employee attributes. Returns the updated config.
    """
    updated_config = copy.deepcopy(config)  # Don't mutate original config
    rules = updated_config.get("rules", [])

    for rule in rules:
        condition = rule.get("condition", {})
        actions = rule.get("actions", {})
        if evaluate_condition(condition, employee):
            apply_actions(updated_config, actions)

    return updated_config
