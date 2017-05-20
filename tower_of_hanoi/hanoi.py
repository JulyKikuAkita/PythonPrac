# Solve the classic puzzle Tower of Hanoi
# hanoi(1, "Middle", "Left", "Right")
# Move top ring in 'Middle' tower to the 'Left' tower

__author__ = 'July'
class towerOfHanoi:

    def print_move(self, fr, to):
        print "- Move top ring in '{}' tower to the '{}' tower".format(fr, to)

    def hanoi(self, n, source, helper, target):
        if n == 1: self.print_move(source, target)
        if n > 0:
        # move tower of size n - 1 to helper:
            self.hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
            self. hanoi(n - 1, helper, source, target)


    def hanoiKnowDetails(self, n, source, helper, target):
        print "hanoi( ", n, source, helper, target, " called"
        if n > 0:
            # move tower of size n - 1 to helper:
            self.hanoiKnowDetails(n - 1, source, target, helper)
            # move disk from source peg to target peg
            if source[0]:
                disk = source[0].pop()
                print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
                target[0].append(disk)
            # move tower of size n-1 from helper to target
            self.hanoiKnowDetails(n - 1, helper, source, target)

source = [4,3,2,1]
target = []
helper = []
#towerOfHanoi().hanoi(len(source),source,helper,target)
#print source, helper, target




source = ([4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
towerOfHanoi().hanoiKnowDetails(len(source[0]),source,helper,target)

print source, helper, target