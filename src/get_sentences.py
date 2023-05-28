import os
import sys

sys.path.insert(0, os.getcwd())


def get_sentences(text_file, con_file, num_sents, outfile_name):
    cons = [line.rstrip() for line in open(con_file)]

    print(f"num_concepts : {len(cons)}", flush=True)
    no_sent_found = []

    with open(outfile_name, "w") as out_file:
        for idx, con in enumerate(cons):
            SENT_COUNTS = 0

            print(flush=True)
            print(f"processing_con : {con}, {idx}/{len(cons)}")

            with open(text_file, "r") as inp_file:
                for sent in inp_file:
                    if con in sent.split():
                        print(SENT_COUNTS, con, sent.strip(), flush=True)

                        out_file.write(f"{con}\t{sent.strip()}\n")

                        SENT_COUNTS += 1

                        if SENT_COUNTS >= num_sents:
                            print(f"sent_count : {SENT_COUNTS}", flush=True)
                            print(f"breaking_out", flush=True)
                            print
                            break
                    else:
                        pass
                        # print(f"{con} : not_found")
                no_sent_found.append(con)

    print(f"no_sent_found : {no_sent_found}")


inp_text_file = "/scratch/c.scmag3/en_wikipedia/en_wikipedia.txt"
inp_concept = "dataset/cnetpchatgpt/con_vocab_cnetchatgpt.txt"
out_file = "dataset/cnetpchatgpt/con_sentences.tsv"
num_sents = 500


if __name__ == "__main__":
    get_sentences(
        text_file=inp_text_file,
        con_file=inp_concept,
        num_sents=num_sents,
        outfile_name=out_file,
    )
