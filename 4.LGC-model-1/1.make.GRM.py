import pandas as pd
import os
import subprocess
import multiprocessing

def process_line(line):
    b = line.split()
    bim_chr = bim[bim[0] == int(b[0])]
    bim_chr = bim_chr[bim_chr[3].between(int(b[1]), int(b[2]))]
    return bim_chr

def sig_pcut(top_p):
    lgc = pd.read_csv('../0.example_data/TA.OX.TA.UC.1.bivar.lava', sep='\s+')
    lgc_sorted = lgc.sort_values('p')
    lgc_cut = lgc_sorted.head(int(top_p))
    if lgc_sig.shape[0] > 0:
        lgc_sig[['chr','start','stop']].to_csv('sig.pos', index=None, header=None, sep='\t')
        res = pd.DataFrame()
        with open('sig.pos') as f:
            lines = f.readlines()
        with multiprocessing.Pool() as pool:
            results = pool.map(process_line, lines)
        res = pd.concat(results)
        res[1].to_csv('sig.snp', index=None, header=None)
        os.system('plink --bfile ../0.example_data/combined --exclude sig.snp --make-bed --out non_sig')
        os.system('plink --bfile ../0.example_data/combined --extract sig.snp --make-bed --out sig')

top_p = 5
bim = pd.read_csv('../0.example_data/combined.bim', sep='\s+', header=None)
sig_pcut(top_p)
run_script='gmat2 --make-grm --bfile sig --out sig --threads 30'
subprocess.run(run_script, shell=True)
run_script='gmat2 --make-grm --bfile non_sig --out non_sig --threads 30'
subprocess.run(run_script, shell=True)
