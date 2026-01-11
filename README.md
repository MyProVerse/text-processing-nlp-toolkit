# Text Processing & NLP Data Cleaning Toolkit

A Python-based data cleaning and text processing toolkit developed for big data applications. This project demonstrates text preprocessing techniques using regular expressions, NLTK, and pandas for cleaning textual data.

## Project Overview

This project was developed as part of the **Programming for Big Data** course in Spring 2023. It implements a data cleaning pipeline that processes text data using pandas DataFrames and regular expressions.

## Features

The toolkit implements 11 text processing functions:

1. **Email Removal**: Removes .pk domain emails using pattern `\w+@\w+\.\w+\.pk`
2. **URL Removal**: Removes HTTP/HTTPS URLs using pattern `https?://\S+`
3. **Phone Number Validation**: Extracts phone numbers in format `\d{4}-\d{7}`
4. **Case Conversion**: Finds words starting with capital letters using `\b[A-Z][a-zA-Z]*\b` and converts to lowercase
5. **Text Replacement**: Replaces "ucp" with "University of Central Punjab"
6. **Number Removal**: Removes all numbers using pattern `\d+`
7. **HTML Tag Removal**: Removes HTML tags from text
8. **Word Pattern Extraction**: Extracts words ending with "ing"
9. **Whitespace Removal**: Removes whitespace characters
10. **Lemmatization with POS Tagging**: Uses NLTK WordNetLemmatizer
11. **Text Classification**: Classification approach implementation

## Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation
- **NLTK** - Natural Language Processing
- **Regular Expressions (re)** - Pattern matching
- **Jupyter Notebook** - Development environment

## Project Structure

```
project/
├── BigDataProject.ipynb    # Main implementation
├── BigDataProject.csv      # Dataset (58 records)
├── Project.docx           # Documentation
└── README.md              # Project documentation
```

## Dataset

The CSV dataset contains 58 records with columns:
- **Name**: Person names
- **Email**: Email addresses (including .pk domains)
- **Phone**: Phone numbers in format XXXX-XXXXXXX
- **Text**: Sample text for processing

## Getting Started

### Prerequisites

```bash
pip install pandas nltk jupyter
```

### NLTK Setup

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

### Running the Project

1. Open `BigDataProject.ipynb` in Jupyter Notebook
2. Run all cells to execute the data cleaning pipeline

## Implementation Details

Each cleaning function:
- Takes text as input parameter
- Uses specific regex patterns for processing
- Returns cleaned text
- Applied to DataFrame using `.apply()` method

### Key Functions

- `remove_email()` - Removes .pk emails
- `remove_url()` - Removes URLs
- `check_phone_number()` - Validates phone format
- `convert_to_lowercase()` - Converts capitals to lowercase
- `replace_words()` - Replaces UCP with full name
- `remove_numbers()` - Strips numeric characters

## Contributors

- Ali Zaman (L1F21BSCS1119)
- Umer Tahir (L1F21BSCS0378)
- Lajwer Liaquat (L1F21BSCS0821)

## Academic Context

Completed for Programming for Big Data course, demonstrating:
- Regular expression usage
- NLTK library implementation
- Pandas DataFrame operations
- Text preprocessing techniques

---

*Developed in Spring 2023*