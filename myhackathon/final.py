# importing Flask and other modules
from flask import Flask, request, render_template 
import sqlite3
import urllib.request
import re


conn = sqlite3.connect('workouts.db')
c = conn.cursor()
 
# Flask constructor
app = Flask(__name__, static_url_path='/static')   
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])

    
def gfg():
    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workouts")
    rows = c.fetchall()

    # Print the data
    if len(rows) > 0:
        for row in rows:
            print(row)
        
            
    else:
        print("No data found in the 'workouts' table.")
        return render_template("main.html", text=rows)
        
    

    
    
    
    if request.method == "POST":
        inp = request.form.get("exerciseinp")
        c.execute("SELECT id FROM workouts WHERE rowid = ?", (inp,))
        workout_id = c.fetchone()[0]

        c.execute("SELECT exercise_name FROM exercises WHERE workout_id = ?", (workout_id,))
        exercises = c.fetchall()
        links = []
        for i in range(len(exercises)):
            
            print(f"Exercise {i+1}: {exercises[i]}")
            v1 = str(exercises[i])
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + v1)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            link="https://www.youtube.com/embed/" + video_ids[0]
            
            print(link)
            
            links.append(link)
        return render_template("main.html", text2=links, text=rows)
            
        

       
    conn.close()
            
    return render_template("main.html", text=rows)
 
if __name__=='__main__':
   app.run()
   