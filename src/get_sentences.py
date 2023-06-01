import os
import sys
import pandas as pd

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

                if SENT_COUNTS == 0:
                    no_sent_found.append(con)
                    print(f"no_sent_found : {con}", flush=True)
                    print(flush=True)

    print(f"no_sent_found list: {no_sent_found}")


inp_text_file = "/scratch/c.scmag3/en_wikipedia/en_wikipedia.txt"
inp_concept = "dataset/cnetpchatgpt/con_vocab_cnetchatgpt.txt"
num_sents = 500


############################
out_file = "dataset/cnetpchatgpt/part2_con_sentences.tsv"


all_con_file = "dataset/cnetpchatgpt/con_vocab_cnetchatgpt.txt"
part1_file = "dataset/cnetpchatgpt/part1_con_sentences.tsv"

part1_con = pd.read_csv(part1_file, sep="\t", names=["concept", "sent"])[
    "concept"
].unique()

all_con = pd.read_csv(inp_concept, sep="\t", names=["concept"])["concept"].unique()

part2_con = [con for con in all_con if con not in part1_con]
part2_con.insert(0, "cooks")


print(f"part1_con len : {len(part1_con)}")
print(f"part2_con len : {len(part2_con)}")
print(f"all_con len : {len(all_con)}")


part2_inp_concept = "dataset/cnetpchatgpt/part2_con_vocab_cnetchatgpt.txt"
with open(part2_inp_concept, "w") as outfile:
    for con in part2_con:
        outfile.write(f"{con.strip()}\n")

############################

if __name__ == "__main__":
    get_sentences(
        text_file=inp_text_file,
        con_file=part2_inp_concept,
        num_sents=num_sents,
        outfile_name=out_file,
    )

    parts = [
        "dataset/cnetpchatgpt/part1_con_sentences.tsv",
        "dataset/cnetpchatgpt/part2_con_sentences.tsv",
    ]

    df = pd.DataFrame()
    for part in parts:
        part_df = pd.read_csv(part, sep="\t", names=["concept", "sent"])
        df = pd.concat((df, part_df), axis=0, ignore_index=True)

    df.drop_duplicates(inplace=True)

    final_file = "dataset/cnetpchatgpt/all_con_sentences.tsv"

    print(f"final_df_shape : {df.shape}")

    df.to_csv(
        final_file,
        sep="\t",
        header=False,
        index=False,
    )
