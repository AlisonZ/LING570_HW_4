
STATE_DICT = {}

def create_state_dict(line):
    line.rstrip()
    split_line = line.rstrip().split(" ")
    split_line.append("</s>")
    for i, token in enumerate(split_line):
        if i < len(split_line) - 2:
            w1_tag = split_line[i]
            w2_tag = split_line[i+1]
            w3_tag = split_line[i+2]
            if w3_tag == "</s>":
                w3_split = ["</s>", 'EOS']
            else:
                w3_split = w3_tag.split("/")

            w1_split = w1_tag.split("/")
            w2_split = w2_tag.split("/")
            
            w1_pos = w1_split[1]
            w2_pos = w2_split[1]
            w3_pos = w3_split[1]
            bigram = f"{w2_pos} {w3_pos}"
            if w1_pos in STATE_DICT:
                if bigram in STATE_DICT[w1_pos]:
                    STATE_DICT[w1_pos][bigram] +=1
                else:
                    STATE_DICT[w1_pos][bigram] = 1
            else:
                STATE_DICT[w1_pos] = {bigram: 1}        

def get_input():
    # TODO: change to take in info through cat
    output_file = './output_3.txt'
    input_file = './training_data.txt'

    with open(input_file, 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            create_state_dict(line)

    return output_file

def main():
    output_file = get_input()
    print(f"STATE {STATE_DICT}")
main()