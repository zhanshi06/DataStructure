In Windows Active Directory, a group can consist of user(s) and group(s) themselves. The program recursively explores each directory and its sub-directories on whether or not a user is a member of the given group. The time and space complexity is O(#of groups in a group * #of users in each of those groups)
Time complexity of this process is O(# of groups + # of users) and space complexity is O(depth * users)

