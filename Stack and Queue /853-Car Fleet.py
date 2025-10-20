class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position, speed), reverse=True)
        stack=[]

        for pos, spd in cars:
            time=(target-pos)/spd
            if not stack or time> stack[-1]:    #If current car takes more time → new fleet
                stack.append(time)

        return len(stack)   #number of fleets =size of stack
