
# React Project Automation Tests

This repository contains an automated test suite for a React-based application, using:

- **Selenium** for UI tests
- **Pytest** for API and functional testing
- **GitHub Actions** for CI/CD integration

---

## 📁 Project Structure
├── backend_base_functions/ # API interaction helpers
├── base_pages/ # Selenium page objects
├── test_cases/ # UI and API test cases
│ ├── frontend/
│ └── backend/
├── test_data/ # Input data for tests
├── configurations/ # Constants/configs
├── utilities/ # Reusable utility functions
├── requirements.txt # Python dependencies
└── .github/workflows/ # GitHub Actions CI pipelines

---

## ⚙️ Setup Instructions

> Tested with Python 3.10+

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

python -m venv testvenv
# Windows
testvenv\Scripts\activate
# macOS/Linux
source testvenv/bin/activate

pip install -r requirements.txt

pytest test_cases/frontend/

pytest test_cases/backend/
