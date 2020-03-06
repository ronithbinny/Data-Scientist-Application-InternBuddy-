import pandas as pd
import re

dataset = pd.read_csv("Book1.csv")

x = dataset.iloc[:,[2,3,4,5,7,9]].values
skill__col = []

for i in range(0,len(x)) :
    
    try :
        sp = x[i][3].split(",")
        count = 0
        
        for skill in sp :
            skill = skill.strip()

            if ((skill == "Machine Learning") or (skill == "Deep Learning") or (skill == "Natural Language Processing (NLP)") or 
            (skill == "Statistical Modeling") or (skill == "AWS") or (skill == "SQL") or 
            (skill == "NoSQL") or (skill == "Excel")) :
                count = count + 1
        
        skill__col.append(count)
        
    except :
        skill__col.append(0)
        
decision = []
degree = []

for i in range(0,len(x)) :
    
    student_score = 0
    
    if x[i][0] == 1 :
        student_score = student_score + 3
        
    elif x[i][0] == 2 :
        student_score = student_score + 7
    
    elif x[i][0] == 3 :
        student_score = student_score + 10
        
    
    if x[i][1] == 1 :
        student_score = student_score + 3
        
    elif x[i][1] == 2 :
        student_score = student_score + 7
    
    elif x[i][1] == 3 :
        student_score = student_score + 10
        
        
    if x[i][2] == 1 :
        student_score = student_score + 3
        
    elif x[i][2] == 2 :
        student_score = student_score + 7
    
    elif x[i][2] == 3 :
        student_score = student_score + 10
        
        
    student_score = student_score + (3 * skill__col[i])
    
    try : 
        if re.search("B.E",x[i][-2]) :
            deg = "B.E"
            degree.append("B.Tech")
        elif re.search("B.Tech",x[i][-2]) :
            deg = "B.E"
            degree.append("B.Tech")
        elif re.search("M.Tech",x[i][-2]) :
            deg = "M.Tech"
            degree.append("M.Tech")
        elif re.search("M.Sc",x[i][-2]) :
            deg = "M.Tech"
            degree.append("M.Tech")
        else :
            degree.append("-")
            
        if deg == "B.E" and x[i][-1] == 2020 :
            student_score = student_score + 10
        elif deg == "B.E" and x[i][-1] == 2019 :
            student_score = student_score + 8
        elif deg == "B.E" and x[i][-1] <= 2019 :
            student_score = student_score + 5
        elif deg == "M.Tech" and x[i][-1] == 2020 :
            student_score = student_score + 7
        elif deg == "M.Tech" and x[i][-1] <= 2019 :
            student_score = student_score + 3
    
    except :
        degree.append("-")
        
        
    if student_score >= 40 :
        decision.append(1)
    else :
        decision.append(0)
    
filename = "modified.csv"
sub = pd.DataFrame({"Python" : dataset['Python (out of 3)'], "R" : dataset["R Programming (out of 3)"], 
                                       "Data Science" : dataset["Data Science (out of 3)"], "Other skills" : skill__col,
                                       "Degree" : degree, "Year" : dataset["Current Year Of Graduation"],
                                       "Decision" : decision})
sub.to_csv(filename, index = False)