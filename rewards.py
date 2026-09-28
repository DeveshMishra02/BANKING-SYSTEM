from account import account

def show_rewards():
    print("\n===== REWARD POINTS =====")
    points = account["reward_points"]
    print("Your reward points:", points)

    if points >= 100:
        print("Reward status: Gold")
    elif points >= 50:
        print("Reward status: Silver")
    else:
        print("Keep using your account to earn more points.")
