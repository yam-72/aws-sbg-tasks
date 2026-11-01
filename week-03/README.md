# Week 03: Break the Spam Filter

## Overview

This project evaluates a simple machine-learning spam classifier using the SMS Spam Collection dataset. I trained a Multinomial Naive Bayes model with TF-IDF text features, measured its performance, and tested five custom messages designed to expose possible classification mistakes.

## Dataset

- **Name:** SMS Spam Collection
- **Source:** [UCI Machine Learning Repository — SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection)
- **Total messages:** 5,574
- **Labels:** `ham` (legitimate) and `spam`

The dataset is downloaded for use in the notebook and is not included in this repository.

## Technologies

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Google Colab / Jupyter Notebook

## Model and Evaluation

The dataset was divided into training and testing sets using an 80/20 split with `random_state=42`. The model was trained using `TfidfVectorizer` and `MultinomialNB`.

### Test Results

| Metric                                          |   Result |
| ----------------------------------------------- | -------: |
| Test accuracy                                   | 96.6816% |
| Total test messages                             |    1,115 |
| Correctly classified legitimate messages        |      966 |
| Legitimate messages incorrectly flagged as spam |        0 |
| Correctly detected spam messages                |      112 |
| Spam messages missed                            |       37 |

The model achieved approximately 96.68% accuracy. However, it missed 37 spam messages, showing that high accuracy does not guarantee that every spam message will be detected.

## Custom Adversarial Tests

I created five messages to test the classifier's ability to handle unusual spelling, negation, misleading keywords, and businesslike language.

|   # | Test message                                                   | Model prediction | Expected label | Result        |
| --: | -------------------------------------------------------------- | ---------------- | -------------- | ------------- |
|   1 | Cl@im your fr33 g1ft card now                                  | ham              | spam           | Misclassified |
|   2 | Not free, just confirming lunch at 1pm                         | ham              | ham            | Correct       |
|   3 | Congratulations! You have won a free prize. Claim now!         | spam             | spam           | Correct       |
|   4 | Your account review is complete. Please verify your details.   | ham              | spam           | Misclassified |
|   5 | Hey, I am not selling anything. Are we still meeting tomorrow? | ham              | ham            | Correct       |

### Why Did the Model Make Mistakes?

**Test 1 — Character substitutions:** The message uses `@` instead of `a` and `33` instead of `ee`. These substitutions change the words the model sees, making familiar spam terms harder to recognize.

**Test 4 — Businesslike language:** The message sounds like an account notification and asks the recipient to verify details. It may resemble a phishing message, but the model classified it as legitimate.

These results demonstrate two limitations: TF-IDF does not automatically understand disguised words, and a basic Naive Bayes classifier does not truly understand the meaning or intent of a message.

## Techniques Tested

1. **Character substitutions:** Replaced letters with symbols and numbers, such as `claim` → `Cl@im` and `free` → `fr33`.
2. **Negation:** Used phrases such as "not free" and "not selling anything" to test the influence of potentially misleading keywords.
3. **Businesslike language:** Tested an account-verification message that resembles a legitimate notification.
4. **Misleading keywords:** Compared ordinary conversation containing words like "free" with a message promoting a prize.

## What I Learned

I learned that a model can achieve high test accuracy while still missing carefully written spam messages. I also learned that spelling substitutions, context, and the meaning of words can expose the limitations of a basic TF-IDF and Naive Bayes classifier.

## Project Files

- `spam_filter.ipynb` — Dataset preparation, model training, evaluation, and custom message tests.
- `README.md` — Project description, evaluation results, and lessons learned.
- `requirements.txt` — Required Python packages.

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Open `spam_filter.ipynb` in Google Colab or Jupyter Notebook and run the cells in order. The notebook downloads the dataset and trains the model.

## Conclusion

The experiment demonstrated that a simple spam classifier can perform well on a test dataset but still make mistakes on specially designed messages. More advanced text preprocessing and models that better understand context could help address these weaknesses.
