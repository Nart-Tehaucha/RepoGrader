import pandas as pd
import math


def gradeRepo(additions, deletions, messageLen, method):
    mlog = 1

    if method == 1:
        return additions + deletions + messageLen
    else:
        if additions > 0 or deletions > 0:
            mlog = 2*additions + deletions
        return math.log(mlog) + messageLen


# Grade by Total lines of code changed + message length
def gradeFirstMethod():
    filename = 'FinalDataset.csv'
    df = pd.read_csv(filename)
    df['grade'] = df.apply(lambda row : gradeRepo(row['additions'], row['Deletions'], len(str(row['Messages'])), 1), axis = 1)

    df_normalized = df.copy()
    df_normalized['norm_grade'] = df_normalized.groupby('Repository')['grade'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

    #print(df_normalized)

    df_avg = df_normalized[['Repository', 'Forks', 'norm_grade']].groupby(['Repository', 'Forks'], sort=False)['norm_grade'].median().reset_index(name="avg_grade")

    print(df_avg)
    print('==============================================================')
    print('Correlation between forks and avg_grade')
    print(df_avg['Forks'].corr(df_avg['avg_grade']))

    df_avg['Correlation'] = df_avg['Forks'].corr(df_avg['avg_grade'])

    df_avg.to_csv('Normalized.csv', encoding='utf-8')



# Grade by message length only
def gradeSecondMethod():
    filename = 'FinalDataset.csv'
    df = pd.read_csv(filename)
    df['grade'] = df.apply(lambda row: len(str(row['Messages'])), axis=1)

    df_normalized = df.copy()
    df_normalized['norm_grade'] = df_normalized.groupby('Repository')['grade'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()))

    # print(df_normalized)

    df_avg = df_normalized[['Repository', 'Forks', 'norm_grade']].groupby(['Repository', 'Forks'], sort=False)[
        'norm_grade'].median().reset_index(name="avg_grade")

    print(df_avg)
    print('==============================================================')
    print('Correlation between forks and avg_grade')
    print(df_avg['Forks'].corr(df_avg['avg_grade']))

    df_avg['Correlation'] = df_avg['Forks'].corr(df_avg['avg_grade'])

    df_avg.to_csv('Normalized2.csv', encoding='utf-8')
    df_normalized.to_csv('Normalized2.csv', encoding='utf-8')



# Grade by Total lines of code changed only
def gradeThirdMethod():
    filename = 'FinalDataset.csv'
    df = pd.read_csv(filename)
    df['grade'] = df.apply(lambda row : row['Total'], axis=1)

    df_normalized = df.copy()
    df_normalized['norm_grade'] = df_normalized.groupby('Repository')['grade'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()))

    # print(df_normalized)

    df_avg = df_normalized[['Repository', 'Forks', 'norm_grade']].groupby(['Repository', 'Forks'], sort=False)[
        'norm_grade'].median().reset_index(name="avg_grade")

    print(df_avg)
    print('==============================================================')
    print('Correlation between forks and avg_grade')
    print(df_avg['Forks'].corr(df_avg['avg_grade']))

    df_avg['Correlation'] = df_avg['Forks'].corr(df_avg['avg_grade'])

    df_avg.to_csv('Normalized3.csv', encoding='utf-8')



# Grade by the log of lines of code added and deleted + message length. Add 2x weight to lines of code added.
def gradeFourthMethod():
    filename = 'FinalDataset.csv'
    df = pd.read_csv(filename)
    df['grade'] = df.apply(lambda row: gradeRepo(row['additions'], row['Deletions'], len(str(row['Messages'])), 2), axis=1)

    df_normalized = df.copy()
    df_normalized['norm_grade'] = df_normalized.groupby('Repository')['grade'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()))

    # print(df_normalized)

    df_avg = df_normalized[['Repository', 'Forks', 'norm_grade']].groupby(['Repository', 'Forks'], sort=False)[
        'norm_grade'].median().reset_index(name="avg_grade")

    print(df_avg)
    print('==============================================================')
    print('Correlation between forks and avg_grade')
    print(df_avg['Forks'].corr(df_avg['avg_grade']))
    df_avg['Correlation'] = df_avg['Forks'].corr(df_avg['avg_grade'])

    df_avg.to_csv('Normalized4.csv', encoding='utf-8')


gradeFirstMethod()
gradeSecondMethod()
gradeThirdMethod()
gradeFourthMethod()




