# repo_link_extractor
A github actions + python code to extract URLs to code repositories to put into standard form, starting with github

## ---- NOTE: JUST STARTED ONLY AN IDEAD TO COME BACK TO ----

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
