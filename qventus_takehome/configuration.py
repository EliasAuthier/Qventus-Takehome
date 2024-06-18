from environs import Env

env = Env()
try:
    env.read_env()
except OSError: 
    env.read_env('.env')