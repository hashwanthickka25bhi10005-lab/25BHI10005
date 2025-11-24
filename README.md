# Oral health analyser
------------------------------------------------
## Overview of the project
This project is a modular Python application. It allows users to upload an oral health image, process it, predict a dental issue, and receive recommendations. It also stores user profiles and past analysis records for future reference.
----------------------------------------------------------------
## Features

User Profile Creation (Name, Age, History)

Image Input & Preprocessing Simulation

Oral Health Analysis Simulation

Automatic Recommendations Based on Detected Issue

Report Generation (issue, confidence, clarity score, advice)

Save & Load User Data (JSON storage)

View Past Records

Simple text-based menu system

## Technologies / Tools Used

Python (Core language)

Built-in modules:

json (for saving/loading data)

random (for simulated scoring)

Modular Programming Concepts

Separate .py files for user, processing, prediction, storage, etc.

No external libraries required.

## Steps to Install & Run the Project

1. Download / Copy All Project Files

Make sure the following files are in the same folder:

main.py  
module1_user.py  
module2_image_processing.py  
module3_prediction.py  
module4_storage.py  
module5_recommendations.py  
module6_report.py  
module7_utils.py  2. Open a Terminal / Command Prompt

2.Navigate to the project folder:

cd path/to/project  


3. Run the main program

python main.py  

4. Follow the On-Screen Instructions

You can:

Analyze new image  
View previous results  
Save and exit  

## Instructions for Testing

To test the project:

1. Start the program

Run:

python main.py  

2. Choose Option 1: Analyze New Image

Enter name, age, and any image path (since processing is simulated).

3. Check if the report prints correctly

See:

Issue  
Confidence  
Clarity  
Recommendation  

4. Choose Option 2: View Previous Records

Ensure the history list displays correctly.

5. Choose Option 3: Save & Exit

Check if oral_health_data.json is created and contains correct values.

## Screenshot
<img width="1665" height="615" alt="image" src="https://github.com/user-attachments/assets/a8938970-0182-4566-b0ee-8826225c360d" />












