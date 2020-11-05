## pass-ch

Simple scripts for answering questions any student had throughout their stay at EPFL.

## Features

- Say you want to know how many points to score on a final exam to reach the desired mark (here, the smallest score yielding a 4/6 result via rounding), knowing your scores to two intermediary tests accounting for 15% each  
```python pass.py --marks 84/100 74/100 --weights 0.15 0.15 --target 57.5/100```

- Or perhaps you're wondering what subjects you could fail without affecting your credits goal of 30 credits for this semester, the possibly failed courses accounting for 7, 5 and 4 credits resptectively, with 19 credits already obtained  
```python credits.py 30 19 --credits 7 5 4```
