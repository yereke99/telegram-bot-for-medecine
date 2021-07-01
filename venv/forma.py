from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    surname_name = State()
    age = State()
    gender = State()
    which_blood = State()
    tele_number = State()

class wait_terapeft(StatesGroup):
    inn = State()
    yes = State()

class wait_lor(StatesGroup):
    inn = State()
    yes = State()

class wait_hirurg(StatesGroup):
    inn = State()
    yes = State()

class wait_oculist(StatesGroup):
    inn = State()
    yes = State()
    
class wait_pediatr(StatesGroup):
    inn = State()
    yes = State()

class wait_nevrolog(StatesGroup):
    inn = State()
    yes = State()

###################################
class spravka_sport(StatesGroup):
    inn = State()
    yes = State()
class spravka_086(StatesGroup):
    inn = State()
    yes = State()
class spravka_job(StatesGroup):
    inn = State()
    yes = State()