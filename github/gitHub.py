from github import Github as git
from github import GithubException

g_login = git("<USER_NAME>", "<PASSWORD>")

x = 0
total_stars = 0

for repo in g_login.get_user().get_repos():
    try:
        print("In the "+ str(repo.name) + " repo, the total no. of stars is " + str(repo.stargazers_count))
        print("traffic " + str(repo.get_views_traffic()))
        total_stars += repo.stargazers_count
        x += 1
    except GithubException:
        print("")


print("total repo is " + str(x))
print("Total stars is :- " + str(total_stars))