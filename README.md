# repo_link_extractor
A github actions + python code to extract URLs to code repositories to put into standard form, starting with github

## ---- NOTE: JUST STARTED ONLY AN IDEA TO COME BACK TO ----

## Summary

#### first minimum viable product goal
The first minimum viable product goal will be to harvest from https://github.com/softwareunderground/awesome-open-geoscience/blob/main/README.md all the github repositories URLs such that the form returned is https://github.com/ + "username" + "repository name" and then add them to the "repos" key in an existing JSON in a form like this: https://github.com/softwareunderground/open_geosciene_code_projects_viz/blob/main/_explore/input_lists.json , which is summarized below:
```
{
    "memberOrgs": [
        "softwareunderground"
    ],
    "orgs": [
        "agile-geoscience",
        "softwareunderground"
    ],
    "repos": [
        "ahotovec/redpy",
        "whamlyn/auralib"
    ]
}
```

#### 2nd intermediate product goal
- Fires from a GitHubAction


#### 3rd intermediate product goal
- Integrated into https://github.com/softwareunderground/open_geosciene_code_projects_viz in terms of either internal code or dependency


#### Eventual product goal
- works for public, internal, and private GitHub URLs
- Works for GitHub, GitLab, BitBucket, and other code repository URLS & APIs
- Keeps track of harvest date, source file name, source file URL & code platform & domain in an intermediate file.

## Related Projects
This is referenced on an issue here: https://github.com/softwareunderground/open_geosciene_code_projects_viz/issues/23

## Potential Useful Bits
regular expression `(https:\/\/github.com\/)\w+(\/)\w+ ` seems like a good starting point for the extraction of Github URLs.


## GitHub Actions Structure Tentative:
- download README file
- replace old README file with new
- extract all links matching a regular expression
- sort & take out duplicates
- make into JSON with domain, URL, org or username, repository name, source file name, source file link, and date of harvests
- pull out org or username & repository name from above and put into appropriate key of the file JSON if not already there in either org or repo keys.

## How to Integrate into https://github.com/softwareunderground/open_geosciene_code_projects_viz ??????

#### Options:
1. Put all of the code here into the repository: https://github.com/softwareunderground/open_geosciene_code_projects_viz 
2. Call the code here from https://github.com/softwareunderground/open_geosciene_code_projects_viz


##### If calling the code....
- (1) add the script to read the README to MASTER.sh as the first step
- (2) set master.sh to be callled by GitHub actions
- (3) when triggered the github actions does the entirity of the github actions in this repo, including calling the python scripts as its first step. 
- (4) latter steps include setting up the environnment and calling all the python scripts that the master.sh bash script calls.
The code would need to be called by either a GitHub Action on (pull request, push, manual, or cron job) or by trigger after the call to refresh the 