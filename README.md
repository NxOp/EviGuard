* EviGuard - Digital Evidence Chain of Custody Tool*

**Description:**

**EviGuard** is a Python-based tool designed to facilitate the tracking and maintenance of the chain of custody for digital evidence, ensuring its integrity and admissibility in legal proceedings. This powerful tool combines user-friendly functionality with advanced security features to streamline the process of handling and recording digital evidence. EviGuard is an essential asset for law enforcement agencies, legal professionals, and digital forensics experts who need to maintain a reliable and tamper-evident record of digital evidence throughout its lifecycle.

**Prerequisites:**

Before using **EviGuard**, ensure that you meet the following prerequisites and requirements:

1. **Python 3:** EviGuard is written in Python, so you need Python 3 installed on your system. You can download Python from the official website (https://www.python.org/downloads/) and follow the installation instructions.

2. **Colorama Library:** EviGuard uses the Colorama library for ANSI color codes to provide a visually appealing and user-friendly interface. Install Colorama using the following command:

   ```bash
   pip install colorama
   ```

3. **Operating System:** EviGuard is designed to work on both Windows and Unix-like systems (Linux and macOS). Ensure you have a compatible operating system.

**How to Use EviGuard:**

1. **Installation:**
   - Download the EviGuard tool from the official repository (provide the link to your repository).
   - https://github.com/NxOp/EviGuard

2. **Setup:**
   - Extract the tool to a directory of your choice.
   - Ensure you have a directory named "evidence" in the same location as the tool. This directory will be used to store digital evidence files.

3. **Launching EviGuard:**
   - Open a terminal or command prompt.
   - Navigate to the directory where EviGuard is located.

4. **Running EviGuard:**
   - Execute the `main.py` script to start the tool.

   ```bash
   python main.py
   ```

5. **Using EviGuard:**
   - Upon launching, EviGuard will display an eye-catching ASCII art banner.
   - Choose from the following options by entering the corresponding number:
     - **Option 1: Record Chain of Custody**
       - Enter the name of the digital evidence file you want to record.
       - EviGuard will calculate the SHA-256 hash of the file, record the custody information, and pause for you to press Enter to continue.
     - **Option 2: Verify Chain of Custody**
       - Enter the name of the digital evidence file you want to verify.
       - EviGuard will display the latest custody record for the specified evidence file, including the timestamp, file name, and hash.
     - **Option 3: Exit**
       - Choose this option to exit EviGuard.

6. **Security and Compliance:**
   - EviGuard ensures the integrity of digital evidence through secure hashing and maintains a tamper-evident record.
   - It complies with legal requirements and provides a clear audit trail for use in legal proceedings.

7. **Advanced Features:**
   - EviGuard can be further customized and enhanced to meet specific organizational and legal requirements, including user authentication, encryption, and more.

**EviGuard** simplifies the process of managing digital evidence, making it a crucial tool for legal professionals, digital forensics experts, and law enforcement agencies. By providing a user-friendly interface and robust security features, it helps ensure the integrity and admissibility of digital evidence in a wide range of legal proceedings.
