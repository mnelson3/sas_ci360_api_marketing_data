# How to Contribute

We'd love to accept your patches and contributions to this project. There are just a few small guidelines you need to follow.

## Contributor License Agreement

Contributions to this project must be accompanied by a signed
[Contributor Agreement](CONTRIBUTOR_AGREEMENT.txt). You (or your employer) retain the copyright to your contribution, this simply gives us permission to use and redistribute your
contributions as part of the project.

## Branching model

This project uses three long-lived branches:

- `develop` - active integration branch; feature branches target this branch.
- `staging` - pre-release integration testing; `develop` is merged here when a release is being prepared.
- `main` - stable, released code; only `staging` is merged here, and each merge should correspond to a tagged release.

Create feature branches off `develop` (e.g. `feature/my-change`), and open a pull request back into `develop`.

## Code reviews

All submissions, including submissions by project members, require review. We use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more information on using pull requests.
