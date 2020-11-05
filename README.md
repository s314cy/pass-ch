# Pass CH

Example usages:

- Say you want to know how many points to score on a final exam to reach the desired mark (here, the smallest score yielding a 4/6 result via rounding), knowing your scores to two intermediary tests accounting for 15% each  
```python pass.py --marks 88/100 79/100 --weights 0.15/0.7 0.15/0.7 --target 57.5/100```

- Or perhaps you're wondering what subjects you could fail without affecting your credits goal of 30 credits for this semester, the possibly failed courses accounting for 7, 5 and 4 credits resptectively, with 19 credits already obtained  
```python credits.py 30 19 --credits 7 5 4```
