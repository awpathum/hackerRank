class Token:
    def __init__(self, id, token_exp_time) -> None:
        # self.action = action
        self.id = id
        self.token_exp_time = token_exp_time
    
    def __str__(self):
        # return f"Person (Name: {self.name}, Age: {self.age})"
        return f"id : {self.id} | time: {self.token_exp_time}"


system_tokens = {}


def numberOfTokens(expiryLimit, commands):
    # print(commands)
    # active_token_count = 0
    T = 0
    for com in commands:
        action, id, system_time = com
        print(f"System Time : {system_time}")
        
        if action == 0:
            token = Token(id, system_time + expiryLimit)
            print(f"Add: {token.id} | system_time : {system_time}")
            system_tokens[id] = token
            # print(f"Add: {token}")
        elif action == 1:
            # print(f"Rest: {id} | system_time = {system_time}")
            if id in system_tokens.keys():
                system_token = system_tokens[id]
                if system_token.token_exp_time < system_time:
                    system_tokens.pop(id)
                    print(f"remove {system_token}")
                else:
                    system_token.token_exp_time = system_time + expiryLimit
                    system_tokens[id] = system_token
                    print(f"Token After reset = {system_token}")
            else:
                # print("Expired: {id}")
                pass
        
        T = system_time
        print("#################")
        
    active_tokens = 0
    print(f"System Time : {T}")
    for t in system_tokens.values():
        if t.token_exp_time >= T:
            print(f"Active tokens: {t}")
            active_tokens = active_tokens +1
        else:
            print(f"Expired : {t}")

    return active_tokens
    



# commands = [[0,1,1],[0,2,2],[1,1,5],[1,2,7]]
# expiryLimit = 4


expiryLimit = 4
commands = [
  [0, 1, 1],
  [0, 2, 2],
  [0, 3, 3],
  [1, 1, 4],
  [1, 2, 5],
  [1, 3, 6],
  [0, 4, 7],
  [1, 1, 8],
  [1, 4, 9],
  [0, 5, 10],
  [1, 5, 11],
  [1, 3, 12]
]







valid_tokens = numberOfTokens(expiryLimit,commands)
print(valid_tokens)

