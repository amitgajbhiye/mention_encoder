#!/bin/bash --login

#SBATCH --job-name=getSents

#SBATCH --output=logs/get_sents/out_get_wiki_sents.txt
#SBATCH --error=logs/get_sents/err_get_wiki_sents.txt

#SBATCH --tasks-per-node=5
#SBATCH --ntasks=5
#SBATCH -A scw1858

#SBATCH -p compute


#SBATCH --mem=16G
#SBATCH -t 0-00:30:00

conda activate venv


python3 src/get_sentences.py

echo 'Job Finished !!!'