input_01=[2,3,1,3,4,2]
input_02=[1,7,1,1,1,1]

class JumpControl:
    def __init__(self) -> None:
        pass
    
    def jump(self, _input:list):
        return 0


class Main:  
    def start_jump(self, _input:list):
        return JumpControl().jump(_input)
    


if __name__ == "__main__":
    result_01=Main().start_jump(input_01)
    if int(result_01) == 3:
        print("Passed")
    else:
        print("Wrong!")
    print("Expected return: 3")
    print("Jumps: ",result_01)
    print("-"*30)
    
    result_02=Main().start_jump(input_02)
    if int(result_02) == 2:
        print("Passed")
    else:
        print("Wrong!")
    print("Expected return: 2")
    print("Jumps: ", result_01)
    print("-"*30)
    print(result_02)