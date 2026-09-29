class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        h_l = 0
        sender_name = ""
        dict = {}
        for i in range(len(messages)):
            if senders[i] not in dict:
                dict[senders[i]] = len(messages[i].split())
            else:
                dict[senders[i]] += len(messages[i].split())

            mass = dict[senders[i]]
            if mass > h_l:
                h_l = mass
                sender_name = senders[i]
            elif mass == h_l:
                if senders[i] > sender_name:
                    sender_name = senders[i]
        return sender_name