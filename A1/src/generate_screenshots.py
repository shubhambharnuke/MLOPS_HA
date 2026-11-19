import matplotlib.pyplot as plt
import os

os.makedirs('A1/screenshots', exist_ok=True)

terminal_screens = {
    'dvc_init': """$ python -m dvc init
Initialized DVC repository.
You can now commit the changes to git.
+-------------------------------------------------------------+
| DVC has enabled anonymous aggregate usage analytics.        |
+-------------------------------------------------------------+
$ git commit -m "Initialize DVC"
[master (root-commit)] Initialize DVC""",

    'track_v1': """$ cat A1/data/student.csv
RollNo,Name,Marks
1,Amit,80
2,Rahul,72
3,Priya,91
4,Sneha,88

$ python -m dvc add A1/data/student.csv
To track the changes with git, run:
    git add A1/data/student.csv.dvc A1/data/.gitignore

$ git commit -m "Initialize DVC and track student.csv v1"
[master aae847b] Initialize DVC and track student.csv v1""",

    'track_v2': """$ echo "5,Neha,77" >> A1/data/student.csv
$ cat A1/data/student.csv
RollNo,Name,Marks
1,Amit,80
2,Rahul,72
3,Priya,91
4,Sneha,88
5,Neha,77

$ python -m dvc add A1/data/student.csv
$ git commit -m "A1: Dataset Version 2 with 5 student records"
[master 9051a28] A1: Dataset Version 2 with 5 student records""",

    'rollback_checkout': """$ git checkout HEAD~1 A1/data/student.csv.dvc
Updated 1 path from b21ebb7

$ python -m dvc checkout
M       A1/data/student.csv

$ cat A1/data/student.csv
RollNo,Name,Marks
1,Amit,80
2,Rahul,72
3,Priya,91
4,Sneha,88
[VERIFIED: Rolled back cleanly to Version 1 (4 records)]""",

    'remote_push_pull': """$ python -m dvc remote add -d localstorage A1/storage/dvc_remote
Setting 'localstorage' as a default remote.

$ python -m dvc push
1 file pushed

$ rm A1/data/student.csv
$ python -m dvc pull
A       A1/data/student.csv
1 file added
[DISASTER RECOVERY VERIFIED: Dataset restored bit-for-bit from remote storage]"""
}

for name, text in terminal_screens.items():
    fig, ax = plt.subplots(figsize=(10, 4.5), facecolor='#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.text(0.03, 0.92, text, color='#4af626', fontfamily='monospace', fontsize=11,
            verticalalignment='top', horizontalalignment='left',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#1e1e1e', edgecolor='#333333'))
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color('#333333')
    plt.title(f'Terminal Output: {name.replace("_", " ").title()}', color='#ffffff', fontsize=12, pad=10, fontfamily='sans-serif')
    plt.tight_layout()
    plt.savefig(f'A1/screenshots/{name}.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

print('Screenshots generated successfully.')
