from base.ast import AST

class Program(AST):
    def __init__(self, port, action_list, agent_list, behavior_list, task_list, main):
        self.port = port
        self.action_list = action_list
        self.agent_list = agent_list
        self.behavior_list = behavior_list
        self.task_list = task_list
        self.main = main

class ActionList(AST):
    def __init__(self):
        self.children = []

class Action(AST):
    def __init__(self, name, formal_params, compound_statement):
        self.name = name
        self.formal_params = formal_params  # a list of Param nodes
        self.compound_statement = compound_statement

class AgentList(AST):
    def __init__(self):
        self.children = []

class Agent(AST):
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

class AgentCall(AST):
    def __init__(self, name, count):
        self.name = name
        self.count = count

class BehaviorList(AST):
    def __init__(self):
        self.children = []

class Behavior(AST):
    def __init__(self, name, formal_params, init_block, goal_block, routine_block):
        self.name = name
        self.formal_params = formal_params  # a list of Param nodes
        self.init_block = init_block
        self.goal_block = goal_block
        self.routine_block = routine_block

class BehaviorCall(AST):
    def __init__(self, name, actual_params, token):
        self.name = name
        self.actual_params = actual_params  # a list of AST nodes
        self.token = token
        self.symbol = None          # a reference to task symbol

class TaskList(AST):
    def __init__(self):
        self.children = []

class Task(AST):
    def __init__(self, name, formal_params, init_block, goal_block, routine_block):
        self.name = name
        self.formal_params = formal_params  # a list of Param nodes
        self.init_block = init_block
        self.goal_block = goal_block
        self.routine_block = routine_block

class TaskCall(AST):
    def __init__(self, name, actual_params, token):
        self.name = name
        self.actual_params = actual_params  # a list of AST nodes
        self.token = token
        self.symbol = None          # a reference to task symbol
    
class Main(AST):
    def __init__(self, agent_call, task_call):
        self.agent_call = agent_call
        self.task_call = task_call

class Compound(AST):
    """Represents a list of statements"""
    def __init__(self):
        self.children = []

class Param(AST):
    def __init__(self, var_node):
        self.var_node = var_node

class Var(AST):
    """The Var node is constructed out of ID token."""
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
