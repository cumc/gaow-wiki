# Python tips

## Performance tips

### Overall performance

```
python -m cProfile encode-linkage --vcf 19.vcf.gz --tfam 19.tfam --vanilla -j4 > profile.log
cat profile.log | grep -v -e 'argparse\|time\|posix\|threading\|urllib' | sort -k4 -g -r | head -50
```

### Time per line

```
pip install line_profiler
kernprof -l script_to_profile.py
python -m line_profiler script_to_profile.py.lprof
```

### Memory per line

```
pip install memory_profiler
python -m memory_profiler script_to_profile.py
```