#!/bin/bash

# --- LaTeX Automation Toolkit: Master Test Script ---
# This script navigates into each project folder, runs the 
# necessary Python/LaTeX commands, and verifies the output.

echo "🚀 Starting Master Toolkit Test..."
echo "---------------------------------------"

# 1. Automated Invoice
echo "📂 Testing 01-Automated-Invoice..."
cd 01-Automated-Invoice && python3 generate_invoices.py && cd ..

# 2. Automated Mail Merge
echo "📂 Testing 02-Automated-Mail-Merge..."
cd 02-Automated-Mail-Merge
pdflatex -interaction=batchmode certificates.tex > /dev/null
pdflatex -interaction=batchmode certificates.tex > /dev/null
cd ..

# 3. Exam Generator
echo "📂 Testing 03-Exam-Generator..."
cd 03-Exam-Generator && pdflatex -interaction=batchmode master_exam.tex > /dev/null && cd ..

# 4. Data-Driven Reports
echo "📂 Testing 04-Data-Driven-Reports..."
cd 04-Data-Driven-Reports && python3 generate_data.py && pdflatex -interaction=batchmode report.tex > /dev/null && cd ..

echo "---------------------------------------"
echo "✅ All tests complete! Check each folder for the generated PDFs."
