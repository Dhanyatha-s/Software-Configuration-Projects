from config_manager import load_config, save_config
from version_control import backup_comfig, rollback_config, list_backups
from database_logger import init_db, log_action
from utils import init_git_repo, commit_changes
import os


def menu():
    print("\n=== ConfigTrack Menu ===")
    print("1. Load & View Config")
    print("2. Modify & save Config")
    print("3. List Backups")
    print("4. Rollback Config")
    print("5. Exit")

def main():
    repo = init_git_repo()
    init_db()
    file_path = input("Enter config file path (JASON/YAML): ")

    while True:
        menu()
        choice = input("Enter the Choice: ")

        if choice == '1':
            try:
                config = load_config(file_path)
                print(config)
            except Exception as e:
                print(f'Error loading Config: (e)')

        
        elif choice == '2':
            try:
                backup_path = backup_comfig(file_path)
                log_action("backup", file_path)
                config = load_config(file_path)
                key = input("Enter config key to modify:  ")
                value = input("Enter new Value: ")
                config[key] = value
                save_config(config, file_path)
                print("saved")
                log_action("edit", file_path)
                commit_changes(repo, f"updated config key: {key}")
                print("Saved and committed Changes")
            except Exception as e:
                print(f"Error modifying config(e)")
                
        
        elif choice == '3':
            backups = list_backups(os.path.basename(file_path))
            print("Backups: ")
            for b in backups:
                print(b)
        elif choice == '4':
            backups = list_backups(os.path.basename(file_path))
            print("Available Backups: ")
            for b in backups:
                print(b)

            chosen = input("Enter backup filename to restore: ")
            rollback_config(file_path, chosen)
            log_action("rollback",file_path)
            print("Rollback Complete.")
        
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
