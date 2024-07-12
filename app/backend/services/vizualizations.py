import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_plot(data, x_column, y_column, label_column, title, filename, asc):
    df = pd.DataFrame(data)
    df_sorted = df.sort_values(y_column, ascending=asc)[0:10]
    colors = sns.color_palette("husl", n_colors=len(df_sorted))
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_sorted[x_column], df_sorted[y_column], color=colors)
    plt.title(title, fontweight='bold', fontsize=16)
    plt.xlabel('Company Name', fontweight='bold', fontsize=12)
    plt.ylabel(label_column, fontweight='bold', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontweight='bold')
    plt.yticks(fontweight='bold')

    for bar, label in zip(bars, df_sorted[label_column]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 label, ha='center', va='bottom', fontweight='bold')

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    file_path = os.path.join('app/backend/images/', filename)
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.clf()

    return filename
