
# NASA HTTP Log Parser

This repository provides an efficient solution for parsing and analyzing NASA HTTP access logs. The project focuses on extracting meaningful insights from raw HTTP logs, including statistics on request counts, IPs, status codes, and error classifications.

## Features
- **Log Parsing**: Extract key information from NASA HTTP access logs.
- **Data Analysis**: Generate useful statistics like request counts, most frequent IPs, and error distributions.
- **Error Classification**: Classify logs based on HTTP status codes.
- **Visualization**: Create insights through data visualization (optional).

## Table of Contents
1. [Installation](#installation)
2. [Files and Directories](#files-and-directories)
3. [External Data](#external-data)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

## Installation

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/yeezerdaw/NASA-HTTP-Log-Parser.git
cd NASA-HTTP-Log-Parser
```

### 2. Setup a Virtual Environment (Recommended)
It's highly recommended to use a virtual environment to manage dependencies.

#### Install `virtualenv` (if not installed):
```bash
pip install virtualenv
```

#### Create and Activate Virtual Environment:
- For Linux/MacOS:
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  ```

- For Windows:
  ```bash
  python -m venv myenv
  myenv\Scripts\activate
  ```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

## Files and Directories

This repository includes several important files and directories:

### Key Directories:
- `scripts/`: Contains Python scripts for parsing and analyzing the logs. Key files include:
  - `nasa_log_parser.py`: Main script for parsing logs and generating statistics.
  - `log_features.py`: Contains features extraction logic.
  
- `datasets/`: Contains data files required for the project. This is where you should place large datasets.

### Key Files:
- `requirements.txt`: Python dependencies needed for the project (listed after setup).
- `README.md`: This documentation file.

### External Data:
Due to GitHub's file size limitations, the following large files are hosted externally on Google Drive:

- [log_features.csv](https://drive.google.com/drive/folders/1_8G0mBQfbl_w0U0Tf_uKd1fsUddaCLCw)
- [access.log](https://drive.google.com/drive/folders/1_8G0mBQfbl_w0U0Tf_uKd1fsUddaCLCw)

#### Important: Place these files in the following directory structure:
1. Download `log_features.csv` and `access.log` from Google Drive.
2. **Place both files in the `datasets/` folder** of the repository.

## Setup Instructions

1. **Clone the repository** (if you haven’t already).
2. **Create and activate a virtual environment** (optional but recommended).
3. **Install required dependencies** by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download external datasets**:
   - Download `log_features.csv` and `access.log` from the provided Google Drive links.
   - **Place both files in the `datasets/` folder**.

## Usage

After setting up the repository and placing the required files in the correct directories, you can start analyzing the logs by running the main parser script:

```bash
python scripts/nasa_log_parser.py
```

This script will:
- Parse the NASA HTTP access log (`access.log`).
- Process the `log_features.csv` to extract relevant features.
- Generate statistics such as request counts, most frequent IPs, error classifications, etc.

### Example Output
- **Request Statistics**: Total number of requests processed.
- **Most Frequent URLs**: List of the most requested URLs.
- **Error Statistics**: Breakdown of HTTP errors by status code.

### Visualization (Optional)
- The project includes optional steps for visualizing the parsed data using `matplotlib` and `seaborn`. This helps in generating plots like error distribution, request counts by status code, and more.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **NASA** for providing the HTTP access logs.
- **Python** community for libraries like `pandas`, `matplotlib`, and `seaborn` that facilitate data manipulation and visualization.
- **Google Drive** for hosting large datasets that exceed GitHub's file size limitations.

## Troubleshooting

### 1. Git Large File Storage (LFS) Issues:
If you encounter issues related to pushing large files (e.g., `log_features.csv` or `access.log`), you can use Git LFS (Large File Storage) to handle large files:
- Install Git LFS:
  ```bash
  git lfs install
  ```

### 2. File Size Limits on GitHub:
GitHub enforces a file size limit of 100MB for each individual file. If your files exceed this size, use external storage (like Google Drive) and provide direct download links as mentioned.

---

Feel free to contribute, submit issues, or provide feedback via GitHub Issues.

```

