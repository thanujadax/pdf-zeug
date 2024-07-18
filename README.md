# PDF Zeug

A tool to modify, merge and split PDFs. Currently it only has the merge feature.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/thanujadax/pdf-zeug.git
    cd pdf-zeug
    ```

2. Create and activate a conda environment:

    ```bash
    conda create --name pdf_env python=3.9
    conda activate pdf_env
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the following command to start the PDF merging tool:

```bash
python -m pdf_merger.merge_pdfs
