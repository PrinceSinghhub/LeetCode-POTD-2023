# class Solution:
#     def minimumRounds(self, task):
#
#         task.sort()
#
#
#         Min = 0
#         for i in task:
#
#             if len(task) > 0:
#
#                 if task.count(task[0]) < 2:
#                     return -1
#
#                 elif task.count(task[0]) == 2:
#                     Min += 1
#                     task = task[2::]
#
#                 elif task.count(task[0]) == 3:
#                     Min += 1
#                     task = task[3::]
#
#                 else:
#
#                     count1 = task.count(task[0])
#                     count = count1 // 2
#                     if count + count == count1:
#
#                         task = task[count::]
#                         Min += 1
#                     else:
#                         task = task[3::]
#                         Min += 1
#         return Min

class Solution1:
    def minimumRounds(self, tasks):

        tasks.sort()
        ans = 0

        index = len(tasks)

        while index > 0:


            if tasks.count(tasks[0]) < 2:
                return -1

            elif tasks.count(tasks[0]) % 2 == 0 and tasks.count(tasks[0]) % 3 != 0:
                tasks = tasks[2::]
                ans += 1
                index -= 2

            elif tasks.count(tasks[0]) % 3 == 0 and tasks.count(tasks[0]) % 2 != 0:
                tasks = tasks[3::]
                ans += 1
                index -= 3

            else:
                tasks = tasks[3::]
                ans += 1
                index -= 3

        return ans

# optimize code
from collections import Counter
class Solution:
    def minimumRounds(self, tasks):

        task_ct = Counter(tasks)

        if 1 in task_ct.values():
            return -1

        output = 0

        for i in task_ct.values():


            this_round = i // 3


            if i % 3 != 0:
                this_round += 1
            output += this_round

        return (output)
ans = Solution()
arr = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
print(ans.minimumRounds(arr))

