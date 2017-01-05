import ply.lex as lex
from .definitions import getEventTypeId, getActionTypeId, getTargetTypeId, getEventFlagId, getCastFlagId
from .expressions import Number, EventFlag, CastFlag

# List of token names.   This is always required
tokens = (
  'SOURCE',
  'L_PAREN',
  'R_PAREN',
  'ENTRYORGUID', # entryorguid
  'NUMBER',
  'SMART_EVENT_TYPE',
  'SMART_ACTION_TYPE',
  'SMART_TARGET_TYPE',
  'PARAM_NAME',
  'EQUAL',
  'D_SLASH',
  'COMMA',
  'TYPE'
)

t_TYPE = r'TYPE'
t_SOURCE = r'CREATURE|GAMEOBJECT|AREATRIGGER|EVENT|GOSSIP|QUEST|SPELL|TRANSPORT|INSTANCE|TIMED_ACTIONLIST'
t_PARAM_NAME= r'LINK|PHASE|FLAGS|CHANCE|(\*\w+)'
t_ENTRYORGUID = r'ENTRY|GUID'
t_EQUAL = r'='
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_COMMA = r','

def t_D_SLASH(t):
  r'\/\/(\w|.| )+'

def t_SMART_EVENT_TYPE(t):
  r'SMART_EVENT_UPDATE_IC|SMART_EVENT_UPDATE_OOC|SMART_EVENT_HEALT_PCT|SMART_EVENT_MANA_PCT|SMART_EVENT_AGGRO|SMART_EVENT_KILL|SMART_EVENT_DEATH|SMART_EVENT_EVADE|SMART_EVENT_SPELLHIT|SMART_EVENT_RANGE|SMART_EVENT_OOC_LOS|SMART_EVENT_RESPAWN|SMART_EVENT_TARGET_HEALTH_PCT|SMART_EVENT_VICTIM_CASTING|SMART_EVENT_FRIENDLY_HEALTH|SMART_EVENT_FRIENDLY_IS_CC|SMART_EVENT_FRIENDLY_MISSING_BUFF|SMART_EVENT_SUMMONED_UNIT|SMART_EVENT_TARGET_MANA_PCT|SMART_EVENT_ACCEPTED_QUEST|SMART_EVENT_REWARD_QUEST|SMART_EVENT_REACHED_HOME|SMART_EVENT_RECEIVE_EMOTE|SMART_EVENT_HAS_AURA|SMART_EVENT_TARGET_BUFFED|SMART_EVENT_RESET|SMART_EVENT_IC_LOS|SMART_EVENT_PASSENGER_BOARDED|SMART_EVENT_PASSENGER_REMOVED|SMART_EVENT_CHARMED|SMART_EVENT_CHARMED_TARGET|SMART_EVENT_SPELLHIT_TARGET|SMART_EVENT_DAMAGED|SMART_EVENT_DAMAGED_TARGET|SMART_EVENT_MOVEMENTINFORM|SMART_EVENT_SUMMON_DESPAWNED|SMART_EVENT_CORPSE_REMOVED|SMART_EVENT_AI_INIT|SMART_EVENT_DATA_SET|SMART_EVENT_WAYPOINT_START|SMART_EVENT_WAYPOINT_REACHED|SMART_EVENT_TRANSPORT_ADDPLAYER|SMART_EVENT_TRANSPORT_ADDCREATURE|SMART_EVENT_TRANSPORT_REMOVE_PLAYER|SMART_EVENT_TRANSPORT_RELOCATE|SMART_EVENT_INSTANCE_PLAYER_ENTER|SMART_EVENT_AREATRIGGER_ONTRIGGER|SMART_EVENT_QUEST_ACCEPTED|SMART_EVENT_QUEST_OBJ_COPLETETION|SMART_EVENT_QUEST_COMPLETION|SMART_EVENT_QUEST_REWARDED|SMART_EVENT_QUEST_FAIL|SMART_EVENT_TEXT_OVER|SMART_EVENT_RECEIVE_HEAL|SMART_EVENT_JUST_SUMMONED|SMART_EVENT_WAYPOINT_PAUSED|SMART_EVENT_WAYPOINT_RESUMED|SMART_EVENT_WAYPOINT_STOPPED|SMART_EVENT_WAYPOINT_ENDED|SMART_EVENT_TIMED_EVENT_TRIGGERED|SMART_EVENT_UPDATE|SMART_EVENT_LINK|SMART_EVENT_GOSSIP_SELECT|SMART_EVENT_JUST_CREATED|SMART_EVENT_GOSSIP_HELLO|SMART_EVENT_FOLLOW_COMPLETED|SMART_EVENT_DUMMY_EFFECT|SMART_EVENT_IS_BEHIND_TARGET|SMART_EVENT_GAME_EVENT_START|SMART_EVENT_GAME_EVENT_END|SMART_EVENT_GO_STATE_CHANGED|SMART_EVENT_GO_EVENT_INFORM|SMART_EVENT_ACTION_DONE|SMART_EVENT_ON_SPELLCLICK|SMART_EVENT_FRIENDLY_HEALTH_PCT|SMART_EVENT_DISTANCE_CREATURE|SMART_EVENT_DISTANCE_GAMEOBJECT|SMART_EVENT_COUNTER_SET'
  t.value = {"name" : t.value, "value" :  getEventTypeId(t.value)}
  return t

def t_SMART_ACTION_TYPE(t):
  r'SMART_ACTION_NONE|SMART_ACTION_TALK|SMART_ACTION_SET_FACTION|SMART_ACTION_MORPH_TO_ENTRY_OR_MODEL|SMART_ACTION_SOUND|SMART_ACTION_PLAY_EMOTE|SMART_ACTION_FAIL_QUEST|SMART_ACTION_ADD_QUEST|SMART_ACTION_SET_REACT_STATE|SMART_ACTION_ACTIVATE_GOBJECT|SMART_ACTION_RANDOM_EMOTE|SMART_ACTION_CAST|SMART_ACTION_SUMMON_CREATURE|SMART_ACTION_THREAT_SINGLE_PCT|SMART_ACTION_THREAT_ALL_PCT|SMART_ACTION_CALL_AREAEXPLOREDOREVENTHAPPENS|SMART_ACTION_SET_INGAME_PHASE_GROUP|SMART_ACTION_SET_EMOTE_STATE|SMART_ACTION_SET_UNIT_FLAG|SMART_ACTION_REMOVE_UNIT_FLAG|SMART_ACTION_AUTO_ATTACK|SMART_ACTION_ALLOW_COMBAT_MOVEMENT|SMART_ACTION_SET_EVENT_PHASE|SMART_ACTION_INC_EVENT_PHASE|SMART_ACTION_EVADE|SMART_ACTION_FLEE_FOR_ASSIST|SMART_ACTION_CALL_GROUPEVENTHAPPENS|SMART_ACTION_COMBAT_STOP|SMART_ACTION_REMOVEAURASFROMSPELL|SMART_ACTION_FOLLOW|SMART_ACTION_RANDOM_PHASE|SMART_ACTION_RANDOM_PHASE_RANGE|SMART_ACTION_RESET_GOBJECT|SMART_ACTION_CALL_KILLEDMONSTER|SMART_ACTION_SET_INST_DATA|SMART_ACTION_SET_INST_DATA64|SMART_ACTION_UPDATE_TEMPLATE|SMART_ACTION_DIE|SMART_ACTION_SET_IN_COMBAT_WITH_ZONE|SMART_ACTION_CALL_FOR_HELP|SMART_ACTION_SET_SHEATH|SMART_ACTION_FORCE_DESPAWN|SMART_ACTION_SET_INVINCIBILITY_HP_LEVEL|SMART_ACTION_MOUNT_TO_ENTRY_OR_MODEL|SMART_ACTION_SET_INGAME_PHASE_ID|SMART_ACTION_SET_DATA|SMART_ACTION_MOVE_FORWARD|SMART_ACTION_SET_VISIBILITY|SMART_ACTION_SET_ACTIVE|SMART_ACTION_ATTACK_START|SMART_ACTION_SUMMON_GO|SMART_ACTION_KILL_UNIT|SMART_ACTION_ACTIVATE_TAXI|SMART_ACTION_WP_START|SMART_ACTION_WP_PAUSE|SMART_ACTION_WP_STOP|SMART_ACTION_ADD_ITEM|SMART_ACTION_REMOVE_ITEM|SMART_ACTION_INSTALL_AI_TEMPLATE|SMART_ACTION_SET_RUN|SMART_ACTION_SET_FLY|SMART_ACTION_SET_SWIM|SMART_ACTION_TELEPORT|SMART_ACTION_SET_COUNTER|SMART_ACTION_STORE_TARGET_LIST|SMART_ACTION_WP_RESUME|SMART_ACTION_SET_ORIENTATION|SMART_ACTION_CREATE_TIMED_EVENT|SMART_ACTION_PLAYMOVIE|SMART_ACTION_MOVE_TO_POS|SMART_ACTION_RESPAWN_TARGET|SMART_ACTION_EQUIP|SMART_ACTION_CLOSE_GOSSIP|SMART_ACTION_TRIGGER_TIMED_EVENT|SMART_ACTION_REMOVE_TIMED_EVENT|SMART_ACTION_ADD_AURA|SMART_ACTION_OVERRIDE_SCRIPT_BASE_OBJECT|SMART_ACTION_RESET_SCRIPT_BASE_OBJECT|SMART_ACTION_CALL_SCRIPT_RESET|SMART_ACTION_SET_RANGED_MOVEMENT|SMART_ACTION_CALL_TIMED_ACTIONLIST|SMART_ACTION_SET_NPC_FLAG|SMART_ACTION_ADD_NPC_FLAG|SMART_ACTION_REMOVE_NPC_FLAG|SMART_ACTION_SIMPLE_TALK|SMART_ACTION_INVOKER_CAST|SMART_ACTION_CROSS_CAST|SMART_ACTION_CALL_RANDOM_TIMED_ACTIONLIST|SMART_ACTION_CALL_RANDOM_RANGE_TIMED_ACTIONLIST|SMART_ACTION_RANDOM_MOVE|SMART_ACTION_SET_UNIT_FIELD_BYTES_1|SMART_ACTION_REMOVE_UNIT_FIELD_BYTES_1|SMART_ACTION_INTERRUPT_SPELL|SMART_ACTION_SEND_GO_CUSTOM_ANIM|SMART_ACTION_SET_DYNAMIC_FLAG|SMART_ACTION_ADD_DYNAMIC_FLAG|SMART_ACTION_REMOVE_DYNAMIC_FLAG|SMART_ACTION_JUMP_TO_POS|SMART_ACTION_SEND_GOSSIP_MENU|SMART_ACTION_GO_SET_LOOT_STATE|SMART_ACTION_SEND_TARGET_TO_TARGET|SMART_ACTION_SET_HOME_POS|SMART_ACTION_SET_HEALTH_REGEN|SMART_ACTION_SET_ROOT|SMART_ACTION_SET_GO_FLAG|SMART_ACTION_ADD_GO_FLAG|SMART_ACTION_REMOVE_GO_FLAG|SMART_ACTION_SUMMON_CREATURE_GROUP|SMART_ACTION_SET_POWER|SMART_ACTION_ADD_POWER|SMART_ACTION_REMOVE_POWER|SMART_ACTION_GAME_EVENT_STOP|SMART_ACTION_GAME_EVENT_START|SMART_ACTION_START_CLOSEST_WAYPOINT|SMART_ACTION_RISE_UP|SMART_ACTION_RANDOM_SOUND|SMART_ACTION_SET_CORPSE_DELAY'
  t.value = {"name" : t.value, "value" :  getActionTypeId(t.value)}
  return t

def t_SMART_TARGET_TYPE(t):
  r'SMART_TARGET_NONE|SMART_TARGET_SELF|SMART_TARGET_VICTIM|SMART_TARGET_HOSTILE_SECOND_AGGRO|SMART_TARGET_HOSTILE_LAST_AGGRO|SMART_TARGET_HOSTILE_RANDOM_NOT_TOP|SMART_TARGET_HOSTILE_RANDOM|SMART_TARGET_ACTION_INVOKER|SMART_TARGET_POSITION|SMART_TARGET_CREATURE_RANGE|SMART_TARGET_CREATURE_GUID|SMART_TARGET_CREATURE_DISTANCE|SMART_TARGET_STORED|SMART_TARGET_GAMEOBJECT_RANGE|SMART_TARGET_GAMEOBJECT_GUID|SMART_TARGET_GAMEOBJECT_DISTANCE|SMART_TARGET_INVOKER_PARTY|SMART_TARGET_PLAYER_RANGE|SMART_TARGET_PLAYER_DISTANCE|SMART_TARGET_CLOSEST_CREATURE|SMART_TARGET_CLOSEST_GAMEOBJECT|SMART_TARGET_CLOSEST_PLAYER|SMART_TARGET_ACTION_INVOKER_VEHICLE|SMART_TARGET_OWNER_OR_SUMMONER|SMART_TARGET_THREAT_LIST|SMART_TARGET_CLOSEST_ENEMY|SMART_TARGET_CLOSEST_FRIENDLY'
  t.value = {"name" : t.value, "value" :  getTargetTypeId(t.value)}
  return t

def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    #numbers with comma or numbers with no comma
    if t.value.isdigit():
        number_value = int(t.value)
        number_type = "int"
    else:
        number_value = float(t.value)
        number_type = "float"
    t.value = Number(number_value, number_type)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# this function returns tokens from data input as a list
def apply(data):
  # Give the lexer some input
  lexer.input(data)
  return list(lexer)
