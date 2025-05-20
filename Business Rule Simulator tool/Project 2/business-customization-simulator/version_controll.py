# Initialize a Git repo in the project root (if not already)

# Commit any changes to config files to a branch

# Allow rollback to previous versions

import os
import subprocess

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def git_init():
    if not os.path.exists(os.path.join(REPO_DIR, '.git')):
        subprocess.run(["git", "init"], cwd=REPO_DIR)
        subprocess.run(["git", "config", "user.name", "DhanyathaS"], cwd=REPO_DIR)
        subprocess.run(["git", "config", "user.email", "yashu.m.k7@gmail.com"], cwd=REPO_DIR)

def git_commit(file_path, message="Auto backup"):
    git_init()

    # Convert file path to relative to REPO_DIR
    rel_path = os.path.relpath(file_path, REPO_DIR)

    try:
        # Ensure the file is added (even if untracked)
        subprocess.run(["git", "add",".",rel_path], cwd=REPO_DIR, check=True)

        # Only commit if there is something to commit
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_DIR,
            capture_output=True,
            text=True
        )

        if status_result.stdout.strip():  # there are changes to commit
            subprocess.run(["git", "commit", "-m", message], cwd=REPO_DIR, check=True)
            print(f"✅ Git commit successful: {message}")
        else:
            print("⚠️ Nothing new to commit.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git commit failed: {e}")

def git_log():
    git_init()
    result = subprocess.run(["git", "log", "--oneline"], cwd=REPO_DIR, capture_output=True, text=True)
    return result.stdout.strip()

def git_checkout(commit_hash):
    git_init()
    try:
        subprocess.run(["git", "checkout", commit_hash], cwd=REPO_DIR, check=True)
        print(f"✅ Checked out to {commit_hash}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Checkout failed: {e}")
