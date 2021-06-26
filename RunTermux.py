import subprocess
import priconne
from flask import Flask,request, render_template

app = Flask('priconne')

@app.route('/',methods=["GET","POST"])
@app.route('/boss-early-ub',methods=["GET","POST"])
@app.route('/index.html',methods=["GET","POST"])
def query():
  if request.method == 'GET':
    return render_template('boss-early-ub.html')
  if request.method == 'POST':
    tpBoost = int(request.form['tp_boost'])
    hpMax = int(request.form['hp_max'])
    data = priconne.boss_early_ub(tpBoost, hpMax)
    return render_template('boss-early-ub.html', data=repr(data))

@app.route('/clan-battle-progress',methods=["GET","POST"])
def query_clan_battle():
  if request.method == 'GET':
    return render_template('clan-battle-progress.html')
  if request.method == 'POST':
    score = int(request.form['clan_score'] )
    data = priconne.clan_battle_progress(score)
    return render_template('clan-battle-progress.html', data=repr(data))


if __name__ =='__main__':
  app.run(debug=True)