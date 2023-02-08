#Laden benötiger Modulen/Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#Laden der Datei
df = pd.read_csv('standard.csv',encoding='iso-8859-1')

#Einrichtung: Größe des Plots
plt.figure(figsize=(12,10))

#Hinzufügung: Farbe jedes Vereins :)
color_dict = dict({'Augsburg':'#BA3733',
                  'Bayern Munich':'#DC052D',
                  'Bochum': '#005CA9',
                  'Dortmund': '#FDE100',
                  'Eint Frankfurt': '#E1000F',
                  'Freiburg':'#000000',
                  'Hertha BSC': '#004D9E',
                  'Hoffenheim': '#1961B5',
                  'Köln': '#ed1c24',
                  'Leverkusen':'#E32221',
                  "M'Gladbach":'#000000',
                  'Mainz 05':'#C3141E',
                  'RB Leipzig':'#DD013F',
                  'Schalke 04':'#004d9d',
                  'Stuttgart':'#E32219',
                  'Union Berlin':'#EB1923',
                  'Werder Bremen': '#1d9053',
                  'Wolfsburg':'#65B32E'})

sss = sns.scatterplot(x = 'PrgC',
                        y= 'PrgP',
                        hue= 'Squad',
                        size='npxG',
                        sizes=(100,200),
                        alpha=.8,
                        palette= color_dict,
                        data=df,
                        legend = False)

#Labels
plt.title('Vergleich der Progressivität\n zwischen Bundesligaklubs(angepasst für npxG)',size=15)
plt.xlabel('Erfolgreiche progressive Pässe')
plt.ylabel('Erfolgreiche progressive Tragen')

#customfunktion passt nicht so säuberlich
#for i in range(df.shape[0]):
 #   plt.annotate(df.Squad.tolist()[i], 
  #  (df['PrgC'].tolist()[i], df.PrgP.tolist()[i]))

#Einrichtung der Bregrenzung der Achsen
plt.xlim([100,500])
plt.ylim([450,1200])


#Referenzlinie f. beide Achsen
plt.axhline(y=np.nanmean(df.PrgP),color='grey')
plt.axvline(x=np.nanmean(df.PrgC),color='grey')


#Hinzufügung von Namen des Klubs zum Plot
plt.annotate('Bayern München',
                xy=(400,1115),
                xytext=(400,1115))

plt.annotate('Borussia Dortmund',
            xy=(381,899),
            xytext=(381,899))

plt.annotate('RB Leipzig',
            xy=(318,769),
            xytext=(318,769))    

plt.annotate('Augsburg',
            xy=(135,498),
            xytext=(135,498))

plt.annotate('Union Berlin',
            xy=(158,540),
            xytext=(158,540))

plt.annotate('Schalke 04',
            xy=(218,515),
            xytext=(218,515))

plt.annotate('Bayer Leverkusen',
            xy=(369,685),
            xytext=(369,685))

plt.annotate('VfL Bochum',
            xy=(160,572),
            xytext=(160,572))

plt.annotate('TSG Hoffenheim',
            xy=(300,715),
            xytext=(300,715))


plt.annotate('VfL Wolfsburg',
            xy=(185,700),
            xytext=(185,700))

plt.show()            
