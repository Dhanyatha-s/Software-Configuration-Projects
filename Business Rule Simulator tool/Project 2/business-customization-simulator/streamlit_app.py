import streamlit as st
import json
from datetime import datetime, timezone
from rules_engine import apply_rules
from employee_form import get_employee_input

st.set_page_config(page_title="HR Business Rule Simulator", layout="centered")
st.title("HR Business Rule Simulator")

# Sidebar for file upload
with st.sidebar:
    st.markdown("### Upload Rules Configuration")
    config_file = st.file_uploader("Upload Rules JSON", type=["json"])

# Employee input section
st.markdown("###  Employee Profile")
employee_data = get_employee_input()

# Apply button
apply_btn = st.button("Apply Rules")

# Global placeholders
updated_config = None
summary_text = ""

if config_file is not None and apply_btn:
    try:
        config = json.load(config_file)
        updated_config = apply_rules(config, employee_data)

        # Show final config
        with st.expander("✅ Final Configuration (Click to Expand/Collapse)"):
            st.json(updated_config)


        # Generate readable rule summary
        summary_text += "**📋Employee Rule Summary:**\n\n"
        for k, v in employee_data.items():
            summary_text += f"- `{k}`: **{v}**\n"

        summary_text += "\n**🔧 Applied Configuration:**\n"
        for section, items in updated_config.items():
            if section != "rules":
                summary_text += f"\n**{section.capitalize()}**\n"
                if isinstance(items, dict):
                    for key, val in items.items():
                        summary_text += f"  - {key}: `{val}`\n"
                else:
                    summary_text += f"  - {items}\n"

        st.markdown(summary_text)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="📥 Download Curated JSON",
                data=json.dumps(updated_config, indent=4),
                file_name=f"curated_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

        with col2:
            st.download_button(
                label="📄 Download Summary Text",
                data=summary_text,
                file_name=f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )


    except Exception as e:
        st.error(f"Error while applying rules: {e}")

# Manual backup option
if updated_config and st.button("💾 Save Local Backup"):
    now = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"backups/hr_config_{now}.json"
    with open(filename, 'w') as f:
        json.dump(updated_config, f, indent=4)
    st.success(f"Saved to `{filename}`")
