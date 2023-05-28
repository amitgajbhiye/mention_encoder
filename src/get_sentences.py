import os
import sys

sys.path.insert(0, os.getcwd())


def get_sentences(text_file, con_file, num_sents, outfile_name):
    cons = [line.rstrip() for line in open(con_file)][0:2]

    print(f"num_concepts : {len(cons)}", flush=True)

    with open(outfile_name, "w") as out_file:
        with open(text_file, "r") as inp_file:
            for con in cons:
                SENT_COUNTS = 0

                for sent in inp_file:
                    if con in sent.split():
                        print(con, sent.strip(), flush=True)

                        out_file.write(f"{con}\t{sent}")

                        SENT_COUNTS += 1

                        if SENT_COUNTS >= num_sents:
                            print(f"sent_count : {SENT_COUNTS}", end="\n", flush=True)
                            break


inp_text_file = "/scratch/c.scmag3/en_wikipedia/en_wikipedia.txt"
inp_concept = "dataset/cnetpchatgpt/con_vocab_cnetchatgpt.txt"
out_file = "dataset/cnetpchatgpt/con_sentences.tsv"
num_sents = 10


get_sentences(
    text_file=inp_text_file,
    con_file=inp_concept,
    num_sents=num_sents,
    outfile_name=out_file,
)


if __name__ == "__main__":
    pass
