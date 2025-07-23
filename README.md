
# 📝 Dolce Vita Restaurant Review Analysis

This project analyzes customer reviews of Dolce Vita, a restaurant, to gain insights into customer satisfaction through sentiment analysis and aspect-based opinion mining. The focus is on identifying key issues from low-rated reviews and evaluating aspects like food, service, ambiance, and value.

---

## 🎯 Research Questions

1. **What are the most common themes in low-rated customer reviews for Dolce Vita?**
2. **How are the sentiments distributed across aspects such as food, service, ambiance, and value in poor reviews?**
3. **Can we quantify sentiment polarity for each aspect in negative reviews using TextBlob?**
4. **What text-cleaning and preprocessing steps are necessary for reliable sentiment and aspect analysis of restaurant reviews?**

---

## 📁 Repository Contents

- `Research_Question_1.ipynb` – Exploratory analysis of review data and aspect identification.
- `Research_Question_2.py` – Aspect-based sentiment analysis on low-rated reviews using TextBlob.
- `Research_Question_3.ipynb` – Visualization and polarity aggregation by aspect.
- `Research_Question_4.ipynb` – Additional modeling or classification steps (e.g., topic clustering).
- `code for cleaning proj dataset.py` – Cleans text data and standardizes ratings.
- `Data_Cleaning.py` – Further preprocessing: location parsing, date formatting, text normalization.
- `Dolce Vita Reviews.csv` – Raw customer review dataset.
- `Cleaned_Dolche_Vita_Reviews.csv` – Final cleaned version used for sentiment analysis.
- `FinalProjectPaper_Team9_AIT582.pdf` – Full project report with methodology, analysis, and visual results.

---

## 🔍 Key Insights

- **Service** had the most negative sentiment polarity among all aspects in low-rated reviews.
- **Food** was mentioned most frequently, with mostly neutral-to-negative sentiment scores.
- Many low-rated reviews emphasized **delays in service**, **bland food**, and **poor value for money**.
- **Aspect frequencies** showed:
  - `Food`: 144 mentions
  - `Service`: 93 mentions
  - `Ambiance`: 67 mentions
  - `Value`: 89 mentions
- **Average sentiment polarity** (range: -1 to 1):
  - `Service`: -0.31 (most negative)
  - `Food`: -0.22
  - `Value`: -0.25
  - `Ambiance`: -0.18

---

## 🛠️ Technologies Used

- **Python**: pandas, matplotlib, re, TextBlob
- **Jupyter Notebook** & `.py` scripts
- **Natural Language Processing**: Tokenization, polarity scoring, keyword extraction

---

## 📊 Visualizations

- Bar chart of aspect keyword frequency from negative reviews
- Bar chart of average sentiment polarity for each aspect
- Word clouds and additional visuals for qualitative insights

---

## 📜 Sample Output

```python
Aspect Counts: {'food': 144, 'service': 93, 'ambiance': 67, 'value': 89}
Average Aspect Sentiments: {'food': -0.22, 'service': -0.31, 'ambiance': -0.18, 'value': -0.25}
