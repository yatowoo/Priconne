# Python package - Utilities for Priconne 

from math import *
from random import uniform as rng
from copy import deepcopy as cp_dict

LV_MAX = 202
HIT_DAMAGE_LIMIT = 999999

# Clan Battle stage
CLAN_BATTLE_STAGE = {
  'start_cycle' : [1, 4, 11, 31, 41],
  'hp_score':[
    [(6000000, 1.2), (8000000, 1.2), (10000000, 1.3), (12000000, 1.4), (15000000, 1.5)],
    [(6000000, 1.6), (8000000, 1.6), (10000000, 1.8), (12000000, 1.9), (15000000, 2.0)],
    [(12000000, 2.0), (14000000, 2.0), (17000000, 2.4), (19000000, 2.4), (22000000, 2.6)],
    [(19000000, 3.5), (20000000, 3.5), (23000000, 3.7), (25000000, 3.8), (27000000, 4.0)],
    [(85000000, 3.5), (90000000, 3.5), (95000000, 3.7), (100000000, 3.8), (110000000, 4.0)]
  ]
}
CLAN_BATTLE_STAGE_DATA = {}
def clan_battle_stage():
  total_score = 0
  # Generate stage score data -> To be STATIC?
  for stage in range(0,len(CLAN_BATTLE_STAGE['start_cycle'])):
    stage_name = chr(ord('A')+stage)
    CLAN_BATTLE_STAGE_DATA[stage_name] = {}
    stageNow = CLAN_BATTLE_STAGE_DATA[stage_name]
    stageNow['start_cycle'] = CLAN_BATTLE_STAGE['start_cycle'][stage]
    stageNow['hp_score'] = CLAN_BATTLE_STAGE['hp_score'][stage]
    stageNow['start_score'] = total_score
    score_cycle = 0
    for hp, score_coeff in CLAN_BATTLE_STAGE['hp_score'][stage]:
      score_cycle += hp * score_coeff
    stageNow['score_cycle'] = score_cycle
    # NOT last stage
    if stage < len(CLAN_BATTLE_STAGE['start_cycle']) - 1:
      stageNow['n_cycle'] = CLAN_BATTLE_STAGE['start_cycle'][stage+1] - CLAN_BATTLE_STAGE['start_cycle'][stage]
      stageNow['score_stage'] = stageNow['n_cycle'] * score_cycle
      total_score += stageNow['score_stage']
    else:
      stageNow['n_cycle'] = 0
      stageNow['score_stage'] = 1000 * stageNow['score_cycle']
  return CLAN_BATTLE_STAGE_DATA
def clan_battle_progress(score):
  progress = {'stage':'A', 'cycle':1, 'boss':1, 'hp_current': 6000000}
  if(not CLAN_BATTLE_STAGE_DATA):
    clan_battle_stage()
  # Loop by ABCDE
  for stage in sorted(CLAN_BATTLE_STAGE_DATA.keys()):
    data = CLAN_BATTLE_STAGE_DATA[stage]
    if(score >= data['start_score'] + data['score_stage']):
      continue
    progress['stage'] = stage
    delta_score = score - data['start_score']
    delta_cycle = int(delta_score / data['score_cycle'])
    progress['cycle'] = data['start_cycle'] + delta_cycle
    delta_score -= delta_cycle * data['score_cycle']
    scoreCylcleTmp = 0
    for i in range(0, len(data['hp_score'])):
      hp, score_coeff = data['hp_score'][i]
      if delta_score > scoreCylcleTmp + hp * score_coeff:
        scoreCylcleTmp += hp * score_coeff
        continue
      else:
        delta_score -= scoreCylcleTmp
        progress['boss'] = i+1
        progress['hp_current'] = int(hp -  delta_score / score_coeff)
        return progress
  return progress

##
# Properties
##
# Properties of Luna
LUNA = {
    'attack': 16138 + (240 + 15 * LV_MAX),
    'critical': 1392,
    'defence_phys': 225,
    'defence_magic': 329,
    'hp': 24376,
    'tp_boost': 13,
    'tp_retain': 29
}
 
LUNA_4 = {
    'attack': 15559 + (15 + 15 * LV_MAX),
    'critical': 1392,
    'defence_phys': 200,
    'defence_magic': 304,
    'hp': 20773,
    'tp_boost': 13,
    'tp_retain': 29
}
 
LUNA_3 = {
    'attack': 14977 + (15 + 15 * LV_MAX),
    'critical': 1392,
    'defence_phys': 172,
    'defence_magic': 276,
    'hp': 17168,
    'tp_boost': 13,
    'tp_retain': 29
}
 
 
# Properties of Nyaru
NYARU = {
    'attack': 16709 + (240 + 15 * LV_MAX),
    'critical': 1602,
    'defence_phys': 238,
    'defence_magic': 300,
    'hp': 24137,
    'tp_boost': 13,
    'tp_retain': 17
}
NYARU_4 = {
    'attack': 16116 + (15 + 15 * LV_MAX),
    'critical': 1602,
    'defence_phys': 211,
    'defence_magic': 280,
    'hp': 20589,
    'tp_boost': 13,
    'tp_retain': 17
}
NYARU_3 = {
    'attack': 15522 + (15 + 15 * LV_MAX),
    'critical': 1602,
    'defence_phys': 182,
    'defence_magic': 257,
    'hp': 17038,
    'tp_boost': 13,
    'tp_retain': 17
}
# Nuneka
# Rank 12, TP equip ONLY, 12-1/3 + 12-3/5
# Rank 12, FULL
NUNEKA_512 = {
    'attack': 7950 + (240 + 15 * LV_MAX),
    'critical': 128,
    'defence_phys': 217,
    'defence_magic': 365,
    'hp': 26940,
    'tp_boost': 5,
    'tp_retain': 32
}
NUNEKA_412= {
    'attack': 7336 + (15 + 15 * LV_MAX),
    'critical': 128,
    'defence_phys': 187,
    'defence_magic': 336,
    'hp': 22834,
    'tp_boost': 5,
    'tp_retain': 32
}
NUNEKA_312 = {
    'attack': 6720 + (15 + 15 * LV_MAX),
    'critical': 128,
    'defence_phys': 156,
    'defence_magic': 306,
    'hp': 18741,
    'tp_boost': 5,
    'tp_retain': 32
}
# Neneka
# Rank 21-4 FULL
NENEKA = {
    'attack': 15934 + (240 + 15 * LV_MAX),
    'critical': 1382,
    'defence_phys': 238,
    'defence_magic': 338,
    'hp': 27337,
    'tp_boost': 13,
    'tp_retain': 17
}
NENEKA_4 = {
    'attack': 15254 + (15 + 15 * LV_MAX),
    'critical': 1382,
    'defence_phys': 211,
    'defence_magic': 311,
    'hp': 23242,
    'tp_boost': 13,
    'tp_retain': 17
}
NENEKA_3 = {
    'attack': 14572 + (15 + 15 * LV_MAX),
    'critical': 1382,
    'defence_phys': 182,
    'defence_magic': 284,
    'hp': 19166,
    'tp_boost': 13,
    'tp_retain': 17
}

# Skill & Battle formula
def buff(buffCoef, lv = LV_MAX):
  return buffCoef * (lv + 1)
 
def tp_integer(tp_orignal, tp_boost):
  return round(tp_orignal * (1 + tp_boost/100.))
 
def yukari_tp(tp_boost, lv = LV_MAX):
  return tp_integer(75 + 2.5 *lv, tp_boost)
 
def miren_tp(tp_boost, lv = LV_MAX):
  return tp_integer(200 + 1.35 * lv, tp_boost)
 
def uzuki_tp(tp_boost, lv = LV_MAX):
  return tp_integer(50 + 0.3 * lv, tp_boost)
 
def nuneka_tp(tp_boost, lv = LV_MAX):
  return tp_integer(18 + 0.6 * lv, tp_boost)
 
def action_tp(tp_boost):
  return tp_integer(90, tp_boost)
 
def kill_tp(tp_boost):
  return tp_integer(200, tp_boost)
 
def hurt_tp_magic(damage, role):
  return hurt_tp(damage, role['hp'], role['defence_magic'],role['tp_boost'])
 
def hurt_tp(damage, hp, defence, tp_boost):
  return tp_integer(damage/(1+defence/100.) / hp * 500, tp_boost)
 
def hurt_for_UB(nActions, tpBoost, tpRetain, hpMAX, defence, otherTP = 0):
  tpAction = nActions * action_tp(tpBoost)
  dTP = 1000 - 1000 * tpRetain / 100 - tpAction - otherTP
  return dTP / 500 * hpMAX / (1+tpBoost/100.) * (1+ defence/100.)
 
# Damage for UB shifts
def boss_early_ub(tpBoost, bossHP, nMaxBefore = 5):
  N_MAX = floor(1000 / action_tp(tpBoost)) + 1
  result = {'n_action':N_MAX}
  print(N_MAX, ' actions for UB without damage')
  for nAction in range(N_MAX-nMaxBefore, N_MAX):
    damage = round(hurt_for_UB(nAction, tpBoost, 0, bossHP, 0, 0))
    result[N_MAX - nAction] = damage
    print('Early UB from %d actions, if damage more than : %d' % (N_MAX - nAction, damage))
  return result
 
def LogBarrier(damage, threshold=850000, factor=100000):
    if(damage < threshold):
        return damage
    else:
        return (factor * log((damage-threshold)/factor + 1) + threshold)
  
def critical_rate(criVal, enemyLv, lv = LV_MAX):
    return (0.05 * criVal / 100 * lv / enemyLv)
 
def critical_damage(orignalDamage, rate, criticalDamageBuff = 0., criticalCoeff = 2.0, defense = 0, logBarrier=False):
    hit = 0
    if(rng(0,1) < rate ):
        hit = round(orignalDamage * criticalCoeff * (1 + criticalDamageBuff))
    else:
        hit = round(orignalDamage)
    if(logBarrier):
      hit = LogBarrier(hit)
    return min(HIT_DAMAGE_LIMIT, round(hit / (1+defense/100.)))
 
NYARU_UB_BUFF_COEFF = 0.1125
def nyaruUB(attackWithBuff, criticalWithBuff, criticalDamageBuff = 0.,
            enemyLv = LV_MAX, lv = LV_MAX,
            detail=False, magic_defense = 0, logBarrier=False):
    # split in 10 parts = 1/13 * 9 + 4/13
    orignalDamage = 60 * (LV_MAX + 1 ) + 4.8 * attackWithBuff
    hits = []
    for i in ([1] * 9 + [4]):
      hit = critical_damage(orignalDamage*i/13, critical_rate(criticalWithBuff, enemyLv, lv), criticalDamageBuff, defense=magic_defense)
      hits.append(hit)
    totalDamage = sum(hits)
    if(logBarrier):
      effectDamage = LogBarrier(totalDamage)
      ratio = effectDamage / totalDamage
      effectDamage = sum([round(hit * ratio) for hit in hits])
    else:
      effectDamage = round(totalDamage)
    if detail:
        return [round(orignalDamage * 1/13), round(orignalDamage * 4/13), effectDamage]
    else:
        return effectDamage
 
def NyaruS1(attackWithBuff, enemyDefense, criticalWithBuff, criticalDamageBuff =0., enemyLv = LV_MAX, lv = LV_MAX, logBarrier=False):
   original = 27 * (LV_MAX + 1) + 2.1 * attackWithBuff
   damage = critical_damage(original, critical_rate(criticalWithBuff, enemyLv, lv), criticalDamageBuff, defense = enemyDefense, logBarrier=logBarrier)
   return damage
 
def NyaruS2_Shield(attackWithBuff):
  return round(buff(3) + 0.08 * attackWithBuff)
 
def LunaS1(attackWithBuff, enemyDefense, criticalWithBuff, criticalDamageBuff = 0., enemyLv = LV_MAX, lv = LV_MAX):
    return round(critical_damage(attackWithBuff, critical_rate(criticalWithBuff, enemyLv, lv), criticalDamageBuff, defense=enemyDefense))
 
def LunaS2(attackWithBuff, enemyDefense, criticalWithBuff, friendFlag=0, criticalDamageBuff =0., enemyLv = LV_MAX, lv = LV_MAX, logBarrier=False):
  if(friendFlag <2):
    original = 20 * (LV_MAX + 1) + 1.6 * attackWithBuff
  else:
    original = 40 * (LV_MAX + 1) + 3.2 * attackWithBuff
  damage = critical_damage(original, critical_rate(criticalWithBuff, enemyLv, lv), criticalDamageBuff, defense = enemyDefense, logBarrier=logBarrier)
  return damage
 
def LunaUB(attackWithBuff, enemyDefense, criticalWithBuff, friendFlag=5, criticalDamageBuff =0., enemyLv = LV_MAX, lv = LV_MAX):
  original = 12.5 * (LV_MAX +1) + (1.0 + min(5, friendFlag) * 1.2) * attackWithBuff
  # divide into 5 hits, each took 1/5 damage
  hits = []
  for i in ([1] * 5):
    hit = critical_damage(original*i/5, critical_rate(criticalWithBuff, enemyLv, lv), criticalDamageBuff, defense=enemyDefense)
    hits.append(round(hit))
  return sum(hits)

##
# QuickSort
##
# For skills to decide target with max/min stats.
MAX_LOOP_TRY = 100000
def swap(arr, left, right):
  tmp = arr[left]
  arr[left] = arr[right]
  arr[right] = tmp
def qsort(vals, left, right, pos):
  if(left >= right):
    return
  pivotL = left
  pivotR = right
  pivotVal = vals[int((pivotL + pivotR) / 2)]
  for i in range(MAX_LOOP_TRY):
    while(pivotL < right and vals[pivotL] < pivotVal):
      pivotL += 1
    while(pivotR > left and vals[pivotR] > pivotVal):
      pivotR -= 1
    if(pivotL > pivotR):
      break
    # swap value
    vals[pivotL], vals[pivotR] = vals[pivotR], vals[pivotL]
    pos[pivotL], pos[pivotR] = pos[pivotR], pos[pivotL]
    pivotL +=1
    pivotR -=1
  if(left < pivotR):
    qsort(vals, left, pivotR, pos)
  if(pivotL < right):
    qsort(vals, pivotL, right, pos)
  return
def qsort_selection(vals, maxFlag = True, reverseFlag=True):
  pos = list(range(1, len(vals)+1))
  if(reverseFlag):
    pos.reverse()
  qsort(vals, 0, len(vals)-1, pos)
  if(maxFlag):
    return pos[-1]
  else:
    return pos[0]

##
# Timeline Simulation
##

# Class: Status recorder
# Data: LIST for delta information (DICT)
# Methods: input object, TIMESTAMP and properties, return accumulated buff/debuff and current status
# Status change (buff/debuff): 
#   physic_attack, magic_attack
#   physic_defence, magic_defence
#   physic_critical, magic_critical, physical_critical_damage, magic_critical_damage
#   TP boost
#   speed (final value, not delta)
#   field (overlap?)
#   Other: HP drain rate, HOT/DOT
#   Info: caster, target (name/ID), timestamp (start/end) [seconds or frame?]
class StatusRecorder:
  STATS_NAME = ['atk_phy', 'atk_mag', 'def_phy', 'def_mag', 'crit_phy', 'crit_mag', 'crit_damage_phy', 'crit_damage_mag','tp_boost','speed']
  INFO_NAME = ['caster', 'target', 'start', 'stop', 'duration']
  party = []
  objects = []
  status_delta = []
  status_delta_backup = [] 
  def __init__(self, party):
    self.status_delta = []
    self.party = party
    self.objects = party + ['boss']
  # Input check and change function object abbr to list
  def append(self, newStatusChange):
    # Argument type check
    if(type(newStatusChange) is not dict or not bool(newStatusChange)):
      print('[X] Argument error - require dict with stats name and value - from StatusRecorder.append')
      return False
    delta =cp_dict(newStatusChange)
    # Name check
    for k in delta.keys():
      if(k not in self.STATS_NAME + self.INFO_NAME):
        print('[X] Argument error - can not find key ' + repr(k) + ' - from StatusRecorder.append')
        return False
    # Target check
    tgt = delta['target']
    if(type(tgt) is not list):
      if(tgt == 'all'):
        delta['target'] = self.party
      elif(tgt in self.objects):
          delta['target'] = [tgt]
      else:
        print('[X] Argument error - can not find target ' +repr(tgt) + ' in current party ' + repr(self.party) + '- from StatusRecorder.append')
    else:
      for name in tgt:
        if(name not in self.objects):
          print('[X] Argument error - can not find target ' +repr(name) + ' in current battle ' + repr(self.objects) + '- from StatusRecorder.append')
    # End time
    delta['stop'] = delta['start'] - delta['duration']
    self.status_delta.append(delta)
    return True
  def addAtkBuff(self, buffValue, timestamp, duration=12, buffCritical = 0, buffCritDamage=0, buffType='phy', target='all', caster=None):
    delta = {'start': timestamp, 'stop': timestamp - duration, 'duration': duration, 'target': target, 'caster': caster}
    if(buffType == 'phy'):
      delta['atk_phy'] = buffValue
      delta['crit_phy'] = buffCritical
      delta['crit_damage_phy'] = buffCritDamage
    elif(buffType == 'mag'):
      delta['atk_mag'] = buffValue
      delta['crit_mag'] = buffCritical
      delta['crit_damage_mag'] = buffCritDamage
    else:
      print('[X] Input buff type error - ', buffType, ' not defined - from StatusRecorder.addAtkBuff')
      return
    return self.append(delta)
  def update(self, deltaVal, timestamp, duration = 12, statsType='atk_phy', target='all', caster=None):
    delta = {'start': timestamp, 'stop': timestamp - duration, 'duration': duration, 'target': target, 'caster': caster}
    delta[statsType] = deltaVal
    return self.append(delta)
  def getStatus(self, initStats, target, timestamp=90, statsKey='all'):
    nowStats = cp_dict(initStats)
    for delta in self.status_delta:
      if(delta['stop'] > timestamp or  delta['start'] < timestamp or target not in delta['target']):
        continue
      for k in [name for name in delta.keys() if name not in self.INFO_NAME]:
        nowStats[k] += delta[k]
    # Value check - non-zero stats
    for k in [name for name in nowStats.keys() if name in self.STATS_NAME and name not in self.INFO_NAME]:
      nowStats[k] = max(0, nowStats[k])
    if(statsKey == 'all'):
      return nowStats
    else:
      return nowStats[statsKey]
# END - Class StatusRecorder

# Class: TLManager - Timeline Management 
class TLManager:
  statsRec = None # instance of StatusRecorder
  initStats = {}  # initial chara & boss status
  damageRec = {}  # TL simulation result - damage only
  FLAG_DEBUG = False
  FLAG_LOGBARRIER = True
  def __init__(self) -> None:
    statsRec = StatusRecorder(['yukari', 'anna', 'akari', 'nyaru', 'luna'])
    self.initStats['nyaru'] = {'atk_mag':NYARU['attack'], 'crit_mag':NYARU['critical']}
    self.initStats['boss'] = {'name': '2021/05 C4', 'lv': 115, 'HP': 18000000, 'def_phy': 300, 'def_mag': 290, 'tp_boost':40}
    for k in [x for x in self.statsRec.STATS_NAME if x not in self.initStats['nyaru'].keys()]:
      self.initStats['nyaru'][k] = 0.
    for name in statsRec.party:
      self.damageRec[name] = []
  # LIST of tuples with format (timestamp, action)
  # action is function or string to call
  def RunTimeline(timeline):
    # Run timeline
    for timestamp, action in timeline:
      # Run Action
      if(callable(action)):
        action(timestamp)
      else:
        name = action.split('_')[0]
        skill = action.split('_')[1]
        if(skill == 'a' or skill == 'attack'):
          globals()['action_attack'](timestamp, name)
        else:
          globals()['action_' + action](timestamp)
# END - Class TLManager