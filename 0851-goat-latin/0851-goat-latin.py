class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """

        vowel = ["a","e","i","o","u"]
        count=1
        words= sentence.split()

        for i in range(len(words)):
            if words[i] and words[i][0].lower() in vowel:
                words[i]= words[i] + "ma"
            else:
                delete_letter = words[i][0]
                words[i] = words[i][1:] + delete_letter + "ma"

            words[i] = words[i] + "a"*count
            count = count + 1

        sentence = " ".join(words)
        return sentence