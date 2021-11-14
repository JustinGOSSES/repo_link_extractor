# repo_link_extractor
A github actions + python code to extract URLs to code repositories to put into standard form, starting with github

## ---- IN PROGRESS ----

### Summary

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
