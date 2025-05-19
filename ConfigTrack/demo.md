# ConfigTrack - Configuration Management system  
### ConfigTrack is a simple Streamlit-based Software Configuration Management tool that allows developers and configuration engineers to manage JSON/YAML configuration files, track version changes, create backups, and roll back to previous versions — all with Git and database logging support.

- Configuration Managemnet: **It's a process of systematically handelling changes to ensure software integrty over time**
- its both application and CLI Interface Module
- Here is the demo!!
  
![config manager](https://github.com/user-attachments/assets/e33bd123-0e53-4b1a-9fb4-6c1e340baa6e)

Features
- Load & view config files (JSON/YAML)  

- Modify and save configuration entries  

- Backup before changes  

- Rollback to previous backup  

- Git integration for version tracking  

- SQLite logging of every action  

- Streamlit-powered clean UI

## User Flow Diagram
```
 [Start]
    |
    v
[Enter Config File Path]
    |
    v
[Main Menu (Select Action)]
    |
    +-------------------------------+----------------------------+---------------------------+--------------------+
    |                               |                            |                           |                    |
    v                               v                            v                           v                    v
[Load & View Config]      [Modify & Save Config]      [List Backups]          [Rollback Config]         [Exit]
    |                               |                            |                           |
    v                               v                            v                           v
[View Config as JSON]     [Show Current Key]          [Display Backup List]  [Select from List]
                                |                                         |                           |
                                v                                         |                           v
                     [Modify & Save New Value]                            |                 [Restore Config File]
                                |                                         |                           |
                                v                                         |                           v
        [Log to DB] → [Create Backup] → [Commit to Git]         [Optional Git View]      [Log & Commit to Git]
                                |
                                v
                         [Confirmation]

```
## System  Architecture
```
               +-------------------+
               |     User (UI)     |
               | Streamlit Web App|
               +-------------------+
                        |
                        v
            +------------------------+
            |  Application Logic     |
            | streamlit_app.py       |
            +------------------------+
                        |
     +------------------+----------------------+
     |                  |                      |
     v                  v                      v
[Config Manager]   [Version Control]   [Database Logger]
(load/save files)  (backup/rollback)  (SQLite logging)
(config_manager.py) (version_control.py) (database_logger.py)

                        |
                        v
               +--------------------+
               | File System (Disk) |
               |  - JSON/YAML Files |
               |  - Backup Folder   |
               +--------------------+

                        |
                        v
               +--------------------+
               | Git Integration    |
               | (utils.py - GitPython) |
               +--------------------+

                        |
                        v
              +---------------------+
              | Git Repository (.git)|
              | Tracks versioned    |
              | changes to configs  |
              +---------------------+

```
### Setup Instructions
Folder Structure  
```
ConfigTrack/  
│  
├── configs/              # Sample JSON/YAML config files  
├── backups/              # Auto-generated backups    
├── config_manager.py     # Load/Save config logic  
├── version_control.py    # Backup/Rollback logic  
├── database_logger.py    # SQLite logger  
├── utils.py              # Git init and commit  
├── streamlit_app.py      # Streamlit UI (main entry)  
└── requirements.txt
```

Tech Stacks/Libraries/packages:
| Layer                | Tech / Tools                    |
| -------------------- | ------------------------------- |
| **UI**               | Streamlit                       |
| **Backend Logic**    | Python                          |
| **Config Parsing**   | `json`, `yaml` modules          |
| **Version Control**  | Git via `GitPython`             |
| **File Backups**     | Filesystem (timestamped copies) |
| **Database Logging** | SQLite3                         |
- shutil: module which offers high-level file oparations on files & collection of files, supports to the file copying and 
#### Sample.json
```
{
  "host": "localhost",
  "port": 8080,
  "debug": true
}

```
Installation 
```
# Clone the repo
git clone https://github.com/Dhanyatha-s/Software-Configuration-Projects.git
cd Software-Configuration-Projects/ConfigTrack

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```
Run the App
```
streamlit run app.py
```



