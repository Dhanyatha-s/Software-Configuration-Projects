# Business  Rule Simulator Tool. (HR RULE ENGINE)
<p align="center">
  <img src="https://github.com/user-attachments/assets/46a72044-6476-476d-afad-2d877b52edbd" width="45%" style="margin-right: 10px;" />
  <img src="https://github.com/user-attachments/assets/dadaec57-3fe1-4104-9b51-2ded1f860b9f" width="45%" />
</p>


## Overview

The **Business Customization Simulator** is a flexible HR configuration tool built with **Streamlit** and optional **Flask CLI integration**, designed to simulate dynamic business logic rules based on employee data. This project enables HR departments, business analysts, and system integrators to create, test, and apply rule-based configurations on-the-fly using a JSON-driven rules engine.

---

##  Features

- 📄 Upload custom JSON rule configurations.
- 🧠 Apply dynamic business rules based on employee attributes (e.g., department, experience, location).
- 📥 Download curated configurations in JSON or summary text format.
- 📊 Intuitive Streamlit-based UI for non-technical users.
- 🖥️ CLI interface (via Flask) for backend integrations or automation.
- 🔒 Follows real-world standards for business process simulations.
- 💾 Supports versioned backups of configurations.

---

##  Real-World Use Cases

| Industry       | Use Case Example                                                   |
|----------------|---------------------------------------------------------------------|
| HR Tech        | Auto-assign benefits, leave policies, or onboarding tasks          |
| SaaS Platforms | Customize user experiences or features based on profile tiers      |
| FinTech        | Apply credit rules or dynamic eligibility conditions               |
| Gov/Policy     | Simulate rule-based decision systems for social programs           |

---

##  Tech Stack

- **Python 3.10+**
- **Streamlit** - for the front-end simulation UI
- **Flask (optional)** - for CLI/API interface
- **JSON** - as the rules engine configuration format

---

## 📁 Project Structure

```
business-customization-simulator/
├── streamlit_app.py          # Main Streamlit interface
├── rules_engine.py           # Core logic for evaluating and applying rules
├── employee_form.py          # Streamlit form UI for employee inputs
├── cli_app.py                # Flask-based CLI/API (optional)
├── backups/                  # Saved configurations
├── example_rules.json        # Sample rule configuration
└── README.md                 # This file
```

---

##  Running the Application

### 🔹 Option 1: Using Streamlit UI (Recommended)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### 🔹 Option 2: Using CLI (Flask based)

```bash
pip install Flask
python cli_app.py --config example_rules.json --employee_data '{"role": "manager", "location": "india"}'
```

> 🔧 `cli_app.py` allows you to apply rules from terminal or backend pipelines (e.g., cron jobs, CI/CD).

---

##  How It Works

1. **Upload** a rules configuration file (`rules.json`) through the UI.
2. **Input** employee-specific data using the provided form (department, role, experience, etc.).
3. **Apply Rules**: The system evaluates conditions in the rules and merges the `actions` if matched.
4. **Download** the final configuration or the textual summary for audits and deployment.

---

##  Example Rule (JSON)

```json
{
  "rules": [
    {
      "condition": {
        "all": [
          { "field": "role", "equals": "manager" },
          { "field": "experience", "gte": 5 }
        ]
      },
      "actions": {
        "benefits": {
          "leave_days": 30,
          "bonus": "15%"
        }
      }
    }
  ]
}
```

---

##  Output Example

```json
{
  "benefits": {
    "leave_days": 30,
    "bonus": "15%"
  }
}
```

**Text Summary:**
```
 Applied 1 rule:
- Manager with 5+ years: granted 30 leave days and 15% bonus.
```

---

##  Industry Benefits

- ✔️ **Modularity**: Easily add/edit rules without changing application code.
- ✔️ **Transparency**: Generates a readable summary of which rules were applied.
- ✔️ **Scalability**: Works across departments or business units with different rule sets.
- ✔️ **Audit-Ready**: Download and store versioned configurations for compliance.
- ✔️ **Non-Technical Friendly**: Intuitive interface for HR/business teams to test logic.

---

##  Testing

Basic test cases can be written using `pytest` to validate:
- Rule application logic
- Invalid/missing fields
- Backup file generation

```bash
pip install pytest
pytest tests/
```

---

##  Future Enhancements

- 🧩 Rule testing sandbox for advanced what-if analysis
- 🧠 Integration with LLMs to generate rules from plain English
- ☁️ Cloud-based version with user login and saved sessions
- 🪄 Visual editor for rule creation

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

1. Clone the repo
2. Create a branch (`git checkout -b feature-x`)
3. Commit your changes
4. Push and submit a PR

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Contact

For questions, suggestions, or collaborations:

**Dhanyatha**  
📧 dhanyatha237.y@gmail.com  
🌐 [LinkedIn](https://linkedin.com/in/dhanyatha)

---



