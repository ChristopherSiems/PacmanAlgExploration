import pandas
from matplotlib import pyplot

def remove_outliers(series):
  q1 = series.quantile(.25)
  q3 = series.quantile(.75)
  iqr = q3 - q1
  upper = q3 + 1.5 * iqr
  lower = q1 - 1.5 * iqr
  result = series.loc[(series >= lower) & (series <= upper)]
  return result

data = pandas.read_csv('data.csv')
groups = data.groupby(by = 'alg')
algs = ['Rand_Dir', 'Rand_Dir_Legal', 'Rand_Dir_Hold', 'Rand_Dir_Legal_Hold','Rand_Turn', 'Rand_Turn_Legal', 'Rand_Dir_Charge', 'BFS_Rand', 'BFS_Gum', 'BFS_Agress', 'BFS_Mod', 'A_Star_Rand', 'A_Star_Agress', 'Dijkstra_Rand']
dimension = (8, 4)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

pyplot.figure(figsize = dimension)
BFS_Gum_wins = groups.get_group('BFS_Gum')['win'].value_counts()
BFS_Mod_wins = groups.get_group('BFS_Mod')['win'].value_counts()
BFS_Gum_labels = ['win' if label else 'loss' for label in BFS_Gum_wins.index]
BFS_Mod_labels = ['win' if label else 'loss' for label in BFS_Mod_wins.index]
pyplot.subplot(1, 2, 1)
pyplot.pie(BFS_Gum_wins, labels = BFS_Gum_labels, autopct = '%1.1f%%')
pyplot.title('BFS Pacgum')
pyplot.subplot(1, 2, 2)
pyplot.pie(BFS_Mod_wins, labels = BFS_Mod_labels, autopct = '%1.1f%%')
pyplot.title('BFS Solver')
pyplot.tight_layout()
pyplot.savefig('graphs/wins.png')

pyplot.figure(figsize = dimension)
pyplot.boxplot([groups.get_group(alg)['pacgums'] for alg in algs], labels = letters)
pyplot.axhline(244, label = 'Total number of pacgums: 244', color = 'C2')
avg = int(data['pacgums'].mean())
pyplot.axhline(avg, label = f'Mean number of pacgums collected: {avg}', color = 'C3')
med = int(data['pacgums'].median())
pyplot.axhline(med, label = f'Median number of pacgums collected: {med}', color = 'C4')
pyplot.title('Pacgums collected by algorithm.')
pyplot.xlabel('Algorithms')
pyplot.ylabel('Pacgums collected.')
pyplot.legend(loc='upper left', bbox_to_anchor = (1, 1))
pyplot.tight_layout()
pyplot.savefig('graphs/gums.png')

pyplot.figure(figsize = dimension)
pyplot.boxplot([remove_outliers(groups.get_group(alg)['score']) for alg in algs], labels = letters)
avg = int(data['score'].mean())
pyplot.axhline(avg, label = f'Mean score: {avg}', color = 'C2')
med = int(data['score'].median())
pyplot.axhline(med, label = f'Median score: {med}', color = 'C3')
pyplot.title('Score by algorithm.')
best = data.sort_values(by = 'score', ascending = False).iloc[0]
print(f'Maximum Score: {best['alg']}, {best['score']}')
pyplot.xlabel('Algorithms')
pyplot.ylabel('Score')
pyplot.legend(loc='upper left', bbox_to_anchor = (1, 1))
pyplot.tight_layout()
pyplot.savefig('graphs/score.png')

pyplot.figure(figsize = dimension)
pyplot.boxplot([groups.get_group(alg)['time'] for alg in algs], labels = letters)
pyplot.title('Runtime by algorithm.')
pyplot.xlabel('Algorithms')
pyplot.ylabel('Time (sec.)')
pyplot.tight_layout()
pyplot.savefig('graphs/time.png')