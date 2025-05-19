from  git import Repo
import os

def init_git_repo(repo_path='.'):
    if not os.path.exists(os.path.join(repo_path, '.git')):
        Repo.init(repo_path)

        print("Git Repository Initialized")
    return Repo(repo_path)

def commit_changes(repo, message="Config Updates"):
    repo.git.add('--all')
    repo.index.commit(message)
    print(f"Commited: {message}")