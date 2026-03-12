# week02_machine_learning: machine learning

## Concept
This week introduces the practical ML loop: load a dataset, split into train/test sets, train a model, and evaluate it with clear metrics. Focus on shipping a baseline before tuning.

## Key Ideas
- Separate training data from evaluation data.
- Start with a simple baseline model first.
- Use metrics that match the business goal (not accuracy only).
- Keep preprocessing and model steps inside one pipeline.

## Minimal Code Example
```python
"""Train and evaluate a small sklearn model.
Install: pip install scikit-learn
Run: python3 ml_baseline.py
"""

from __future__ import annotations

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.2,
        random_state=42,
        stratify=dataset.target,
    )

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=500)),
        ]
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions, target_names=dataset.target_names))


if __name__ == "__main__":
    main()
```

## Exercise
Swap `LogisticRegression` for another classifier (for example `RandomForestClassifier`) and compare metrics.

## Extra Challenge
Run 5-fold cross-validation and report mean + standard deviation of accuracy.
