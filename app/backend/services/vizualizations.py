import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_sorted_dataframe(data, y_column, asc):
    df = pd.DataFrame(data)
    return df.sort_values(y_column, ascending=asc)[0:10]


def get_colors(df_sorted):
    return sns.color_palette("husl", n_colors=len(df_sorted))


def create_bar_plot(df_sorted, x_column, y_column, colors):
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_sorted[x_column], df_sorted[y_column], color=colors)
    return bars


def add_plot_labels(title, label_column):
    plt.title(title, fontweight='bold', fontsize=16)
    plt.xlabel('Company Name', fontweight='bold', fontsize=12)
    plt.ylabel(label_column, fontweight='bold', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontweight='bold')
    plt.yticks(fontweight='bold')


def add_bar_labels(bars, df_sorted, label_column):
    for bar, label in zip(bars, df_sorted[label_column]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 label, ha='center', va='bottom', fontweight='bold')


def remove_plot_borders():
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()


def save_plot(filename):
    file_path = os.path.join('app/backend/images/', filename)
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.clf()
    return filename


def create_plot(data, x_column, y_column, label_column, title, filename, asc):
    df_sorted = get_sorted_dataframe(data, y_column, asc)
    colors = get_colors(df_sorted)
    bars = create_bar_plot(df_sorted, x_column, y_column, colors)
    add_plot_labels(title, label_column)
    add_bar_labels(bars, df_sorted, label_column)
    remove_plot_borders()
    return save_plot(filename)
