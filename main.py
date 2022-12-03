import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import inquirer

# ---------------- DEFINING COLORS ---------------------------------------
pkmn_type_colors_typ1 = [
                    '#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
]
pkmn_type_colors_typ2 = [
                    '#A040A0',  # Poison
                    '#6bb5ff',  # Flying
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#78C850',  # Grass
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#84888c',  # Steel
                    '#98D8D8',  # Ice
                    '#B8A038',  # Rock
                    '#6890F0',  # Water
]
sns.set_style("whitegrid")
#--------------------------Working with CSV--------------------------------------------------
pokemon = pd.read_csv('./Pokemon.csv',index_col=0,encoding='latin')
poki_stat = pokemon.drop(['Total','Stage','Legendary'],axis=1)
poki_melted = pd.melt(poki_stat,id_vars=["Name","Type 1","Type 2"],var_name="Stat")

#--------------------------Functions---------------------------------------------------------
def adScatter():
    plt.figure(figsize=(12,8))
    sns.scatterplot(x='Attack',y='Defense',data=pokemon,hue='Type 1',legend='brief',style='Stage')
    plt.ylim(0,200)
    plt.xlim(0,160)
    plt.legend(bbox_to_anchor=(1,1),loc=2)
    plt.show()

def adDensity():
    plt.figure(figsize=(12,8))
    sns.kdeplot(x='Attack',y='Defense',data=pokemon,hue='Stage',fill=True,common_norm=False,palette="crest",alpha=.5,linewidth=0)
    plt.show()

def adCombined():
    plt.figure(figsize=(12,8))
    sns.scatterplot(x='Attack',y='Defense',data=pokemon,hue='Type 1',legend='full',style='Stage',palette=pkmn_type_colors_typ1)
    sns.kdeplot(x='Attack',y='Defense',data=pokemon,hue='Stage',palette="crest",alpha=.5,linewidth=.5)
    plt.legend(bbox_to_anchor=(1,1),loc=2)
    plt.show()

def attackDefense():
    questions = [
        inquirer.List("selected",
                      message="Which type of graph you want?",
                      choices=[("Scatter Plot","1"),("Density Plot","2"),("Both Combined (^-^)","3"),("Back to Main Menu","4"),("Exit","5")],
                      carousel=True,
                      ),
    ]
    ans=inquirer.prompt(questions)
    opt=int(ans['selected'])
    if(opt == 1):
        adScatter()
        attackDefense()
    elif(opt == 2):
        adDensity()
        attackDefense()
    elif(opt == 3):
        adCombined()
        attackDefense()
    elif(opt == 4):
        mainMenu()
    elif(opt == 5):
        exit()
#-----------------------------------Attack Done--------------------------------------
def heviol():
    plt.figure(figsize=(12,8))
    sns.violinplot(x='Type 1',y='HP',data=pokemon,palette=pkmn_type_colors_typ1)
    sns.despine(offset=5,trim=True)
    plt.show()

def heSwarm():
    plt.figure(figsize=(12,8))
    sns.swarmplot(x='Type 1',y='HP',data=pokemon,palette=pkmn_type_colors_typ1)
    plt.show()

def heComb():
    plt.figure(figsize=(12,8))
    sns.violinplot(x='Type 1',y='HP',inner=None,data=pokemon,palette=pkmn_type_colors_typ1)
    sns.swarmplot(x='Type 1',y='HP',data=pokemon,color='k',alpha=0.6)
    plt.show()

def healthlData():
    questions = [
        inquirer.List("selected",
                      message="Which type of graph you want?",
                      choices=[("Violin Plot","1"),("Swarm Plot","2"),("Both Combined (^-^)","3"),("Back to Main Menu","4"),("Exit","5")],
                      carousel=True,
                      ),
    ]
    ans=inquirer.prompt(questions)
    opt=int(ans['selected'])
    if(opt == 1):
        heviol()
        healthlData()
    elif(opt == 2):
        heSwarm()
        healthlData()
    elif(opt == 3):
        heComb()
        healthlData()
    elif(opt == 4):
        mainMenu()
    elif(opt == 5):
        exit()
#-------------------------------Health Done--------------------------------------

def statWise():
    plt.figure(figsize=(15,8))
    sns.swarmplot(x='Stat',y='value',data=poki_melted,hue='Type 1',dodge=True,palette=pkmn_type_colors_typ1)
    plt.ylim(0,260)
    plt.legend(bbox_to_anchor=(1,1),loc=2)
    plt.show()

#------------------------------Stat Wise-----------------------------------------------

def heatMap():
    corrl = poki_stat.corr()
    plt.figure(figsize=(9,8))
    sns.heatmap(corrl,annot=True)
    plt.show()
#------------------------------Histogram-----------------------------------------------

def speedHist():
    plt.figure(figsize=(15,8))
    plt.legend(bbox_to_anchor=(1,1),loc=2)
    sns.histplot(pokemon,x='Speed',kde=True,hue='Stage',element='poly',multiple='dodge')
    plt.show()

#------------------------------Bar Graph Types-----------------------------------------------
def oneBar():
    plt.figure(figsize=(15,8))
    sns.countplot(x='Type 1',data=pokemon,palette=pkmn_type_colors_typ1)
    plt.xticks(rotation=-60)
    plt.show()

def twoBar():
    plt.figure(figsize=(15,8))
    sns.countplot(x='Type 2',data=pokemon,palette=pkmn_type_colors_typ2)
    plt.xticks(rotation=-60)
    plt.show()

def typeNum():
    questions = [
        inquirer.List("selected",
                      message="Which type of graph you want?",
                      choices=[("See for Type 1","1"),("See for Type 2","2"),("Back to Main Menu","3"),("Exit","4")],
                      carousel=True,
                      ),
    ]
    ans=inquirer.prompt(questions)
    opt=int(ans['selected'])
    if(opt == 1):
        oneBar()
        typeNum()
    elif(opt == 2):
        twoBar()
        typeNum()
    elif(opt ==3):
        mainMenu()
    elif(opt == 4):
        exit()

#------------------------------MAINMENU-----------------------------------------------
def mainMenu():
    questions = [
        inquirer.List("selected",
                      message="Choose",
                      choices=[("Attack VS Defense Data","1"),
                               ("Health Data","2"),
                               ("Different Stats Wise Graph","3"),
                               ("Heat Map","4"),
                               ("Histogram on basis of Speed","5"),
                               ("Number of Pokemon in each Types","6"),
                               ("Exit the Program","7")
                               ],
                      carousel=True,
                      ),
    ]
    ans=inquirer.prompt(questions)
    opt=int(ans['selected'])
    if(opt == 1):
        attackDefense()
    elif(opt == 2):
        healthlData()
    elif(opt == 3):
        statWise()
        mainMenu()
    elif(opt == 4):
        heatMap()
        mainMenu()
    elif(opt == 5):
        speedHist()
        mainMenu()
    elif(opt == 6):
        typeNum()
        mainMenu()
    elif(opt == 7):
        exit()
#----------------------------------------MAIN PROGRAM------------------------------------------------------
mainMenu()
