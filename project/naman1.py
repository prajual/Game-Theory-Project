def biasedflip(p):
   import matplotlib.pyplot as plt
   import numpy as np
   import random

   if random.randint(1,100) < p:
      return 1
   else:
      return 0

