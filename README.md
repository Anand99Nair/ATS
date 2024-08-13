## Applicant Tracking System using Google Gemini Pro

# Applicant Tracking System (ATS) using Gemini Pro

## Overview

This project is an Applicant Tracking System (ATS) that utilizes the Gemini Pro language model from Google's Generative AI to evaluate resumes based on a given job description. The system provides a user-friendly interface built with Streamlit, allowing users to upload their resumes in PDF format and paste the job description they are applying for. The Gemini Pro model then analyzes the resume and job description, providing a percentage match, missing keywords, and a profile summary to help users improve their resumes and increase their chances of getting hired.

## Features

- **Resume Evaluation**: The system evaluates the uploaded resume against the provided job description, considering the competitive job market and the need for a strong resume.
- **Percentage Match**: The system calculates the percentage match between the resume and the job description, giving users an idea of how well their resume aligns with the requirements.
- **Missing Keywords**: The system identifies keywords that are missing from the resume but are relevant to the job description, allowing users to update their resumes accordingly.
- **Profile Summary**: The system generates a profile summary based on the resume and job description, providing users with a concise overview of their qualifications and potential fit for the role.
- **User-friendly Interface**: The Streamlit interface makes it easy for users to upload their resumes, paste the job description, and view the evaluation results.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/applicant-tracking-system.git
```

2. Navigate to the project directory:

```bash
cd applicant-tracking-system
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the Google API key:

   - Obtain a Google API key by following the instructions in the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a `.env` file in the project directory and add the following line, replacing `<your-api-key>` with your actual API key:

     ```
     GOOGLE_API_KEY=<your-api-key>
     ```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. In the Streamlit interface, paste the job description in the provided text area.
3. Upload your resume in PDF format using the file uploader.
4. Click the "Submit" button.
5. The system will process your resume and job description, and display the evaluation results, including the percentage match, missing keywords, and a profile summary.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

#
