import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def is_word(word):
	# English words do not have non-alphanumeric characters
	return word.isalpha()

words = []
with open("./top_2000000.txt", 'r') as f:
    for line in f:
        values = line.split()
        if is_word(values[0]):
        	words.append(values[0])


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



df = pd.DataFrame()



df["words"] = words
df["word_rank"] = np.array([x for x in range(len(words))])+1
df["is_k1_word"] = np.array([is_k1(w)  for w in words])
df["is_k3_word"] = np.array([is_k3(w)  for w in words])
df["cum_k1_count"] = df["is_k1_word"].cumsum()
df["cum_k3_count"] = df["is_k3_word"].cumsum()
df["k1_freq"] = df["cum_k1_count"]/df["word_rank"]
df["k3_freq"] = df["cum_k3_count"]/df["word_rank"]

df2 = df




df = df.head(1000000)
print("1,000,000: ")
print("k-1st words: ",df["is_k1_word"].sum() )
print("k-3rd words: ",df["is_k3_word"].sum() )

plt.figure()
plt.title("Top " + "1,000,000" + " words")
plt.plot(df["k1_freq"],"r", label = "k-1st")
plt.plot(df["k3_freq"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Frequency")
plt.legend(loc='best')
plt.show()





df = df.head(100000)
print("100,000: ")
print("k-1st words: ",df["is_k1_word"].sum() )
print("k-3rd words: ",df["is_k3_word"].sum() )

plt.figure()
plt.title("Top " + "100,000" + " words")
plt.plot(df["k1_freq"],"r", label = "k-1st")
plt.plot(df["k3_freq"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Frequency")
plt.legend(loc='best')
plt.show()



df = df.head(10000)
print("10,000: ")
print("k-1st words: ",df["is_k1_word"].sum() )
print("k-3rd words: ",df["is_k3_word"].sum() )

plt.figure()
plt.title("Top " + "10,000" + " words")
plt.plot(df["k1_freq"],"r", label = "k-1st")
plt.plot(df["k3_freq"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Frequency")
plt.legend(loc='best')
plt.show()



df = df.head(1000)
print("1,000: ")
print("k-1st words: ",df["is_k1_word"].sum() )
print("k-3rd words: ",df["is_k3_word"].sum() )

plt.figure()
plt.title("Top " + "1,000" + " words")
plt.plot(df["k1_freq"],"r", label = "k-1st")
plt.plot(df["k3_freq"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Frequency")
plt.legend(loc='best')
plt.show()




# ADJUSTED GRAPHS
# VVVVVVVVVVVVVVV

df = df2



df["word_freq"] = .07/df["word_rank"]
df["cum_word_freq"] = df["word_freq"].cumsum()

df["is_k1_word_adj"]= df["is_k1_word"]*df["word_freq"]
df["is_k3_word_adj"]= df["is_k3_word"]*df["word_freq"]
df["cum_k1_count_adj"] = df["is_k1_word_adj"].cumsum()
df["cum_k3_count_adj"] = df["is_k3_word_adj"].cumsum()
df["k1_freq_adj"] = df["cum_k1_count_adj"]/df["word_rank"]
df["k3_freq_adj"] = df["cum_k3_count_adj"]/df["word_rank"]

df3 = df


df = df.head(1000000)

plt.figure()
plt.title("Top " + "1,000,000" + " words")
plt.plot(df["k1_freq_adj"],"r", label = "k-1st")
plt.plot(df["k3_freq_adj"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted frequency")
plt.legend(loc='best')
plt.show()





df = df.head(100000)

plt.figure()
plt.title("Top " + "100,000" + " words")
plt.plot(df["k1_freq_adj"],"r", label = "k-1st")
plt.plot(df["k3_freq_adj"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted frequency")
plt.legend(loc='best')
plt.show()



df = df.head(10000)

plt.figure()
plt.title("Top " + "10,000" + " words")
plt.plot(df["k1_freq_adj"],"r", label = "k-1st")
plt.plot(df["k3_freq_adj"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Ajusted frequency")
plt.legend(loc='best')
plt.show()



df = df.head(1000)

plt.figure()
plt.title("Top " + "1,000" + " words")
plt.plot(df["k1_freq_adj"],"r", label = "k-1st")
plt.plot(df["k3_freq_adj"],"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted frequency")
plt.legend(loc='best')
plt.show()



# ADJUSTED LOG GRAPHS
# VVVVVVVVVVVVVVVVVVV

df = df3




df = df.head(1000000)

plt.figure()
plt.title("Top " + "1,000,000" + " words")
plt.plot(np.log(df["k1_freq_adj"]),"r", label = "k-1st")
plt.plot(np.log(df["k3_freq_adj"]),"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted log frequency")
plt.legend(loc='best')
plt.show()





df = df.head(100000)

plt.figure()
plt.title("Top " + "100,000" + " words")
plt.plot(np.log(df["k1_freq_adj"]),"r", label = "k-1st")
plt.plot(np.log(df["k3_freq_adj"]),"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted log frequency")
plt.legend(loc='best')
plt.show()



df = df.head(10000)

plt.figure()
plt.title("Top " + "10,000" + " words")
plt.plot(np.log(df["k1_freq_adj"]),"r", label = "k-1st")
plt.plot(np.log(df["k3_freq_adj"]),"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Ajusted log frequency")
plt.legend(loc='best')
plt.show()



df = df.head(1000)

plt.figure()
plt.title("Top " + "1,000" + " words")
plt.plot(np.log(df["k1_freq_adj"]),"r", label = "k-1st")
plt.plot(np.log(df["k3_freq_adj"]),"b", label = "k-3rd")
plt.xlabel("Number of words")
plt.ylabel("Adjusted log frequency")
plt.legend(loc='best')
plt.show()
