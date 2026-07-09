# Missing Value Handling in Pandas

## 📌 Concepts Covered

* Loading the Titanic dataset using `seaborn`
* Viewing the first few rows with `head()`
* Detecting missing values using `isnull().sum()`
* Checking dataset shape with `shape`
* Removing missing values using `dropna()`
* Dropping rows vs. dropping columns (`axis=0` and `axis=1`)
* Mean Imputation for normally distributed numerical data
* Median Imputation for numerical data with outliers
* Mode Imputation for categorical features
* Visualizing data distribution using `sns.histplot()` with KDE

## 📚 Learning Outcomes

* Understand how to identify missing values in a dataset.
* Learn different techniques to handle missing data.
* Know when to use **Mean**, **Median**, and **Mode** imputation.
* Differentiate between dropping rows and dropping columns containing missing values.
* Visualize feature distribution before choosing an imputation method.
* Prepare datasets for data analysis and machine learning preprocessing.
# Handling Imbalanced Dataset - Upsampling & Downsampling

## 📌 Concepts Covered

* Creating an imbalanced dataset using **NumPy** and **Pandas**
* Generating data with `np.random.normal()`
* Setting a random seed using `np.random.seed()`
* Creating majority and minority classes
* Combining DataFrames using `pd.concat()`
* Separating classes based on the target variable
* Random **Upsampling** using `sklearn.utils.resample()`
* Random **Downsampling** using `sklearn.utils.resample()`
* Sampling with and without replacement (`replace=True` / `replace=False`)
* Shuffling the dataset using `sample()`
* Resetting index with `reset_index()`
* Checking class distribution using `value_counts()`
* Comparing Upsampling and Downsampling techniques

## 📚 Learning Outcomes

* Understand what an imbalanced dataset is and why it is a problem in machine learning.
* Learn how to create a synthetic imbalanced dataset for experimentation.
* Balance datasets using **Random Upsampling** by increasing minority class samples.
* Balance datasets using **Random Downsampling** by reducing majority class samples.
* Understand the purpose of `replace`, `n_samples`, and `random_state` in `resample()`.
* Learn when to use Upsampling and Downsampling based on dataset size and requirements.
* Compare the advantages, disadvantages, and use cases of both balancing techniques.
* Prepare datasets for building more reliable and unbiased machine learning models.

# SMOTE (Synthetic Minority Oversampling Technique)

## 📌 Concepts Covered

* Creating a synthetic classification dataset using `make_classification()`
* Understanding class imbalance with the `weights` parameter
* Creating feature and target DataFrames using Pandas
* Combining DataFrames using `pd.concat()`
* Visualizing imbalanced data using `matplotlib.pyplot.scatter()`
* Applying **SMOTE** using `imblearn.over_sampling.SMOTE`
* Generating synthetic minority class samples with `fit_resample()`
* Converting resampled data into a DataFrame
* Visualizing the balanced dataset after SMOTE
* Comparing class distribution before and after SMOTE

## 📚 Learning Outcomes

* Understand how to generate an imbalanced dataset for machine learning experiments.
* Learn the purpose and working of **SMOTE** for handling class imbalance.
* Balance minority and majority classes without simply duplicating samples.
* Visualize the effect of SMOTE on the dataset.
* Use `fit_resample()` to generate synthetic samples and create a balanced dataset.
* Prepare datasets for building more accurate and unbiased classification models.
* Gain practical experience with one of the most widely used imbalance handling techniques in machine learning.
