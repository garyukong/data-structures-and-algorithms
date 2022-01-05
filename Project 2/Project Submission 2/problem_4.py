class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Base case
    if user in group.users:
      return True

    # Traverse through each child group in the parent group
    else:
      for sub_group in group.groups:
        return is_user_in_group(user, sub_group)

    return False


def test_function(user, group, expected_answer):
    """
    Prints "Passed test" if the test case is valid. Prints "Failed test" otherwise
    """
    if is_user_in_group(user, group) == expected_answer:
        print("Passed test")
    else:
        print("Failed test")

if __name__ == "__main__":
    # Generates a directory for testing with the structure:
    # / Parent (Group)
    #   / Child1 (Group)
    #     / Child1_subgroup (Group)
    #       / Child1_subgroup_user (User)
    #   / Child2_user (User)
    #   / Child3 (Group)
    parent = Group('parent')
    child1 = Group('child1')
    child3 = Group('child3')
    child1_subgroup = Group('child1_subgroup')

    parent.add_group(child1)
    parent.add_group(child3)

    child1_subgroup_user = 'child1_subgroup_user'
    child1_subgroup.add_user(child1_subgroup_user)

    child2_user = 'child2_user'
    parent.add_user(child2_user)

    # Test Case 1: Normal case
    print("\nTEST CASE 1: Normal case: user is in the group\n----------------------------------------------------------------")
    test_function(child2_user, parent, True)
    test_function(child1_subgroup_user, child1_subgroup, True)

    # Test Case 2: 'User' is actually a group
    print('\nTEST CASE 2: User is actually a group\n----------------------------------------------------------------')
    test_function(child1, parent, False)
    test_function(child1_subgroup, child1, False)

    # Test Case 3: 'User doesn't exist
    print('\nTEST CASE 3: User does not exist\n----------------------------------------------------------------')
    test_function('Joe', parent, False)
    test_function('Joe', child1, False)

    # Test Case 4: Empty user
    print('\nTEST CASE 4: Empty user\n----------------------------------------------------------------')
    test_function('', parent, False)
    test_function('', child1, False)

    # Test case 5: Empty group
    print('\nTEST CASE 5: Empty group\n----------------------------------------------------------------')
    test_function(child2_user, '', False)
    # Should return an error because the function cannot take in an empty group (IN operation doesn't work)