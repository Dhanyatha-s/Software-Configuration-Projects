# main.py
import json
import os
from config_manager import load_config, save_config
from rules_engine import apply_rules
from version_controll import git_commit
from database_logger import init_db, log_rules_application, log_config_change
from utils import initialize

# Absolute path to project directory (where the script resides)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the config template (you can keep this as is if you want it hardcoded)
CONFIG_PATH = os.path.join(PROJECT_DIR, "config_templates", "hr_config_template.json")

# Backups folder *inside the project folder*
BACKUP_DIR = os.path.join(PROJECT_DIR, "backups")

# Ensure backups folder exists
os.makedirs(BACKUP_DIR, exist_ok=True)

def main():
    initialize()
    init_db()

    # Load base config
    config = load_config(CONFIG_PATH)

    # Example employee data, in real case, input or API
    employee = {
        "department": "Engineering",
        "country": "Germany",
        "role_level": "Senior",
        "employment_type": "Full-time",
        "tenure_years": 3,
        "performance_rating": 4.8,
        "on_probation": False
    }

    # Apply rules and get updated config
    updated_config = apply_rules(config, employee)

    output_path = os.path.join(BACKUP_DIR, "hr_config_updated.json")
    save_config(updated_config, output_path)

    git_commit(output_path, f"Updated config for employee {employee['department']}")

    log_rules_application(employee, updated_config.get("rules", []))
    log_config_change(output_path, message="Config updated after rule application")

    print(f"Updated config saved to {output_path}")


if __name__ == "__main__":
    main()
