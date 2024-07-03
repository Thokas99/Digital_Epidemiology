import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_infected_cases():
    """Plots the sum of infected cases over months for each year."""
    data = {
        'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December'],
        '2001': [414, 272, 137, 22, 17, 2, 0, 1, 17, 1, 9, 127],
        '2002': [454, 301, 160, 55, 25, 11, 7, 1, 17, 32, 86, 417],
        '2003': [382, 138, 120, 50, 2, 10, 4, 4, 31, 64, 284, 607],
        '2004': [348, 145, 129, 9, 6, 4, 0, 0, 15, 28, 88, 373]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sum infected cases for each year
    df_sum = df.groupby('Month').sum().T

    # Plot 1: Enhanced Line Plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_sum, markers=True, dashes=False)
    plt.title('Infected Cases Over Months for Each Year')
    plt.xlabel('Month')
    plt.ylabel('Sum of Infected Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot 2: Bar Plot for Each Year
    plt.figure(figsize=(12, 8))
    for year in df.columns[1:]:
        plt.bar(df['Month'], df[year], alpha=0.7, label=year)
    plt.title('Infected Cases by Month and Year')
    plt.xlabel('Month')
    plt.ylabel('Number of Infected Cases')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot 3: Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.set_index('Month').drop(columns='2001'), cmap='Reds', annot=True, fmt='d')
    plt.title('Infected Cases Heatmap (2002-2004)')
    plt.xlabel('Year')
    plt.ylabel('Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Calculate and plot correlation matrix
    corr_matrix = df.set_index('Month').T.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Infected Cases')
    plt.xlabel('Year')
    plt.ylabel('Year')
    plt.tight_layout()
    plt.show()

plot_infected_cases()
