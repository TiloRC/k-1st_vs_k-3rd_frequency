import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


def read_most_common_words(filepath):
        """reads words from  from each line, excluding words with non-letter characters"""
        words = []
        with open(filepath, 'r') as f:
                for line in f:
                        values = line.split()
                        if values[0].isalpha():
        	                words.append(values[0])
        return words


def is_k1(word):
	if len(word) >= 1:
		if word[0] == "k":
			return True
	return False

def is_k3(word):
	if len(word) >= 3:
		if word[2] == "k":
			return True
	return False


filepath = "./top_2000000.txt"
words = read_most_common_words(filepath)
df = pd.DataFrame()


df["words"] = words
df["word_rank"] = np.array([x for x in range(len(words))])+1
df["is_k1_word"] = np.array([is_k1(w)  for w in words])
df["is_k3_word"] = np.array([is_k3(w)  for w in words])
df["cum_k1_count"] = df["is_k1_word"].cumsum()
df["cum_k3_count"] = df["is_k3_word"].cumsum()
df["k1_freq"] = df["cum_k1_count"]/df["word_rank"]
df["k3_freq"] = df["cum_k3_count"]/df["word_rank"]
unaltered_df = df
num_rows_values = [1000000, 100000, 10000, 1000]

for num_rows in num_rows_values:
        df = df.head(num_rows)
        print("{:,}".format(num_rows), ": ")
        print("k-1st words: ",df["is_k1_word"].sum() )
        print("k-3rd words: ",df["is_k3_word"].sum() )
        plt.figure()
        plt.title("Top " + "{:,}".format(num_rows) + " words")
        plt.plot(df["k1_freq"],"r", label = "k-1st")
        plt.plot(df["k3_freq"],"b", label = "k-3rd")
        plt.xlabel("Number of words")
        plt.ylabel("Frequency")
        plt.legend(loc='best')
        plt.show()

        
df = unaltered_df
df["word_freq"] = .07/df["word_rank"]
df["cum_word_freq"] = df["word_freq"].cumsum()
df["is_k1_word_adj"]= df["is_k1_word"]*df["word_freq"]
df["is_k3_word_adj"]= df["is_k3_word"]*df["word_freq"]
df["cum_k1_count_adj"] = df["is_k1_word_adj"].cumsum()
df["cum_k3_count_adj"] = df["is_k3_word_adj"].cumsum()
df["k1_freq_adj"] = df["cum_k1_count_adj"]/df["word_rank"]
df["k3_freq_adj"] = df["cum_k3_count_adj"]/df["word_rank"]


adjusted_df = df
for num_rows in num_rows_values:
        df = df.head(num_rows)
        print("k-1st words: ",df["is_k1_word"].sum() )
        print("k-3rd words: ",df["is_k3_word"].sum() )
        plt.figure()
        plt.title("Top " + "{:,}".format(num_rows) + " words")
        plt.plot(df["k1_freq_adj"],"r", label = "k-1st")
        plt.plot(df["k3_freq_adj"],"b", label = "k-3rd")
        plt.xlabel("Number of words")
        plt.ylabel("Adjusted frequency")
        plt.legend(loc='best')
        plt.show()



df = adjusted_df
for num_rows in num_rows_values:
        df = df.head(num_rows)
        print("k-1st words: ",df["is_k1_word"].sum() )
        print("k-3rd words: ",df["is_k3_word"].sum() )
        plt.figure()
        plt.title("Top " + "{:,}".format(num_rows) + " words")
        plt.plot(np.log(df["k1_freq_adj"]),"r", label = "k-1st")
        plt.plot(np.log(df["k3_freq_adj"]),"b", label = "k-3rd")
        plt.xlabel("Number of words")
        plt.ylabel("Adjusted log frequency")
        plt.legend(loc='best')
        plt.show()
