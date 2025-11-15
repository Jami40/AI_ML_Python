# Module 16 — Seaborn & Plotly: Advanced Visualization (Final Module)

[![Seaborn](https://img.shields.io/badge/Seaborn-1f77b4?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3f4f7f?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)

This folder contains the final module of the "Python for AI/ML" learning path. Module 16 focuses on producing high-quality static and interactive visualizations using Seaborn and Plotly Express. This completes the course: "End of Python for AI/ML" — congratulations on reaching the finish line!

---

## What you'll find here

- `Module_16.ipynb` — Jupyter notebook with extensive Seaborn and Plotly examples
- `enrollment_data.csv` — CSV used for line chart examples (course enrollment over years)
- `student_completed_data.csv` — dataset used for datetime, groupby and visualization examples

> Note: the notebook may also reference additional datasets (for example `sns_data (1).csv` or `student_dataset_complete.csv`) — ensure those files are present in the same folder if you run the notebook end-to-end.

---

## Topics covered

Seaborn (statistical plotting and high-level interface):
- Line plots: `sns.lineplot`, `sns.relplot(kind='line')`
- Scatter plots: `sns.scatterplot`, `sns.relplot(kind='scatter')` with `hue`, `style`, `size`
- Histograms & distribution plots: `sns.histplot`, `sns.displot`
- KDE plots: `sns.kdeplot`
- Countplots: `sns.countplot`
- Bar plots: `sns.barplot` (with different estimators)
- Regression plots: `sns.regplot`, `sns.lmplot`
- Pairplot & Jointplot: `sns.pairplot`, `sns.jointplot`
- Small-multiples using `col`, `row`, and `col_wrap`

Plotly Express (interactive plotting):
- Interactive scatter plots: `px.scatter` with `hover_data` and `size`
- Line charts: `px.line` with `markers=True`
- Histograms: `px.histogram`
- Exporting interactive HTML: `fig.write_html('file.html')`

Integration tips:
- Seaborn works best for quick statistical visualizations built on top of Matplotlib.
- Plotly Express produces interactive web-ready charts; use `fig.show()` in notebooks and `fig.write_html()` to save.
- Use Pandas DataFrames directly as input to both Seaborn and Plotly.

---

## Requirements

Install the recommended Python packages (if not already installed):

```bash
pip install numpy pandas matplotlib seaborn plotly jupyter
```

---

## How to run

1. Open a terminal in this folder or launch a Jupyter server from the repository root:

```bash
jupyter notebook
```

2. Open `Module_16.ipynb`.
3. Run the cells in order. If a dataset is missing, place the CSV in this folder or update the path in the notebook.
4. For interactive Plotly charts you can export them as HTML with `fig.write_html('chart.html')` and open in a browser.

---

## Final notes — End of Python for AI/ML

This notebook marks the final module of the "Python for AI/ML" curriculum in this repository. After finishing these lessons you should be comfortable with:
- Producing expressive static and interactive visualizations
- Using visualizations for exploratory data analysis and communicating results
- Combining Pandas, Seaborn, Matplotlib and Plotly in real workflows

If you'd like, next steps include:
- Learning interactive dashboards (Dash, Streamlit)
- Moving from visualization to model-building (scikit-learn, TensorFlow, PyTorch)
- Publishing visuals and interactive reports

Congratulations — you've completed "Python for AI/ML"! 🎓

---

If you want me to also add a short example notebook that reproduces the main visualizations as PNG exports (or create a demo script), tell me and I will add it.
